from matplotlib import pyplot as plt
import pandas as pd

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

# rating runtime的分布情况
# 选择图形，直方图

# 准备数据, 获取该列的所有值，作为一个数组
runtime_data = df["Runtime (Minutes)"].values

# 计算最大值和最小值
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算直方图的组数,间距为5
group_num = (max_runtime - min_runtime) // 5

# 画图
plt.figure(figsize=(20, 8), dpi=80)

# 设置数据
plt.hist(runtime_data, group_num)

# 设置x轴的显示
plt.xticks(range(min_runtime, max_runtime+5, 5))


# 显示
plt.show()

