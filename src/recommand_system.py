import pandas as pd
import numpy as np

# 电影推荐系统
# 基于item的协同过滤法：寻找相似的电影
# 从csv文件中读取数据
ratings_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('../datas/u.data', sep='\t', names=ratings_cols, usecols=range(3))

movies_cols = ['movie_id', 'title']
movies = pd.read_csv('../datas/u.item', sep='|', names=movies_cols, encoding='ISO-8859-1', usecols=range(2))

ratings = pd.merge(ratings, movies)

# 构造用户的电影矩阵
""""
pivot_table有四个最重要的参数index、values、columns、aggfunc，本文以这四个参数为中心讲解pivot操作是如何进行。
每个pivot_table必须拥有一个index，用于定义透视表的行
Values用于定义透视表的列，Aggfunc设置我们对数据聚合时进行的函数操作，比如sum，mean
columns用于定义透视表的列的子列
"""
movieRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')

# 选择一部电影并生成这部电影与其他所有电影的相似度
starWarsRatings = movieRatings['Star Wars (1977)']
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)

# 去除不流行的电影以避免生成不合适的推荐
ratingsCount = 100
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
popularMovies = movieStats['rating']['size'] >= ratingsCount
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

# 提取与目标电影相类似的流行电影
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.sort_values(['similarity'], ascending=False)[:15]

# 方法二：基于用户的所有评分做出推荐
# 生成每两部电影之间的相似度，并只保留流行电影的相似度
userRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')
corrMatrix = userRatings.corr(method='pearson', min_periods=100)

# 对于每部用户看过并评分过的电影，生成推荐（这里我们选择用户0）
myRatings = userRatings.loc[1].dropna()
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    # 取出与评分过电影相似的电影
    sims = corrMatrix[myRatings.index[i]].dropna()
    # 以用户对这部电影的评分高低来衡量它的相似性
    sims = sims.map(lambda x: x * myRatings[i])
    # 将结果放入相似性候选列表中
    simCandidates = simCandidates.append(sims)

simCandidates.sort_values(inplace=True, ascending=False)

# 将所有相同电影的相似度加和
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)

# 只保留用户没有看过的电影
filteredSims = simCandidates.drop(myRatings.index)
print(simCandidates)