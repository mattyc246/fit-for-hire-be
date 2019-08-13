import datetime
import time
import os
import config
from flask import Flask
from models.message import Message
from models.chat_room import ChatRoom
from models.user import User
from models.base_model import db
from commands import seed
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from dotenv import load_dotenv
load_dotenv()

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'fitforhire_web')

app = Flask('FITFORHIRE', root_path=web_dir)
app.cli.add_command(seed)
socketio = SocketIO(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc


@socketio.on('join_room')
def join(data):
    room_no = data['roomNo']
    join_room(room)


@socketio.on('leave_room')
def leave(data):
    room_no = data['roomNo']
    leave_room(room)


@socketio.on('message_out')
def receive_message(data):
    room_no = data['roomNo']
    room = ChatRoom.get(ChatRoom.room_no == room_no)
    message_body = data['message']
    sender = User.get(User.username == data['username'])

    new_message = Message(
        room_id=room.id,
        sender_id=sender.id,
        body=message_body,
    )

    new_message.save()

    return_data = {
        'message': message_body,
        'username': sender.username,
        'timestamp': time.mktime(datetime.datetime.today().timetuple())
    }

    emit('message_in', return_data)
