#-*- coding:utf-8 -*-

#python函数

#调用函数

#   abs 求绝对值

print(abs(-20))

#   max() 求最大值
#   min() 求最小值

print(max(1,5,7,9))
print(min(1,5,7,9))

#数据类型转换

print(int('22'))
print(str(100))
print(bool(''))
print(bool('  '))
print(bool(0))
print(bool(1001))

#函数赋值

a = abs
print(a(-50))


#函数定义

def myAbs(x):
    if x>0:
        return x
    else:
        return -x

print(myAbs(-10))


#定义幂指数函数
def mi(x,y=2):
    z = 1
    if y==0:
        return 1
    else:
        for i in list(range(abs(y))):
            z*=x
        if y<0:
            return 1/z
        else:
            return z

print(mi(10,-3))
print(1/10)
print(list(range(abs(10))))
print(mi(10,-1))

#可变参数

def clac(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(clac(1,2,3,4,5,6))

#数组变为可变参数
li = list(range(10))

print(clac(*li))

#关键字参数
def person(name,age,**ex):
    print('name:',name,'age:',age,'other:',ex)

person('honfeil',18)
person('hash',22,job='coder',city='杭州')

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*
#*后面的参数被视为命名关键字参数。

'''
看的不是很懂，但是实在是太难受了，所以决定先跳过去
'''

#   递归

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(10))

#注意尾递归优化

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

















#
