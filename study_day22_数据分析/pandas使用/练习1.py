"""
使用matplotlib呈现出店铺总数排序前10的国家
"""
import pandas as pd
from matplotlib import pyplot as plt

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# 根据Country分组，并统计个数，只需要随便取一个列的数据即可，然后排序，分片取前10个
data = df.groupby("Country").count()["Brand"].sort_values(ascending=False)[:10]

print(data)

_x = data.index  # 行索引
_y = data.values  # 数据

plt.figure(figsize=(20, 8), dpi=80)

# 设置数据
plt.bar(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x)

plt.show()



