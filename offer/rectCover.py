#矩阵覆盖
#我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#思路：n=1 f(n)=1;n=2 f(n)=2
#假设到了n，那么上一步就有两种情况，在n-1的时候，竖放一个矩形，或者是n-2时候，横放两个矩形（这里不能竖放两个矩形，因为放一个就变成了n-1，那种情况就重复了）
#所以总数是f(n)=f(n-1)+f(n-2).和跳台阶一样

class Solution:
    def rectCover(self, number):
        if number<=0:return 0
        if number==1:return 1
        if number==2:return 2
        result = [1,2]
        for i  in range(2,number):
            result.append(result[-1]+result[-2])
            
        return result[-1]