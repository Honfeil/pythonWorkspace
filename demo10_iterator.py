# -*- coding:utf-8 -*-

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable, Iterator
from datetime import date

print('***[]***')

print(isinstance([], Iterable))

print(isinstance([], Iterator))

print('***{}***')

print(isinstance({}, Iterable))

print(isinstance({}, Iterator))

print('***()***')

print(isinstance((), Iterable))

print(isinstance((), Iterator))

print('***"***')

print(isinstance('', Iterable))

print(isinstance('', Iterator))

print('***range()***')

print(isinstance(range(10), Iterable))

print(isinstance(range(10), Iterator))

print('***[for..in..]***')

print(isinstance([x * x for x in range(10)], Iterable))

print('***(for..in.)***')

print(isinstance((x * x for x in range(10)), Iterable))

print('***str***')

print(isinstance(str, Iterable))

print(isinstance('', str))

print(isinstance(123, int))

print(isinstance(0.12, float))

print(isinstance('1995-09-27', date))

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，
# 却不是Iterator。
#
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
li = iter([1,2,3,4])
print(next(li))
print(next(li))
print(next(li))
print(next(li))


# Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
# 而使用list是永远不可能存储全体自然数的。

