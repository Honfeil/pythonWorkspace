# -*- coding:utf-8 -*-

# 高阶函数除了可以接收函数作为参数之外，还可以吧函数作为结果值返回

# 一般求和

def calc_aum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


# 返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

print(lazy_sum(1,2,3))

print(lazy_sum(1,2,3,4,5,6)())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1 = lazy_sum(1,2,3)
f2 = lazy_sum(1,2,3)

print(f1,f2,'f1 = f2',f1==f2)

# f1()和f2()的调用结果互不影响

# 返回闭包时牢记的一点就是：
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

li = count()

print(len(li))

print(li[0]())
print(li[1]())
print(li[2]())

#可以赋值给三个变量

def lis():
    fs = []
    for i in range(1,4):
        fs.append(i*i)
    return fs

li1,li2,li3=lis()

print(li1,li2,li3)


# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))#f(i)立刻被执行，因此i的值被传入后定住
    return fs

l1,l2,l3 = count()

print(l1())
print(l2())
print(l3())









    #
