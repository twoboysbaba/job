#1.二维数组中的查找
#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

def Find(array,target):
    rows = len(array)-1
    cols = len(array[0])-1
    i = 0
    j = cols
    while(i<=rows and j>=0):
         if(array[i][j]<target):
             j -=1
         if(array[i][j]>target):
             i +=1 
         if(array[i][j]==target):
             return True
    return False

array = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
print(Find(array,12))