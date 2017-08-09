# -- coding:utf-8 --

# sorted()

li = sorted([35, 58, 42, 4, 65, 4, 5, 5, 2, 4, 55, 14, 5])

print(li)

li = [-5, 6, -7, 8, -9]

print(sorted(li))

print(sorted(li, key=abs))

# 字符串排序
li = ['Candy', 'Honey', 'atom', 'bust', 'Bug']

print(sorted(li))

print(sorted(li, key=str.lower))

# 复习map

li = list(map(lambda s: s.capitalize(), li))

print(sorted(li, reverse=True))

# 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def sk(m):
    return m[0]


def ss(m):
    return m[1]


print(sorted(L, key=sk))

print(sorted(L, key=ss, reverse=True))
