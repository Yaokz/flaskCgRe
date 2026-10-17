# 验证 peewee 查询对象的 bool 行为：空结果集是 True 还是 False？
from peewee import SqliteDatabase, Model, AutoField, CharField

db = SqliteDatabase(':memory:')

class BaseModel(Model):
    class Meta:
        database = db

class P(BaseModel):
    name = CharField()

db.create_tables([P])

q = P.select().where(P.name == '不存在的名字')   # 此刻表是空的
print('空表时 bool(query) =', bool(q))

P.create(name='不存在的名字')                    # 插入一条匹配的
q2 = P.select().where(P.name == '不存在的名字')
print('有数据时 bool(query) =', bool(q2))

print('Select 类是否定义 __bool__:', hasattr(type(q), '__bool__'))
print('Select 类是否定义 __len__ :', hasattr(type(q), '__len__'))

import peewee
print('peewee 版本:', peewee.__version__)
