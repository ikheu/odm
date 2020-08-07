import model3 as model


class LineItem(model.Model):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def subtotal(self):
        return self.price * self.weight

if __name__ == '__main__':
    item = LineItem(description='apple', weight=1.4, price=2)
    print(item.description)
    item.description = "ee"
    print(LineItem.description)
    # item.description = 10
    # print(item.subtotal())
    # print(LineItem.price.storage_name)
    # print(item.__class__)
    # print(LineItem.__class__)
    # print(LineItem.__mro__)
