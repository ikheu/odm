class Base:
    def bar(self):
        raise NotImplemented('--')


class Foo(Base):
    class Meta:
        def bar(self):
            print('----')

foo = Foo()

print(Foo)
print(dir(Foo))
print(dir(foo))
foo.bar()
