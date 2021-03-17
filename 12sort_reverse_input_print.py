from random import shuffle
data=list(range(20))
shuffle(data)#随机打乱顺序
print(data)
print(sorted(data))
print(sorted(data,key=str))
print(sorted(data,key=str,reverse=True))


data=list(range(20))
shuffle(data)
print(data)
reverseData=reversed(data)#生成reverse对象
print(reverseData)
print(list(reverseData))#根据reversed对象得到列表
print(tuple(reverseData))#空元组，reversed对象中元素只能用一次


num=int(input('请输入一个大于2的自然数：'))
if num%2==1:
    print('jishu')
else:
    print('oushu')
lst=eval(input('请输入一个包含若干大于2的自然数的列表：'))
print('列表中所有元素之和为：',sum(lst))


