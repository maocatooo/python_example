# import matplotlib.pyplot as plt
#
# fig = plt.figure(figsize=(5, 5), dpi=110)
#
#
# x = tuple(range(2, 26, 2))
# print(x)
# y = tuple(range(2, 26, 2))
#
#
# print(y)
#
# fig1, ax1 = plt.subplots(figsize=(9, 3), dpi=320)
# ax1.plot(x, y)
# ax1.legend()
# plt.show()


import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 1, figsize=(9, 3), dpi=320, sharey=True)
# figsize = (9, 3) 长款
# dpi = 320 像素

# 设置刻度 yticks = Y轴 xticks = X轴
plt.yticks([i + 1 for i in values])
# 清空刻度
# plt.yticks([])

axs.bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')
plt.show()
