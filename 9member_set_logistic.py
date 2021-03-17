print(60 in [70,60,50])
print('abc' in 'a1b2c3d4f')
print([3] in [[3],[4],[5]])
print('3' in map(str,range(5)))
print(5 in range (5))

A={35,45,55,65,75}
B={65,75,85,95}
print(A|B)#交集
print(A&B)#并集
print(A-B)
print(B-A)
print(A^B)#对称差集

print(3 in range(5) and 'abc' in 'abcdefg')
print(3-3 or 5-2)
print(not 5)
print(not [])