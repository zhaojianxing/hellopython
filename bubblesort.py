def bubble_sort(list1):
    length = len(list1)
    for i in range(0,length-1):
        for j in range(0,length-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return (list1)


