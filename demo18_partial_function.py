# -*- coding:utf-8 -*-

# python的functools提供了许多有用的功能，其中一个就是偏函数
# 偏函数（partial function）
# 和数学意义上的偏函数不同

# 通过设定函数的默认值，可以降低函数调用的难度，偏函数也可以实现这一点
import functools

print(int('123456'))

# int 还提供额外的base参数，实现进制转换
# 转换注意
print(int('123456', base=8))
print(int('123456', 8))
print(int('123456', base=16))
print(int('111111', 2))


# int 接受参数为string

# 定义一个将字符转换为二进制数据的函数
def int2(x, base=2):
    return int(x, base)


print(int2('1010101'))


# functools.partial 就是用于帮助创建偏函数，不需要再次定义函数，就可以直接创建


int3 = functools.partial(int,base=2)

print(int3('101111'))


# 总结：functools.partial的作用就是，把一个函数的某些参数给固定住（即设置默认值），并返回一个新函数

# 注意：被固定的参数也可在新函数中再次被赋值

print(int3('123456',base=8))



