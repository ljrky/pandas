""""
合并数据
- 纵向或者横向合并数据: pd.concat([df1, df2, df3], axis=0, ignore_index=True)
- 如果两个数据index有重复的处理:
-- pd.concat([df1, df2], axis=0, join='outer')
-- pd.concat([df1, df2], axis=0, join='inner')
- 按照列或者行的index来合并: pd.concat([df1, df2], axis=1, join_axes=[df1.index])
- 纵向合并数据: df1.append([df2, df3], ignore_index=True)
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

# 纵向合并数据
res = pd.concat([df1, df2, df3], axis=0)
print(res)

# 纵向合并数据,并重置index
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)

# 横向合并数据
res = pd.concat([df1, df2, df3], axis=1)
print(res)

# 如果index有重复，可以通过outer或者inner处理重复部分
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b', 'c', 'd', 'e'], index=[2, 3, 4])

# 包括全部数据，重复的行或者列就删掉
res = pd.concat([df1, df2], axis=0, join='outer')
print(res)

# 只留下两边都有的行或者列，其他删掉
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index=True)
print(res)

# 添加行数据
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

res = df1.append([df2, df3], ignore_index=True)
print(res)


# 按照列或者行的index来处理
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

# 依照`df1.index`进行横向合并
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
print(res)


# 纵向合并数据
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

res = df1.append([df2, df3], ignore_index=True)
print(res)