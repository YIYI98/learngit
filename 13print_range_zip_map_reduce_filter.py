print(1,2,3,4,5)
print(1,2,3,4,5,sep=',')
print(1,2,3,4,5,end=' ')
print(3,4,5)

range1=range(4)
range2=range(5,8)
range3=range(3,20,4)
range4=range(20,0,-3)
print(range1,range2,range3,range4)
print(range4[2])
print(list(range1),list(range2),list(range3),list(range4))
for i in range (10):
    print(i,end=' ')



data=zip('abcd',[1,2,3,4,5,6])
print(data)
print(list(data))
data=zip('abcd',[1,2,3,4,5,6])
print(tuple(data))
data=zip('abcd',[1,2,3,4,5,6])
for item in data:
    print(item)
'''
map()函数把一个可调用对象func依次映射到序列的每个元素上，并返回一个可迭代的map对象，
其中每个元素是原序列中元素经过可调用对象func处理后的结果，该函数不对原序列做任何修改。
该函数返回的map对象可以转换为列表、元组或集合，也可以直接使用for循环遍历其中的元素，但是map对象中的每个元素只能使用一次。示例如下。
'''
from operator import add
print(map(str,range(5)))
print(list(map(str,range(5))))
print(list(map(len,['abc','1234','test'])))
for num in map(add,range(5),range(5,10)):
    print(num)


'''函数reduce()可以将一个接收2个参数的函数以迭代的方式从左到右依次作用到一个序列或可迭代对象的所有元素上，并且每一次计算的中间结果直接参与下一次计算，最终得到一个值。
例如，继续使用operator标准库中的add运算，那么表达式reduce(add,[1,2,3,4,5])计算过程为((((1+2)+3)+4)+5)。'''
from functools import reduce
from operator import add, mul,or_
seq=range(1,10)
print(reduce(add,seq))
print(reduce(mul,seq))
seq=[{1},{2},{3},{4}]
print(reduce(or_,seq))#对seq中的集合连续进行并集

seq=['abcd','1234','.,?!',' ']
print(list(filter(str.isdigit,seq)))#只保留数字字符串
print(list(filter(str.isalpha,seq)))#只保留英文字母字符串
print(list(filter(str.isalnum,seq)))#只保留数字字符串和英文字符串
print(list(filter(None,seq)))#只保留等价于True的元素