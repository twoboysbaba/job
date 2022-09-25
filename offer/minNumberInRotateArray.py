#输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1

class solution:
    def __init__(self):
        pass
    def minNumberInRotateArray(self, rotatearray):
        if not rotatearray:
            return 0
        for i in range(0,len(rotatearray)):
            if(rotatearray[i+1]<rotatearray[i]):
                return rotatearray[i+1]
            
        return rotatearray[0]
    
rotatearray = [3,4,5,1,2]
so = solution()
res = so.minNumberInRotateArray(rotatearray)
print(res)