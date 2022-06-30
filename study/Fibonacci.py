# 斐波那契数列
# 1、1、2、3、5、8、13、21、34
# F1=1,n=1
# F2=1,n=2
# Fn=F[n-1]+F[n-2],n

# 1
def fibo1(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fibo1(4))


# 2
def fibo2(n):
    if (n == 1) or (n == 2):
        return 1
    return fibo2(n - 1) + fibo2(n - 2)


print(fibo2(4))


# 3
def fibo3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(fibo3(4))
