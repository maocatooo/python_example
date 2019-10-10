import numpy as np

arr = np.array([[[1, 2, 3], [2, 3, 4]]], dtype=np.int)

print(arr.dtype)

# 创建array
# 创建两行三列的数据矩阵 内容为0
arr1 = np.zeros((2,3))
print(arr1)

# 创建array
# 创建两行三列的数据矩阵内容为1
arr2 = np.ones((2, 3))
print(arr2)

# 创建array
# 创建两行三列的数据矩阵 内容为[[1. 1. 1.]
#                          [1. 1. 1.]]
#                          这是啥
arr3 = np.empty((2, 3))
print(arr3)

# 创建单行array 0-12 步长为3
arr4 = np.arange(0, 12, 3)
print(type(arr4))

# 创建单行array 0-24 reshape维度 内容必须足够
arr5 = np.arange(24).reshape((3, 4, 2))
print(arr5)

# 创建线段array 1-10 3段, 2个切割点
arr6 = np.linspace(0, 10, 3).reshape((3, 1))
print(arr6)
