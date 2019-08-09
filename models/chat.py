import peewee as pw
from models.base_model import BaseModel
from models.user import User

class Chat(BaseModel):
    customer = pw.ForeignKeyField(User, backref="chats")
    professional = pw.ForeignKeyField(User, backref=)