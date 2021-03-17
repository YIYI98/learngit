# from math import pi as PI
# from os.path import getsize
# from random import choice
# r=3
# print(round(PI*r*r,2)) #round() 方法返回浮点数x的四舍五入值
# # print(getsize(r''))#计算文件大小
# print(choice('Python')) #从字符串中随机选择一个字符


from itertools import *
characters='1234'
for item in combinations(characters,3):#从4个字符中任选3个的组合
    print(item,end=' ')
print('\n'+ '='* 20)#换行后输出20个=号
for item in permutations(characters,3):#从4个字符中任选3个的排列
    print(item,end=' ')