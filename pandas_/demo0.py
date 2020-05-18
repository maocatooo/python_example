import pandas as pd

# 读取 excel 第一个sheet 必须要有 xlrd
'''
data = pd.read_excel('demo.xlsx', sheet_name=1)
:arg
    sheet_name=0 读取 excel 第一个sheet
    sheet_name=1 读取 excel 第二个sheet
    sheet_name >>> str 读取具体'sheet_name'的 sheet
    
    不把第1行作为列名，读取Excel那就没有列名，需增加参数：header=None
'''
data = pd.read_excel('demo.xlsx', sheet_name=1)
'''
# 获取最大行，最大列
nrows = data.shape[0]
ncols = data.columns.size
print(nrows, ncols)
'''

'''
#显示列名，以列表形式显示
print(data.columns)
'''
print(data.columns)

# print(data)
# print(data.head())
# print(data['员工编码'])
