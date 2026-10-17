from peewee import CharField, IntegerField

from .base import BaseModel
class User(BaseModel):
    name = CharField(unique=True,max_length=3)
    age = IntegerField(null=True)
    role = IntegerField(null=True,default=0)
    password = CharField(null=True,max_length=255)
    class Meta:
        db_table = 'sys_user'