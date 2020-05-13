# 归并
def merge_sort(arr: list):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length // 2
    left_list = merge_sort(arr[0:mid])
    right_list = merge_sort(arr[mid:])
    res = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left_list) \
        and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            res.append(left_list[left_pointer])
            left_pointer += 1
        else:
            res.append(right_list[right_pointer])
            right_pointer += 1
    res += right_list[right_pointer:]
    res += left_list[left_pointer:]
    return res


a = [4, 5, 1, 2, 7]
a = merge_sort(a)
print(a)
