#线性查找

def laner_serch(lin,sea):
    for inde,val in enumerate(lin):
        if val == sea:
            return inde
    else:
        return  None



print(laner_serch([1,3,4],4))



#二分查找
def aa (list1,shuzu):
    left = 0
    rigth = len(list1)-1
    while left <= rigth:
        mid = (rigth + left) // 2
        if list1[mid] == shuzu:
            return  mid
        elif  list1[mid] < shuzu:
            left = mid + 1
        else:
            rigth = mid -1
    else:
        return None


shuzu = 11
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(aa(list1 ,shuzu))





























