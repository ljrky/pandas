""""
DataFrame获取数据
- 列数据, 比如挑选 b 列的元素: df['b'] / df.b
- 行数据, 比如挑选 1 列的元素: df.values[0] / df[0:1]
- 通过loc得到行index或者列index的数据: df.loc['20130102',['A','B']]
- 通过iloc得到给定位置的数据，其实就是二维数组访问形式: df.iloc[3,1]
- 通过条件，类似sql中的where: df[df.A > 8]
"""

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(data=np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# 如何获取列数据
print('Column A \n', df['A'])
print("Column B \n", df.B)

# 如何获取行数据
# 通过切片得到行数据
print("all row\n", df[0:-1])
print("row 0 \n", df[0:1])

# 通过index得到行数据
print("index 20130101\n", df['20130101':"20130101"])

# 通过loc得到行index或者列index的数据
print(df.loc['20130102', ['A', 'B']])

# 通过iloc得到给定位置的数据，其实就是二维数组访问形式
print(df.iloc[3, 1])

# 通过条件，类似sql中的where
print(df[df.A > 8])
