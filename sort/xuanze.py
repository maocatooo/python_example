

def select_sort(arr: list):
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length-1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

a = [4,5,1,2,7]
select_sort(a)
print(a)
