

# 快速排序
def quick_sort(arr: list, low, high):
    if low >= high:
        # 限定条件
        return
    mid = arr[low]
    low = low
    high = high
    while low < high:
        while low < high and arr[high] > mid:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] < mid:
            low += 1
        arr[high] = arr[low]
    arr[low] = mid
    quick_sort(arr, 0, low-1)
    quick_sort(arr, low+1, high)


a = [4, 5, 1, 2, 7]
quick_sort(a, 0, len(a)-1)
print(a)
