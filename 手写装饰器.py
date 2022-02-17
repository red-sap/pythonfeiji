
def outer(xingcan_task):
    def inner(*args,**kwargs):
        print("用户开始登录")
        yaunhanshudefanhuizhi = xingcan_task(*args,**kwargs)
        print(yaunhanshudefanhuizhi)
        return yaunhanshudefanhuizhi
    return  inner


@outer
def task(user,password):
        print(user)
        print(password)
        if user == "admin" and password == "1q2w3e4r":
            return 0


task("admin","1q2w3e4r")
print(task("admin","1q2w3e4r"))