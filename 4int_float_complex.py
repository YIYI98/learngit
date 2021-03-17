import math
print(math.factorial(32))#计算32的阶乘
print(0.4-0.3==0.1)
print(math.isclose(0.4-0.3,0.1))#测试两个浮点数是够足够接近
num=7
squreRoot=num**0.5 #计算平方根
print(squreRoot**2==num)
print(math.isclose(squreRoot**2,num))
c=3+4j
print(c+c)
print(c**2)
print(c.real)
print(c.imag)
print(3+4j.imag)
print(c.conjugate())#查看共轭复数
print(abs(c))#计算复数的模
