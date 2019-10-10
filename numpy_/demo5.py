import numpy as np

arr = np.arange(1, 10).reshape((3,3))

print(arr)
# 最小值的索引
print(np.argmin(arr))
print(arr.argmin())
# 平均值
print(np.mean(arr))
print(np.average(arr))

# 中位数
print(np.median(arr))

# 累加
print(np.cumsum(arr))

# 累差
print(np.diff(arr))

print(arr)
print(np.nonzero(arr))

arr1 = np.arange(10, 1, -1).reshape((3, 3))
# 排序, 按照行
print(np.sort(arr1))

# 矩阵转置
arr2 = np.arange(10, 0, -1).reshape((2, 5))
print(np.transpose(arr2))
print(arr2.T.dot(arr2))

