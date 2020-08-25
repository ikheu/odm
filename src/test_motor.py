import field as field
from model import Model
from motor.motor_asyncio import AsyncIOMotorClient
from collection import MotorCollection
import asyncio


db = AsyncIOMotorClient().test
instance = MotorCollection(db)


@instance.register('user')
class User(Model):
    _id = field.IntField()
    name = field.StrField(unique=True)
    age = field.IntField(require=False, default=None)
    country = field.StrField(require=False, default="China")

if __name__ == '__main__':
    async def test():
        return await User.find({}).to_list(None)
    res = asyncio.get_event_loop().run_until_complete(test())
    print(res)
