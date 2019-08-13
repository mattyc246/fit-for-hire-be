import peewee as pw
from models.base_model import BaseModel
from models.user import User


class ChatRoom(BaseModel):
    customer = pw.ForeignKeyField(User, backref="chats")
    professional = pw.ForeignKeyField(User, backref="chats")
    room_no = pw.CharField(null=False)
