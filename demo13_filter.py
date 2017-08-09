# -*- coding:utf-8 -*-

# Python内建的filter()函数用于过滤序列。
#
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

l = list(filter(lambda x:x%2==0,range(10)))

print(l)

#用filter求素数

#奇数生成器：无限序列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

#筛选函数
def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n< 100:
        print(n)
    else:
        break


print("hello"[::-1])

#过滤非回数

def fi(s):
    return str(s)==str(s)[::-1]

li = list(filter(fi,range(10,100)))

print(li)
