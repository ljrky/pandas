import pandas as pd

# 从csv文件中读取数据
data = pd.read_csv('../datas/student.csv')
print(data)

# 将数据存成pickle
pickle_file = data.to_pickle('../datas/student.pickle')
print(pickle_file)