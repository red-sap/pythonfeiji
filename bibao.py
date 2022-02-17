mylist = [1,2,3,4,5]
def func(obj):
    print("func:",obj)
    def func1():
        obj[0] += 1
        print("func1:",obj)
    return func1
var  = func(mylist)
var()
var()