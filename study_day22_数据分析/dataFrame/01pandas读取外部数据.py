import pandas as pd


# panndas读取csv中的文件数据
df = pd.read_csv("./dogNames2.csv")

print(df)

# 获取该该字段中大于800的数据
print(df[df["Count_AnimalName"]>800])


