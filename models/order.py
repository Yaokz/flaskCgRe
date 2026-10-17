from peewee import CharField, ForeignKeyField, IntegerField, DecimalField


from .user import User

from .base import BaseModel
class Order(BaseModel):
    table_no = CharField(null=True,max_length=255)
    user = ForeignKeyField(User)
    status = IntegerField(default=0)
    total_amount = DecimalField(null=True,max_digits=10,decimal_places=2)
    class Meta:
        db_table = 'orders'
    def dump(self):
        return {
            'id':self.id,
            'table_no':self.table_no,
            'user':self.user.dump(),
            'status':self.status,
            'total_amount':self.total_amount,

                }