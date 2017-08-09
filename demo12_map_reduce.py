# -*- coding:utf-8 -*-

# python 内建了map()和reduce()函数

# map()
# map接受两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并将结果作为新的Iterator返回

# x平方

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

#序列求和



