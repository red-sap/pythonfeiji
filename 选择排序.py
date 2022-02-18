# 选择排序  时间复杂度 O（n的平方）
# def sort_xuanze(list_m):
#     list_new = []
#     for i in range(len(list_m)):
#         min_val = min(list_m)
#         list_new.append(min_val)
#         list_m.remove(min_val)
#     return list_new
#
#
# list1 = [2,4,5,6,7,8,9,4,1,32]
# print(sort_xuanze(list1))


def sort_slect(list):
    for i in range(len(list) -1 ):
        min_num = list[i]
        for j in range(i + 1 ,len(list)):
            if list[j] <=  list[min_num]:
                min_num = j
        list[i],list[min_num] = list[min_num],list[i]
    return  list





list1 = [2, 4, 5, 6, 7, 8, 9, 4, 1, 32]
print(sort_slect(list1))
# 插入排序
#
#
# NB三人组
# 快速排序
# 堆排序
# 归并排序
#
#
# 其他排序
#
# 希尔排序
# 计数排序
# 基数排序