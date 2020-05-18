import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# Series 是带标签的一维数组，
# 可存储整数、浮点数、字符串、Python 对象等类型的数据。
# 轴标签统称为索引


print(s[1])

# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame
dates = pd.date_range('20130101', periods=6)
print(dates)

# 用含日期时间索引与标签的 NumPy 数组生成 DataFrame：
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)

# 用 Series 字典对象生成 DataFrame
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
# DataFrame 的列有不同数据类型

print(df2.dtypes)

print(df.head())
print(df.tail(10))

print(df.to_numpy())
print(df[0:1])
print(df['A'])
print(df.array)
