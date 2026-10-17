from peewee import ForeignKeyField, CharField, DecimalField, IntegerField

from .dish import Dish
from .order import Order

from .base import BaseModel

class OrderItem(BaseModel):
    order = ForeignKeyField(Order)
    dish = ForeignKeyField(Dish)
    dish_name = CharField(max_length=100)
    price = DecimalField(null=True,max_digits=10,decimal_places=2)
    quantity = IntegerField(null=True,default=1)
    sub_total = DecimalField(null=True,max_digits=10,decimal_places=2)
    class Meta:
        db_table = 'order_items'

    def dump(self):
        return {
            'id': self.id,
            'order_id': self.order.id,
            'dish_id': self.dish.id,
            'dish_name': self.dish.name,
            'price': self.price,
            'quantity': self.quantity,
            'sub_total': self.sub_total

        }