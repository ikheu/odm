import model2 as model


class LineItem(model.Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    # def __init__(self, description, weight, price):
    #     self.description = description
    #     self.weight = weight
    #     self.price = price

    def subtotal(self):
        return self.price * self.weight


class Foo():

    def foo(self):
        pass

if __name__ == '__main__':
    # item = LineItem(description='apple', weight=1.4, price=2)
    # print(item.description)
    # item.description = 10
    # print(LineItem.__dict__)
    print(Foo.__dict__)
    foo = Foo()
    foo.foo()
    # foo.foo = 10
    print(foo.__dict__)
    # foo.foo()

    # print(item.subtotal())
    # print(LineItem.price.storage_name)
    # print(item.__class__)
    # print(LineItem.__class__)
    # print(LineItem.__mro__)
