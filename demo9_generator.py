# -*- coding:utf-8 -*-


# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
# 列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，
# 这种一边循环一边计算的机制，称为生成器：generator。


#将列表生成器的[] 改为 （）就可以了

g = (x*x for x in range(10))

#通过next获取返回值

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

l = g

#正常使用for来迭代生成器

for i in (x*x for x in range(10)):
    print(i)


#斐波拉契数列
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# #那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b = b,a+b
        n+=1
    print('done')

print(fib)

def fia(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
    print('done')

a = fia(10)

print(a)

# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


#作业 杨辉三角

def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


#数组可以直接相加

c = [1]
d = [2]
print(c+d)






















