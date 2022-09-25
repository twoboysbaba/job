#2.替换空格
#请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

def replaceSpace(replacestr):
    result = ''
    for i in range(0,len(replacestr)):
        if(replacestr[i]==' '):
            result = result + '%20'
        else:
            result = result + replacestr[i]
    return result
str = "We Are Happy."
str_re = replaceSpace(str)

print(str_re)