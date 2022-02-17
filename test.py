import requests
from concurrent.futures import ThreadPoolExecutor
import time

def task (num):
    time.sleep(2)
    print("this is a task ")
    print(num)
    return num

def bibao(name):
    def done(res):
        print("this is donw ")
        print(res)
    print(name)
    return done

pool = ThreadPoolExecutor(1)
date_dict  = {
    "name":"zhansan",
    "name1":"zhansan1",
    "name2":"zhansan2",
    "name3":"zhansan3",
    "name4":"zhansan4",
    "name5":"zhansan5",
    "name6":"zhansan6",
    "name7":"zhansan7",
    "name8":"zhansan8"
}

for name,value in date_dict.items():
    future = pool.submit(task, value)  # 执行task函数，将name参数 传给task 执行完成后会有一个返回值
    future.add_done_callback(bibao(name))    # 拿着返回值 传给done函数
    # print(name,value)

# for i in range(100):
#     future = pool.submit(task,1)   #执行完成后会有一个返回值
#     future.add_done_callback(done)  #拿着返回值 传给done函数



