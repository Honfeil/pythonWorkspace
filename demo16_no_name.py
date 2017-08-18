# -*- coding:utf-8 -*-


li = list(map(lambda x:x*x,range(10)))

print(li)

#相当于

def f(x):
    return x*x

f = lambda x:x*x

print(f(5))

def bulid(x,y):
    return lambda :x*x + y*y

x = bulid(1,2)

print(bulid(3,4)())



