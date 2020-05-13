# 插入排序
def insert_sort(arr: list):
    length = len(arr)
    for i in range(1, length):
        while i > 0:
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                i -= 1


a = [4, 5, 1, 2, 7]
insert_sort(a)
print(a)
