"""
如果用 python 的列表和字典来作比较, 那么可以说 Numpy 是列表形式的，没有数值标签，而 Pandas 就是字典形式。
Pandas是基于Numpy构建的，让Numpy为中心的应用变得更加简单。

主要两个数据结构：Series和DataFrame。
Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。

DataFrame是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。
DataFrame既有行索引也有列索引， 它可以被看做由Series组成的大字典。创建DataFrame，
第一个参数是数据，index是行名，columns是列名
df = pd.DataFrame(data=np.random.randn(6,4), index=dates,columns=['a','b','c','d'])

DataFrame获取数据
- 列数据, 比如挑选 b 列的元素：df['b']
- 行数据, 比如挑选 1 列的元素：df2.values[1]

获取获取DataFrame的统计数据
df2.describe

DataFrame排序
- 根据索引的值进行排序
- 根据列的值排序
"""


import numpy as np
import pandas as pd

# Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。
s = pd.Series([1,3,6,np.nan,44,1])
print("Series S is : ",s)


dates = pd.date_range('20160101', periods=6)

# 创建DataFrame，第一个参数是数据，index是行名，columns是列名
df = pd.DataFrame(data=np.random.randn(6,4), index=dates,columns=['a','b','c','d'])
print('df is \n',df)

# 从Numpy数组创建DataFrame
df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print('df1 is \n',df1)

# 通过类似数据库create的形式创建DataFrame
df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20130101'),
    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4,dtype='int32'),
    'E':pd.Categorical(["test","train","test","train"]),
    'F':'foo'
})

print('df2 is \n',df2)

# 获取DataFrame的行名
print('df2 index is \n',df2.index)

# 获取DataFrame的列名
print('df2 columns is \n',df2.columns)

# 获取获取DataFrame的全部数据
print('df2 values is \n',df2.values)

# 获取获取DataFrame的统计数据
print('df2 descire is \n',df2.describe)

# 根据索引的值进行排序
print(df2.sort_index(axis=1,ascending=False))
# 根据索引的值进行排序
print(df2.sort_index(axis=0,ascending=False))

# 根据数据的值进行排序
print(df2.sort_values(by=['E']))