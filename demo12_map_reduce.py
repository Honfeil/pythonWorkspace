# -*- coding:utf-8 -*-

# python 内建了map()和reduce()函数

# map()
# map接受两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并将结果作为新的Iterator返回

# x平方
from functools import reduce


def f(x):
    return x * x


r = map(f, range(10))

print(next(r))
print(next(r))
print(next(r))
print(next(r))

print(list(r))

# 转字符串
l = list(map(str, range(10)))
print(l)

l = list(map(int, l))
print(l)


# reduce接受两个参数，一个函数，一个参数
# 函数处理两个参数

# 将list转为一个整数
def s(x1, x2):
    return x1 * 10 + x2


l = reduce(s, [1, 3, 5, 7, 9])
print(l)
print(sum(list(range(10000))))


# 将str转为int
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}[s]

# lambda缩减函数为一行输出
print(reduce(lambda x1, x2: x1 * 10 + x2, map(char2num, '135')))

#练习
# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

print(list(map(lambda s:s.capitalize(),['adam', 'LISA', 'barT'])))

print(list(map(lambda s:s[0].upper()+s[1:].lower(),['adam', 'LISA', 'barT'])))



#