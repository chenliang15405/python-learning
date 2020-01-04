"""
分组： groupby() 可以获取到分组对象，有聚合的方法、可以遍历

"""
import pandas as pd

file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# 根据 Country 列进行分组
grouped = df.groupby(by="Country")
print(grouped)

# 根据分组统计个数，取一个字段的数据即可
country_count = grouped["Brand"].count()

print(country_count["US"])
print(country_count["CN"])

# 统计中国每个省店铺的个数
china_data = df[df["Country"] == "CN"]

group_data = china_data.groupby(by="State/Province").count()["Brand"]

print(group_data)



