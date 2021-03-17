print(dir(__builtins__))#查看所有的内置函数和内置对象
print(int(3.5))
print(int('119'))
print(int('1111',2))
print(int('1111',8))
print(int('1111',16))
print(int('  9\n'))
print(float('3.1415926'))
print(float('-inf'))
print(complex(3,4))
print(complex(6j))
print(complex('3'))

print(bin(8888))#把整数转化为二进制数
print(oct(8888))#八
print(hex(8888))#十六


print(ord('a'))#返回字符的ASCII码
print(ord('董'))#返回汉字字符的Unicode编码
print(chr(65))#返回ASCII码对应的字符
print(chr(33891))#返回指定Unicode编码对应的汉字
print(str([1,2,3,4]))#把列表转换为字符串
print(str({1,2,3,4}))#把集合转换为字符串

print(list(),tuple(),dict(),set())
s={3,2,1,4}
print(list(s),tuple(s))
lst=[1,1,2,2,3,4]
print(tuple(lst),set(lst))
print(list(str(lst)))
print(dict(name='Dong',sex='Male',age=41))

#eval用来计算字符串或字节串的值，也可以用来实现类型转换的功能
print(eval('3+4j'))
print(eval('8**2'))
print(eval('[1,2,3,4,5]'))
print(eval('{1,2,3,4}'))