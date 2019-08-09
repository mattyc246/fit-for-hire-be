from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv
load_dotenv()
from commands import seed
from models.base_model import db
from flask import Flask
import os
import config

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


@socketio.on('my event')
def receive_message(data):
    emit('incoming_message', data)
