from peewee import MySQLDatabase
from config import DB_CONFIG


db = MySQLDatabase(None)


def init_db():
    db.init(**DB_CONFIG)


# def create_tables(models):
#     init_db()
#     db.connect(reuse_if_open=True)
#     db.create_tables(models, safe=True)
#     db.close()
