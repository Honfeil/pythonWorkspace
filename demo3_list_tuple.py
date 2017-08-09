# -*- coding:utf-8 -*-

#list 和 tuple

classMates = ['Michael','Bob','Tracy','Ali']
print(classMates[0])
print(len(classMates))
print(classMates[-1])

#添加元素
#   在末尾添加
classMates.append('Lovely')
classMates.append('Canndy')
print(classMates)
#   在指定位置添加
classMates.insert(1,'hash')
classMates.insert(-1,'Honfeil')
print(classMates[-1])

#删除元素
#   删除末尾元素并将其返回
print(classMates)
print(classMates.pop())
print(classMates)
#   删除指定位置元素并将其返回
print(classMates)
print(classMates.pop(1))
print(classMates)

#赋值运算
classMates[1] = 'Hash'
print(classMates)

#多维数组
arr=[[1,2,3],[4,'center',6],[7,8,9]]
print(arr[1][1])

#tuple 元组
#tuple 是不可变的，元组的数据在定义之后就需要被确定
#tuple 更安全，推荐使用tuple
t = (1,2,3)
print(t)
t = (2,3,4)
print(t)
print(t[0])
t1 = (1,)
print(t1)











#
