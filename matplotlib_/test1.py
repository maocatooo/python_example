

import random
import matplotlib.pyplot as plt
import matplotlib

a = [random.randint(20, 25) for i in range(120)]

minute_list = range(1, 121)


fig, ax = plt.subplots(figsize=(16, 6))
_x = minute_list[::3]
_x_labels = ['{}点{}分'.format(10+ i // 60, i%60) for i in _x]
# rotation 旋转
plt.xticks(_x, _x_labels, rotation=-90)
ax.plot(minute_list, a)
plt.show()


