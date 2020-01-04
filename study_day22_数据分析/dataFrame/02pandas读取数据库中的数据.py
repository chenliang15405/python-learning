from pymongo import MongoClient
import pandas as pd


client = MongoClient()  # 默认链接本地
collection = client["douban"]["tv1"]
data = list(collection.find())

t1 = data[0]
t1 = pd.Series(t1)

print(t1)

# 可以使用dataframe

df = pd.DataFrame(data)
print(df)


# 显示头几行
print(df.head(1))  # 显示头一行

print(df.tail(2))  # 显示尾部2行

print(df.info())  # 显示df的概览

print(df.describe())  # 显示均值、最大值、最小值等数据
