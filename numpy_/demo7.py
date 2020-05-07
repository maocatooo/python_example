import numpy as np

arr = np.array([1, 1, 1])

arr1 = np.array([0, 0, 0])
v = np.vstack((arr, arr1))
h = np.hstack((arr, arr1))
print(v)
print(h)
print(v.shape)
print(h.shape)

# 添加一个维度
# np.newaxis = None
print(arr[:, np.newaxis])

# 多个维度的合并
arr = arr[:, np.newaxis]
arr1 = arr1[:, np.newaxis]
arr2 = np.concatenate((arr, arr1, arr), axis=1)
print(arr2)

# for i in arr2:
#     for j in i:
#         print(j)
