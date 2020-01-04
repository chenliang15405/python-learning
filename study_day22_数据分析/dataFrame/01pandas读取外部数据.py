import pandas as pd


# panndas读取csv中的文件数据
df = pd.read_csv("./dogNames2.csv")

print(df)

# 获取该该字段中大于800的数据
print(df[df["Count_AnimalName"]>800])

# 获取该字段中大于800 小于1000的数据
# 如果是多个条件，需要使用 & 连接

# 通过df["Count_AnimalName"] 获取的是该列中对应的数据，比较之后，df[] 是获取该列数据的全数据
print(df[(df["Count_AnimalName"]>800) & (df["Count_AnimalName"]<1000)])


# 获取使用次数大于700 并且 名字的字符串长度大于4的数据

print(df[(df["Count_AnimalName"]>700) & (df["Row_Labels"].str.len() > 4)])

# 使用 .str 就可以将其他类型转换为 string类型
# tolist()方法可以将数组转换为list列表


