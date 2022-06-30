# 动态创建类

User = type("User", (object,), dict(name="Goin", age=18))
user = User()
print(user.age)
user.name = "xxx"
print(user.name)
