def inse(list1):
    for i in range(1,len(list1)): #i 表示摸到的牌的下标志
        tmp =list1[i]
        j  = i - 1
        while j >=0  and list1[j] >tmp:
            list1[j + 1] = list1[j]
            j -=1
        list1[j +1 ] = tmp
        print(list1)

list1 = [2, 1, 5, 6, 7, 8, 9, 4, 1, 32]
inse(list1)