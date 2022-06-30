# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self, number: int) -> int:
        # write code here
        # n=1, 1种
        # n=2, 2种
        # n=3, 3种
        # n=4, 5种
        # n=5, 8种
        if number == 1:
            return 1
        if number == 2:
            return 2
        a, b = 1, 2
        for i in range(number - 2):
            a, b = b, a + b
        return b

        # n=3 a=2,b=3
        # n=4 a=3,b=5
