from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    full_name = pw.CharField(unique=False, null=False)
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique=True, null=False)
    phone_number = pw.CharField(null=False)
    password = pw.CharField(null=False)
    date_of_birth = pw.DateField(null=False)
