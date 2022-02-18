import random
# lowB三人组
# 冒泡排序
# 列表每两个相邻的数，如果前面的比后面的大，则交换这两个数字
# 一趟排序完成后，则无序区域减少一个数，有序增加一个数字 时间复杂度 O（n的平方）
def sort_mopao(list_m):
    for i in range(len(list_m) - 1):
        for j in range(len(list_m) - i - 1):
            if list_m[j] > list_m[j + 1]:
                list_m[j], list_m[j + 1] = list_m[j + 1], list_m[j]


list_m = [random.randint(0, 10000) for i in range(100)]
print(list_m)
sort_mopao(list_m)
print(list_m)


# 冒泡排序改进版
# 增加一个标志位  如果没有发生排序 则不用继续执行
def sort_mopao(list_m):
    for i in range(len(list_m) - 1):
        exchange = False
        for j in range(len(list_m) - i - 1):
            if list_m[j] > list_m[j + 1]:
                list_m[j], list_m[j + 1] = list_m[j + 1], list_m[j]
                exchange = True
        if not exchange:
            return


list_m = [random.randint(0, 10000) for i in range(100)]
print(list_m)
sort_mopao(list_m)
print(list_m)


# 选择排序
# def sort_xuanze(list_m):
#     list_new = []
#     fot
#     i in range(list_m):
#     min_val = min(list_m)
#     list_new.append(min_val)
#     li.remove(min_var)
#
#
# return list_new

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