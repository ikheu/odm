from field import BaseField
from pymongo import IndexModel


class Collection():
    ops = ['drop', 'create_indexes', 'insert', 'find']

    @classmethod
    def ensure_unique(cls):
        indexes = []
        for item in cls.__unique_index__:
            indexes.append(IndexModel(item, unique=True, background=True))
        res = cls.create_indexes(indexes)
        return res

    def commit(self):
        data = self.dump()
        self.__class__.insert(data)


class MetaModel(type):
    def __new__(cls, name, bases, attr_dict):
        if name != 'Model':
            attr_dict['__fieldkeys__'] = []
            attr_dict['__unique_index__'] = []
            for key, attr in attr_dict.items():
                if isinstance(attr, BaseField):
                    attr_dict['__fieldkeys__'].append(key)
                    type_name = type(attr).__name__
                    attr.real_attr = '_{}#{}'.format(type_name, key)
                    if attr.unique:
                        attr_dict['__unique_index__'].append(key)
            if '__tb__' not in attr_dict:
                attr_dict["__tb__"] = None
        bases = (*bases, Collection)
        return super().__new__(cls, name, bases, attr_dict)

    def __getattr__(cls, key):
        if key in cls.ops:
            attr = getattr(cls.__tb__, key, None)
            if attr:
                return attr
        raise AttributeError("%s object has no attribute '%s'" % (cls.__name__, key))

class Model(metaclass=MetaModel):
    def __init__(self, **kwargs):
        self.handle_keys(kwargs)

    def handle_keys(self, kwargs):
        data = {}
        for k in self.__fieldkeys__:
            field = getattr(self.__class__, k)
            if k in kwargs:
                data[k] = kwargs[k]
            else:
                if field.require:
                    raise ValueError("'%s' field is required" % k)
                else:
                    data[k] = field.default
        for k, v in data.items():
            setattr(self, k, v)
    
    def __repr__(self):
        data = self.dump()
        return "%s: %s" % (type(self).__name__, data)

    def dump(self):
        data = {}
        for key in self.__fieldkeys__:
            data[key] = getattr(self, key)
        return data

    @classmethod
    def load(cls, dict_data):
        return cls(**dict_data)
