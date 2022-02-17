"""
需求 在函数执行前输出before 在函数执行后输出after


def func():
    print("我是func函数")
    values = (11,22,33,44)
    return values



result = func()
print(result)
一个特殊的语法，在某个函数上方使用：
@函数名
def xxx():
    pass

python内部会自动执行 函数名(xxx)，在将结果赋值给xxx。
xxx = 函数名(xxx)
"""
def outer(orange):
    def inner():
        print("befor")
        res = orange()
        print("after")
        return res

    return inner

@outer #func = outer(func)
def func():
    print("我是func函数")
    values = (11, 22, 33, 44)
    return values





# func = outer(func)  # outer(func) func 传递到函数outer函数内部 这是func = orange ，在函数内部res接收了 func的返回值，然后return出来

result = func()  # 这个就相当于单独执行了inner函数  result返回 就是return的res
print(result)
