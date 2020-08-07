from model1 import Model, IntegerField, StringField

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(u.name)
u.name = 10 # 无法验证属性
print(u)
# 保存到数据库：
# u.save()