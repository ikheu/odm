from field import BaseField


class MetaModel(type):
    def __new__(cls, name, bases, attr_dict):
        attr_dict['__fieldkeys__'] = []
        for key, attr in attr_dict.items():
            if isinstance(attr, BaseField):
                attr_dict['__fieldkeys__'].append(key)
                type_name = type(attr).__name__
                attr.real_attr = '_{}#{}'.format(type_name, key)
        collection = attr_dict.get('__tb__', None)
        attr_dict['__tb__'] = collection
        return super().__new__(cls, name, bases, attr_dict)


    def __getattr__(cls, key):
        attr = getattr(cls.__tb__, key, None)
        if attr:
            return attr
        else:
            raise AttributeError()


class Model(metaclass=MetaModel):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__fieldkeys__:
                setattr(self, k, v)

    def __repr__(self):
        data = self.dump()
        return "%s: %s" % (type(self).__name__, data)

    def dump(self):
        data = {}
        for key in self.__fieldkeys__:
            data[key] = getattr(self, key)
        return data

    def commit(self):
        data = self.dump()
        self.__class__.insert(data)

    @classmethod
    def load(cls, dict_data):
        return cls(**dict_data)
