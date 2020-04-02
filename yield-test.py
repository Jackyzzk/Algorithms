def fun_inner():
    i = 0
    while True:
        i = yield i
        # print(i)

def fun_outer():
    a = 0
    b = 1
    inner = fun_inner()
    aux = inner.send(None)
    while True:
        a = inner.send(b)
        b = yield a

if __name__ == '__main__':
    outer = fun_outer()
    aux2 = outer.send(None)
    for i in range(5):
        print(outer.send(i))