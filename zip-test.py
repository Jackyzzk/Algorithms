for i in zip((1, 2), (3, 4)):
    print(i)
print('-----')
t = zip((1, 2), (3, 4))
print(t)
print('-----')
print(*t)
print('-----')
p = [1, 2, 3]
q = {1: 2, 3: 4}

# Python中，（*）会把接收到的参数形成一个元组，而（**）则会把接收到的参数存入一个字典
# * 解包？
print(*p)
print(*q)
print(*q)
print('-----')
r = {'ab': 'cd', 'ef': 'gh'}
print(*r)