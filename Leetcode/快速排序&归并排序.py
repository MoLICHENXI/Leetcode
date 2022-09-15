#快速排序
'''
def quicksort(x):
    if len(x) < 2:
        return x
    else:
        base = x[(0+len(x))//2]  #选择基准值至关重要
        less = [i for i in x if i < base]
        bigger = [i for i in x if i > base]
        return quicksort(less) + [base] + quicksort(bigger)
print(quicksort([4,2,1,3,7,9,8,101,15]))
#快速排序核心思想 就是分治法，让所处理的事情不断划分成块，并找到最后适合处理的基线问题，在快速排序中，基线问题就是序列长度为1，此时无序排序，否则一直找一个基准值进行排序
'''



#归并排序
'''
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int (len(lst)/2)

    left = merge_sort(lst[ :middle])#左边
    right = merge_sort(lst[middle: ])#右边
    merged = []
    while left and right:
        merged.append(left.pop(0) if left [0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  #该方法没有返回值，但会在已存在的列表中添加新的列表内容
    return merged

data_lst = [6,202,100,301,38,8,1]
print(merge_sort(data_lst))
'''