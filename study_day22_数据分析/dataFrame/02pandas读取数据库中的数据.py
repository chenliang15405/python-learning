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

