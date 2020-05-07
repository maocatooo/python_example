import numpy as np

arr = np.arange(1, 10).reshape((3, 3))
print(arr)
print('===#索引=='*20)
# 索引
print(arr[1])
print(arr[1][1])

# [1:3)的值
print(arr[1:3])
print(arr[1:3, 1])
print(arr[1, 1:2])
print(arr[2:3, 1])

print('===#迭代=='*20)
# 迭代行
for row in arr:
    print(row)

# 迭代列
for col in arr.T:
    print(col)

print(arr.flatten())

for i in arr.flat:    # arr.flat返回的是迭代器
    print(i)
