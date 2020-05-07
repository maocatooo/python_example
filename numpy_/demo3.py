import numpy as np

arr = np.array([[5, 2, 3, 4], [2, 3, 4, 5]])

arr1 = np.array([0, 1, 2, 3])
# 做下面的内容必须长度,类型一致,才能进行运算
print(arr+arr1)
print(arr-arr1)


print(arr**2)

print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))

print(arr < 2)
print(arr == 2)
# 矩阵乘法
print(np.dot(arr, arr1))

arr2 = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
print(arr2.dot(arr))
print(arr.dot(arr2))
