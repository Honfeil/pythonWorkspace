# -*- coding:utf-8 -*-

# 高阶函数

# 变量可以指向函数,指向函数的变量可以直接调用函数

print(abs(-10))

a = abs

print(a)
print(a(-10))

# 函数名也是变量

abs = 10
print(abs)

print(a(-10))

abs = a


# 如果要恢复abs函数，请重启Python交互环境

# 传入函数：将函数作为参数传入函数中

def add(x, y, f):
    return f(x) + f(y)


print(add(10, -10, abs))



#
