import peewee as pw
from models.base_model import BaseModel
from models.chat_room import ChatRoom
from models.user import User


class Message(BaseModel):
    room = pw.ForeignKeyField(ChatRoom, backref="messages")
    sender = pw.ForeignKeyField(User, backref="messages")
    body = pw.TextField(null=True)
