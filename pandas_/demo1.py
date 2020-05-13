import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# Series 是带标签的一维数组，
# 可存储整数、浮点数、字符串、Python 对象等类型的数据。
# 轴标签统称为索引


print(s[1])
