import pandas as pd


file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

print(df.info())
print(df.head(1))

# 获取电影的平均评分、导演信息

# 平均评分
print(df["Rating"].mean())

# 导演人数
set_arr = set(df["Director"].tolist())
print(len(set_arr))

#可以直接通过方法驱虫
print(len(df["Director"].unique()))

# 获取演员人数
print(df["Actors"].str.split(", ").tolist()) # 这样获取到一个二维数组

df_arr = df["Actors"].str.split(", ").tolist()
arr = [i for j in df_arr for i in j]
arr1 = set(arr)
print(len(arr1))


# 电影时长的最大最小值
print(df["Runtime (Minutes)"].max())
print(df["Runtime (Minutes)"].min())

print(df["Runtime (Minutes)"].idxmin())

print(df.shape[0])  # 这样可以获取到所有行数，0轴是行索引
