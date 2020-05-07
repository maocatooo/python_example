import numpy as np

arr = np.arange(0, 12).reshape((3, 4))
print(arr)
# split只能进行相等的分割
print(np.split(arr, 2, axis=1))
# array_split 可以进行不相等的分割
print(np.array_split(arr, 3, axis=1))

# 纵向分割
print(np.vsplit(arr, 3))
# 横向分割
print(np.hsplit(arr, 3))