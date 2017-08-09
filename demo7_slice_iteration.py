# -*- coding:utf-8 -*-

#切片

l = ['Michael','Sarah','Tracy','Bob','Jack']

# 切片 Slice
print(l)
print(l[0:3])
#开始为零可省略
print(l[:4])
print(l[-2:-1])

li = list(range(100))

print(li[:10])

print(li[-10:])

print(li[10:20])

print('hello world')

print(li[::5])

print(li[::2])

print(li[:])

# 对tuple进行切片，结果也还是tuple
t = (1,2,3,4)
t1 = t[::2]
print(t1)

#字符串也可以看作是一种list



#迭代

#通过for 。。。in。。。进行迭代

#所有可迭代数据都可通过for。。。in。。。进行迭代
# list
l = list(range(10))
for i in l:
    print(i)

#dict   迭代
dict = {'name':'hash','age':18,'hobby':'lolita'}

for key in dict:
    print(key,':',dict.get(key))

for val in dict.values():
    print(val)

for k,v in dict.items():
    print(k,':',v)

#字符串迭代
str = '我爱你北国的雪'

for s in str:
    print(s)

# 判断是否可迭代

from collections import Iterable

print(isinstance('abc',Iterable))

print(isinstance([1,2,3],Iterable))

print(isinstance((1,2,3),Iterable))

print(isinstance(12345,Iterable))

#迭代多维数组

for x,y in [(1,2),(3,4),(5,6)]:
    print('(',x,',',y,')')

#把list变成 索引-元素对 的可迭代对象

for i,val in enumerate(list(range(10))[::2]):
    print(i,':',val)







