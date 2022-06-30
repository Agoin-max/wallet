
from collections import namedtuple

# 方式一
User = namedtuple("User", ["name", "age", "id"])

# 方式二
# User = namedtuple("User", "name age id")

# _make(iterable) 接收一个可迭代对象来生产这个类的实例 _fields 包含这个类所有字段名的元组
user = User._make(["Goin", "male", 12])
print(User._fields)
print(user)
print(user.name)


# 实际应用场景 csv文件与sql数据处理
res = map(User._make, [["Goin", 15, 3], ["Mike", 14, 5]])
print(res)

for r in res:
    print(r.name)
