import numpy as np

a = np.arange(0, 12).reshape((3, 4))
b = a
c = a.copy()
d = np.copy(a)

a[0][0] = 1
print(a)
print(b)
print(c)
print(d)
