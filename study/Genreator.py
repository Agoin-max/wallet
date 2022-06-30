# 生成器yield与send
# 每次的send()都会运行到yield语句,但赋值不会执行,只会有返回值,相当于return后就退出函数了,所以在返回值之后的赋值就不会执行了

def gene():
    print("ok")
    x = 100
    print(x)
    first = yield 50  # 这里就是send函数的关键,send所传递的值其实就是给=号左边的赋值
    print(first)

    second = yield x
    print(second)

    z = "third"
    third = yield z
    print(third)


inst = gene()
output1 = inst.send(None)
print(output1)
print("----")
output2 = inst.send(30)  # send(30) first被赋值为30然后print
print(output2)
print("----")
output3 = inst.send(None)  # send(None) second被赋值为None然后print
print(output3)
