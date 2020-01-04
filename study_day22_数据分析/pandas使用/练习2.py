"""
使用matplotlib呈现出中国每个城市的店铺数量

"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")


# 获取中国的数据
df = df[df["Country"] == "CN"]

# 进行分组统计
data = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

# 准备数据画图
_x = data.index   # 获取行索引
_y = data.values  # 获取数据

plt.figure(figsize=(15,8), dpi=80)

plt.barh(range(len(_x)), _y, height=0.3, color="orange")

plt.yticks(range(len(_x)), _x,  fontproperties=my_font)

plt.show()



