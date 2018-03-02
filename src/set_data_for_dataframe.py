""""
DataFrame更新数据
- 通过loc更新行index或者列index的数据: df.loc['20130102',['A','B']]
- 通过iloc更新定位置的数据，其实就是二维数组访问形式: df.iloc[3,1]
- 通过条件，类似sql中的where: df.D[df.A > 8]

更新整行或者整列的数据
- 列数据, 比如挑选 b 列的元素: df['b'] / df.b
- 行数据, 比如挑选 1 列的元素: df.values[0] / df[0:1]

添加数据
- 列数据, 添加一个F列的元素: df['F'] / df.F
- 行数据, 使用loc添加

"""

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(data=np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])

print("df is \n", df)

df.iloc[2,2] = 1111
df.loc["2013-01-01", "A"] = 2222

print("df is \n", df)

# 我们想要更改D中的数, 而更改的位置是取决于 D 的. 对于D大于等于19的位置. 更改D在相应位置上的数为3333
df.D[df.D >= 19] = 3333

print("df is \n", df)

# 添加数据
# 添加列，需要提供数据，行index
df['E'] = pd.Series([23, 24, 25, 26, 27, 28],index=pd.date_range('20130101', periods=6))
print("df is \n", df)

index = pd.datetime(year=2013,month=1,day=8)
df.loc[index] = [123, 124, 125, 126, 127]
print("df is \n", df)