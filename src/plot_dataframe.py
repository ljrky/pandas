"""
将数据可视化
- plot: 曲线图
- plot.scatter: 散点图
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# 累加数据
data = data.cumsum()
# 生成plot图，x轴=行，y轴=列
data.plot()
# 画图
plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )
data = data.cumsum()
data.plot()
plt.show()

# 画散点图
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# 叠加散点图
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()

