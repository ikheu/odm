import field as field
from model import Model
from pymongo import MongoClient
from factory import make_client

client = make_client(MongoClient, 'test')

class User(Model):
    __tb__ = client['user']
    name = field.StrField()
    age = field.IntField()


if __name__ == '__main__':
    u = User(name='Bob', age=10)
    print(u)
    print(u.dump())
    print(User.load({'name': 'Tom', 'age': 20}))
    u.commit()
    print(User.find_one())
