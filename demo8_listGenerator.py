# -*- coding:utf-8 -*-

# 列表生成器 List Comprehensions 用来创建list的生成式

# 生成1-10
print(list(range(1, 11)))

# 生成n*n
l = []
for x in range(1, 11):
    l.append(x * x)

print(l)

# 简便方法

li = list(x * x for x in range(1, 11))
print(li)

lili = list(x * x for x in range(1, 11) if x % 3 == 0)

print(lili)

# 双重循环

lilili = list(m + n for m in "ABC" for n in "DEF")

print(lilili)

# 列出文件名

import os

dic = list(d for d in os.listdir('D:\\'))

print(dic)

#
dict = {'name': 'honfeil', 'age': '18', 'gender': 'nv'}

for k,v in dict.items():
    print(k,'=',v)

liDict = list(k+'='+v for k,v in dict.items())

print(liDict)

liChar = ['X','Y','Z','S','W','P',"k"]

print(liChar)

liChar = list(s.lower() for s in liChar)

print(liChar)

liTest = [1,2,3,'X','Y','Z','s','Q']

print(liTest)
# 正解
liTest = list(x.lower() if isinstance(x,str) else x for x in liTest)

print(liTest)




