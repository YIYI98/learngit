data=[3,22,111]
print(data)
print(max(data))
print(min(data))
print(max(data,key=str))#转化为字符串后最大的元素
data=['3','22','111']
print(max(data))
print(max(data,key=len))
data=['abc','Abcd','ab']
print(max(data))
print(max(data,key=len))
print(max(data,key=str.lower))#转换为小写之后最大的字符串
print(max(set(data),key=data.count))#出现次数最多set
print(max(range(len(data)),key=data.__getitem__))#最大元素的位置



data=[1,2,3,4]
print(len(data))
print(sum(data))
data=(1,2,3)
print(len(data))
print(sum(data))
data={1,2,3}
print(len(data))
print(sum(data))
data='Readability counts.'
print(len(data))
data={97:'a',100:'b',66:'0'}
print(len(data))
print(sum(data))

