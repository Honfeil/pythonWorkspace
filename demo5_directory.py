# -*- coding:utf-8 -*-

#dict 字典 （directory） 即 Map 存储键值对

d = {'name':'Honfeil','age':18,'hobby':'loli'}
print(d)
d['gender'] = '女'
print(d)

#判断属性存在
print('gender' in d)
print(d.get('tomas',-1))
print(d.pop('hobby'))
print(d)

#和list比较
#   1、查找和插入的速度极快，不会随着key的增加而增加
#   2、需要占用大量的内存，内存浪费多

#set 键的集合，不能重复

s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.add('hello')
print(s)
s.remove('hello')
print(s)


#排序
arr = ['a','d','c']
arr.sort()
print(arr)
str = 'fvck world'
str.replace('v','u')
print(str.replace('v','u'))
print(str)













#
