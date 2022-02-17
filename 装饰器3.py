

def outer(orange):
    def inner(*args,**kwargs):
        print("befor")
        res = orange(*args,**kwargs)
        print("after")
        return res

    return inner


@outer #func = outer(func)
def func1(a):
    print("我是func1函数")
    values = (11, 22, 33, 44)
    return values


def func2():
    print("我是func2函数")
    values = (11, 22, 33, 44)
    return values



def func3():
    print("我是func3函数")
    values = (11, 22, 33, 44)
    return values

def func4():
    print("我是func4函数")
    values = (11, 22, 33, 44)
    return values

func1(1)
