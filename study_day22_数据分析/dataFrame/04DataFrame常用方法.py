"""
pandas中DataFrame的常用方法：
    DataFrame的基础属性：
        df.shape   行数 列数
        df.dtypes  列数据类型
        df.ndim   数据纬度
        df.index  行索引
        df.columns  列索引
        df.values  对象值 俄日为ndarray 数组

    DataFrame整体情况查询
        df.head(3)  显示头部几行，默认5行
        df.tail(3)  显示末尾几行，默认5行
        df.info()  显示信息概览，行数、列数、内存占用等
        df.describe()  快速综合统计结果： 计数、均值、标准差、最大值、最小值、四分位数等

DataFrame中的排序方法：
    df.sort_values()  可以在源码中看其中可以传递的参数，可以根据某个字段排序，并设置升序/降序

df.loc 通过标签索引行取值（通过索引的标签获取）
df.iloc 通过位置获取行数据(123表示第几行)

"""
import pandas as pd
import numpy as np


df = pd.read_csv("./dogNames2.csv")

# print(df.head)
# print(df.info)

df = df.sort_values(by="Count_AnimalName", ascending=False)
# print(s1.head(10))

# 切片取值
"""
 
"""
print(df[:20])

print("*" * 100)

print(df[:20]["Row_Labels"])

# 取多行、多列、点的值
df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("AWYH"))

# 取的是 行索引为 a， 列索引为 W的那一点的值
print(df.loc["a", "W"])

# 获取每一行，第索引为Y的那一列的值
print(df.loc[:, "Y"])

# 获取多行，每列
print(df.loc[["a", "c"], :])

# 获取多列，每行
print(df.loc[:, ["A", "H"]])


# 获取多行，多列
print(df.loc[["a", "b"], ["A", "Y"]])


# 通过 iloc 获取

# 第一行，每一列  行是从0开始的
print(df.iloc[1, :])

# 每一行，第2列
print(df.iloc[:, 2])


# 多行、多列
print(df.iloc[[1, 2], [2, 3]])

# 赋值，更改数据
print(df.iloc[1:, :2])

df.iloc[1:, :2] = 30  
print(df)


print(df["A"])  # 这样取值，获取的是列索引对应的数据
