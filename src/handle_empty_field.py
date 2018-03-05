""""
如何处理dataframe中的空值
- 判断哪些是空值: isnull()
- 删掉空值行或者列: dropna(axis=1, how='any')
- 用给定值来填充空值: df.fillna(value=0)
"""

import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan

print(df)

# 判断是否有空值，把整个dataframe列出来
print('does df having null value? \n', df.isnull())

# 直接去掉空的行或者列
# how=any,有一个是空的，就去掉整行或者整列
# how=all,只有全部是空，才去掉整行或者整列
df_no_empty = df.dropna(axis=1, how='any')

print(df_no_empty)

# 用value填充空的值
df_fill_with_zero = df.fillna(value=0)
print(df_fill_with_zero)