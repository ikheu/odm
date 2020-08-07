import abc
# from exceptions import 

class Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.real_attr)

    def __set__(self, instance, value):
        setattr(instance, self.real_attr, value)


class BaseField(abc.ABC, Descriptor):
    valid_attrs = {'validate', 'required', 'default', 'fkey'}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.valid_attrs:
                pass # 斟酌一下怎么处理
        
    def __set__(self, instance, value):
        value = self.validate(value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, value):
        """return validated value or raise ValueError"""


class TypeField(BaseField):
    def validate(self, value):
        if isinstance(value, self.allow_type):
            return value
        else:
            raise ValueError(" ")


class StrField(TypeField):
    allow_type = str
    

class IntField(TypeField):
    allow_type = int


class DictField(TypeField):
    allow_type = dict


class ListField(TypeField):
    allow_type = list


class BoolField(TypeError):
    allow_type = bool


class DateField(BaseField):
    def validate(self, value):
        return value
