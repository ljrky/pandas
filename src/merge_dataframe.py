"""
类似数据库连接的操作
inner
outer
left
right
"""

import pandas as pd

# 以列的形式创建dataframe
#定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

print("left dataframe is \n", left)

print("right dataframe is \n", right)

# 类似数据库连接的操作
# 根据列名合并数据,类似SQL的: where a.key == b.key
res = pd.merge(left, right, on='key1')
print(res)

# 根据两个列名合并数据,类似SQL的: where a.key1 == b.key1 and a.key2 == b.key2
res = pd.merge(left, right, on=['key1','key2'])
print(res)

# 内连接
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')
print('inner link\n', res)

# 外连接
res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
print('outer link\n',res)

res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print('left link\n',res)

res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print('right link\n',res)


# 类似数据库连接的操作
# 根据行名合并数据,类似SQL的: where a.key == b.key
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)

print(right)


# 依据左右资料集的index进行合并，全包括: how='outer'
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
print(res)


# 依据左右资料集的index进行合并，只包括相同的: how='inner'
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)
