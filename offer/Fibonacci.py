#要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0），n<=39。
#菲波那切数列：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）

class solution:
    def __init__(self) -> None:
        pass
    def Fibonacci(self, n):
        if (n==0):
            return 0
        a = b = 1
        for i in range(2,n):
            a,b = b,a+b
        return b
    
so = solution()
res = so.Fibonacci(4)
print(res)