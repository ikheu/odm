import abc

class BaseField(abc.ABC):
    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""


class Quantity(Validated):
    """a number greater than zero"""

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value

class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value

class Model():
    """Businese entity with validated fields"""
    def __init__(self, **kwargs):
        self._data = {}
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, k, v):
        if k!= '_data':
            obj = getattr(self.__class__, k, None)
            if obj and isinstance(obj, Validated):
                v = obj.validate(self, v)
                self._data[k] = v
                return
        super().__setattr__(k, v)

    def __getattribute__(self, k):
        obj = super().__getattribute__(k)
        if obj and isinstance(obj, Validated):
            return self._data[k]
        else:
            return obj
