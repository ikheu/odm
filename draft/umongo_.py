from datetime import datetime
from pymongo import MongoClient
from umongo import Instance, Document, fields, validate

db = MongoClient().test
instance = Instance(db)

@instance.register
class User(Document):
    email = fields.EmailField(required=True, unique=True)
    birthday = fields.DateTimeField(validate=validate.Range(min=datetime(1900, 1, 1)))
    friends = fields.ListField(fields.ReferenceField("User"))

    class Meta:
        collection_name = "user1"

print(dir(User))
print(User.email)
# Make sure that unique indexes are created
print(db.user1.remove())
User.ensure_indexes()

goku = User(email='goku@sayen.com', birthday=datetime(1984, 11, 20))
goku.commit()
vegeta = User(email='vegeta@over9000.com', friends=[goku])
vegeta.commit()

print(vegeta.friends)
# <object umongo.data_objects.List([<object umongo.dal.pymongo.PyMongoReference(document=User, pk=ObjectId('5717568613adf27be6363f78'))>])>
vegeta.dump()
# {id': '570ddb311d41c89cabceeddc', 'email': 'vegeta@over9000.com', friends': ['570ddb2a1d41c89cabceeddb']}
User.find_one({"email": 'goku@sayen.com'})
# <object Document __main__.User({'id': ObjectId('570ddb2a1d41c89cabceeddb'), 'friends': <object umongo.data_objects.List([])>,
#                                 'email': 'goku@sayen.com', 'birthday': datetime.datetime(1984, 11, 20, 0, 0)})>

print(list(db.user1.find()))
