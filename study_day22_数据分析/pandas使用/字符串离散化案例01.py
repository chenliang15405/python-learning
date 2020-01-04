import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df["Genre"])

# 根据获取到的分类，制作柱状图，表示每个分类的电影数量的多少

temp_list = df["Genre"].str.split(",").tolist()

print(temp_list)

# 去重
genre_list = list(set([i for j in temp_list for i in j]))
print(genre_list)

# 构造全为0的数组 并转换为pandas的数组, 设置列索引
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
print(zeros_df)

# 给每个电影出现，则甚至该点为1
for i in range(df.shape[0]):
    # 需要使用loc，因为指定第几行这里使用列索引和行索引来指定的 iloc使用数字来指定
    zeros_df.loc[i, temp_list[i]] = 1

print(zeros_df.head(3))

# 统计每个分类出现的电影的数量和
sum_count = zeros_df.sum(axis=0)  # 根据行索引来统计，那么就会出现每个列对应一个sum数据
print(sum_count)

# 排序
sum_count = sum_count.sort_values()

# 画图，准备数据
_x = sum_count.index  # 行索引，就是分类名称
_y = sum_count.values  # 数据

# 制作条形图
plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y, width=0.5, color="orange")  # 设置有多少个bar, y表示数据为多少，个数需要对应

# 设置坐标
plt.xticks(range(len(_x)), _x)

plt.show()


