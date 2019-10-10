import numpy as np

arr = np.random.random((2,3))

print(arr)
print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))

print(arr)
# axis 1=行,0=列
print(np.sum(arr, axis=1))
print(np.min(arr, axis=1))
print(np.max(arr))

