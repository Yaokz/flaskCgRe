from charset_normalizer import models
from peewee import CharField, DecimalField, BooleanField

from .base import BaseModel
class Dish(BaseModel):
    name = CharField(null=True,max_length=100)
    price = DecimalField(null=True,max_digits=10,decimal_places=2)
    cost = DecimalField(null=True,max_digits=10,decimal_places=2)
    is_active = BooleanField(default=True)

    class Meta:
        db_table = 'dishes'

    def dump(self):
        return {
            'id':self.id,
            'name': self.name,
            'price': self.price,
            'cost': self.cost,
            'is_active': self.is_active
        }