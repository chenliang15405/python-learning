"""
不同年份的书的数量

不同年分的书的平均数

"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

file_path = "./books.csv"
df = pd.read_csv(file_path)
print(df.info())

# 先剔除为nan的数据
data = df[pd.notnull(df["original_publication_year"])]

data = data.groupby(by="original_publication_year").count()["title"]
print(data)

plt.figure(figsize=(20, 8), dpi=80)

_x = data.index
_y = data.values

plt.plot(range(len(_x)), _y)

plt.xticks(range(len(_x))[::10], _x[::10], rotation=45)
plt.show()


# 不同年份数的评分

data1 = df[pd.notnull(df["original_publication_year"])]

# 获取average_rating字段，并根据original_publication_year分组 并获取均值
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(grouped)

_x1 = grouped.index
_y1 = grouped.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x1)), _y1)

plt.xticks(range(len(_x1))[::10], _x1[::10], rotation=45)
plt.show()
