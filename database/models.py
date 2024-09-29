from peewee import Model, SqliteDatabase, IntegerField, TextField, DateTimeField
import datetime

db = SqliteDatabase('bot_database.db')

class User(Model):
    user_id = IntegerField(unique=True)
    username = TextField(null=True)

    class Meta:
        database = db


class UserRequest(Model):
    user_id = IntegerField()
    query = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def create_tables():
    if db.is_closed():  # Проверяем, закрыто ли текущее соединение
        db.connect()
    db.create_tables([User, UserRequest], safe=True)  # Создаем таблицы, если их еще нет.