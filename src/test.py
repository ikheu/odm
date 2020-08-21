import field as field
from model import Model
from pymongo import MongoClient
from factory import make_client

client = make_client(MongoClient, 'test')


class User(Model):
    __tb__ = client['user']
    _id = field.IntField()
    name = field.StrField(unique=True)
    age = field.IntField(require=False, default=None)
    country = field.StrField(require=False, default="China")


if __name__ == '__main__':
    User.drop()
    User.create_index("name", unique=True)
    User.ensure_unique()
    u1 = User(name='Bob', age=11, _id=10)
    u2 = User(name="Bob1", age=12, _id=11)
    u1.commit()
    u2.commit()
    print(list(User.find()))
