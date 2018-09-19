#冒泡排序
def bubble_sort(list1):
    length = len(list1)
    for i in range(0,length-1):
        for j in range(0,length-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return (list1)


#插入排序
def insert_sort(list1):
    length = len(list1)
    for i in range(1, length):
        if list1[i - 1] > list1[i]:
            temp = list1[i]  # a当前需要排序的元素
            index = i  # 记录索引该处用于插入元素
            while index > 0 and list1[index - 1] > temp:
                list1[index] = list1[index - 1]  # 把按序列排序好的元素往后移动一位，给要插入的元素留出位置
                index -= 1  # 每循环一次减一
            list1[index] = temp  # 条件不满足跳出循环，降元素插入位置
        return list1


#递归快排
def quick_sort(list1):
    length =len(list1)
    if length < 1:
        return []
    key = list1[0]
    left_sort = quick_sort([i for i in list1[1:] if i < key])
    rigth_sort = quick_sort([j for j in list1[1:] if j >= key])
    return left_sort+[key]+rigth_sort


if __name__ == '__main__':
    a = [23, 12, 4, 44, 11, 12, 32]
    print(bubble_sort(a))
    print("********************")
    print(insert_sort(a))
    print("***********************")
    print(quick_sort(a))


