

def bubble_sort(arr: list):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



a = [4,5,1,2,7]
bubble_sort(a)
print(a)
