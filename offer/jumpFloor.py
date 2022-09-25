#跳台阶
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
#典型的动态规划问题，对于第n阶台阶来说，有两种办法，一种是爬一个台阶，到第n-1阶；第二种是爬两个台阶，到第n-2阶。

class solution:
    def __init__(self) -> None:
        pass
    def jumpFloor(self, n):
        if (n<=0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 2
        result = [1,2]
        for i in range(2,n):
            result.append(result[i-1]+result[i-2])
        return result[-1]
    
so = solution()
res = so.jumpFloor(5)
print(res)