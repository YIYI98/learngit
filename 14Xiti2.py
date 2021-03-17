# lst=eval(input('请输入一个包含若干自然数的列表：'))
# print(sum(lst)/len(lst))
# avg=round(avg,3)
#
# from random import shuffle
# lst=eval(input('请输入一个包含若干自然数的列表：'))
# shuffle(lst)
# print(sorted(lst,key=int,reverse=True))
# reverseData=reversed(lst)
# print(reverseData)
# print(list(reverseData))


# lst=eval(input('请输入一个包含若干自然数的列表：'))
# strLst=list(map(str,lst))
# print(list(map(len,strLst)))
# for num in map(len,strLst):
#     print(num)


# lst=eval(input('请输入一个包含若干自然数的列表：'))
# print(max(lst,key=abs))
# from functools import reduce
# from operator import mul
# lst=eval(input('请输入一个包含若干自然数的列表：'))
# print(reduce(mul,lst))



# lst1=eval(input('请输入一个包含若干自然数的列表1：'))
# lst2=eval(input('请输入一个包含若干自然数的列表2：'))
# length1=len(lst1)
# lst3=[]
# lst3.len=length1
# for num in range(length1):
#     lst3[num]=lst1[num]*lst2[num]
# print(lst3)
from operator import mul
lst1=eval(input('请输入一个包含若干自然数的列表1：'))
lst2=eval(input('请输入一个包含若干自然数的列表2：'))
print(sum(map(mul,lst1,lst2)))