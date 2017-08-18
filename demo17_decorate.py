# -*- coding:utf=8 -*-

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

def now():
    print('2017-8-10')


f = now

f()

print(f.__name__)


# 如果我们要增强now()函数的功能，比如，在函数调用前后打印日志
# 但又不希望修改now()函数的定义，这种在代码期间动态增加功能的方式
# 称之为“装饰者模式”（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为他是一个decorator，所以接受一个函数作为参数
# 并返回一个函数，所以要借助@，把decorator置于函数的定义处

@log
def now():
    print('2017-08-10')


# 把@log放到now()函数的定义处，相当于执行了语句
# now = log(now)

now()


# 由于log（）是一个decorator，返回一个函数，所以，原来的now（）函数依然存在
# 只是现在同名的now变量指向了新的函数，于是调用now（）将执行新函数
# 即在log函数中返回的wrapper函数

# 如果decorator本身需要转入参数，那就需要写一个返回decorator的高阶函数

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2017-09-27')


now()

# 相当于执行了 now = log（‘execute’）（now）

print(now.__name__)

# 函数也是对象，拥有__name__等属性，但是经过decorator装饰之后，函数的__name__已经改变
# 因此需要把原始函数属性的__name__等属性复制到wrapper中，否则，有些依赖函数签名的代码执行就会出错
# python内置了function.wraps可以实现上述操作

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s():" % (func.__name__))
        return func(*args,**kw)
    return wrapper

@log
def now():
    print("2017-11-11")

now()

print(now.__name__)

# 针对带参数的装饰器

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('exectue')
def now():
    print("hello world")

now()

print(now.__name__)

test = "success" if 1==2 else "false" if 2==3 else "aha"
# 三元& n元
print(test)


def log(text="执行"):
    def de(func):
        @functools.wraps(func)
        def wra(*args,**kw):
            print("%s() %s 之前" % (func.__name__,text))
            temp = func(*args,**kw)
            print("%s() %s 之后" % (func.__name__,text))
            return temp
        return wra
    return de

@log()
def now():
    print("方法一")

now()
print(now.__name__)

@log("execute")
def now():
    print("方法二")

now()
print(now.__name__)
