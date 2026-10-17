from database import db
from peewee import Model, AutoField


class BaseModel(Model):
    id = AutoField()
    class Meta:
        database = db


    def dump(self):
        return {
            'id': self.id,
        }