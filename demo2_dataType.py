#-*- coding : utf-8 -*-
#python基础
a = 100
if a>100:
    print(a)
else:
    print(-a)

#python可以处理任意大小的整数，包括负数

#浮点数，--以科学记数法表示时，小数位置可变

#字符串，以单引号或者双引号引起来的任意文本
#\转义字符
print("\"")
#r''标识内部字符默认不转义
print(r"\\\\\t\\t\t\n")
#'''...'''表示多行
print('''hello1
hello2
hello3''')

#布尔值 true false
#注意需要大写
print(True and False)
print(True or False)
print(not True)

#用none表示空值
print(None)

#变量
#这个太简单不做练习
a = 'XYZ'
b = a
a = 'ABC'
print('a:',a)
print('b:',b)

#常量 通常用大写的变量名表示常量
#习惯用法，因为python不会保证常量不会被改变

PI = 3.14159265358

#除法
print(10/3)
print(10//3)
print(10%3)

#字符串和编码

print('中')
print(ord('爱'))
print(chr(29233))
print('ABC'.encode('ascii'))
print('我爱你'.encode('utf-8'))


#字符工具
print(len('我爱你'))
print(len('abcdefg'))
print(len('我爱你'.encode('utf-8')))

#第一行是告诉系统，这是一个Python可执行程序。windows会省略
#!/usr/bin/env python3
#按照utf-8格式读取源码，否则会有乱码问题
# -*- coding: utf-8 -*-


#格式化输出
print('Hello,%s' % 'world')
print('hello,%d'%250)
print('hello,%s,%d' % ('lolikong',748))
# %d 整数 %f 浮点数 %s 字符串 %x 十六位进制

print('%2d-%02d'%(10,1))
print('%.2f'%(3.14159))

print('%%%%name: %s,age: %s,gender: %s,married: %s'%('hash',18,'女',False))
