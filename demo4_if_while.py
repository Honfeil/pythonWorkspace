# -*- coding:utf-8 -*-

#条件判断

age = 14

if age>14:
    print('合法萝莉')
else:
    print('三年血赚，死刑不亏')

age = 18

if age>14:
    print('just funny')
elif age>18:
    print('just for married')
elif age>22:
    print('wtf')
else:
    print('wonderful journey')

#循环控制
arr = ['Michael','Hash','Honfeil','Honey','Sweety']
for str in arr:
    print(str)

print(list(range(10)))

li = list(range(101))
sum = 0
for i in li:
    sum+=i
print(sum)

sum = 0
n=99
while n>0:
    sum+=n
    n-=2
print(sum)

#break
n = 100
while n>0:
    if n==55:
        break
    else:
        print(n)
        n-=1

#countinue
n = 100
while n>0:
    n-=1
    if n%2==0:
        print(n)
    else:
        continue


for i in list(range(10)):
    str = ''
    for j in list(range(i+1)):
        if i*j >0:
            str += ('%s x %s = %s \t' % (j,i,i*j))
    print(str+'\n')













#
