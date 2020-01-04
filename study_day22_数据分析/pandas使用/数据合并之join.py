"""
join: 默认情况下两个数组进行join，那么就会将行索引相同的数据合并在一起

df1.join(df2) 如果df1中只有2行，合并之后的数组就只有2行，df2有3行，则合并之后去掉一行
df2.join(df1) 如果df2中有3行，df1只有2行，合并之后，没有的数据则以NaN填充

merge: 按照指定个的列把数据按照一定的方式合并在一起

    默认是内连接，只保留可以匹配到的数据进行列的合并


"""
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.zeros((2, 3)), index=["A", "B"], columns=list("abc"))

df2 = pd.DataFrame(np.ones((3, 4)), index=["A", "B", "C"])

# join两个数组

# df1 join df2， df1只有2行，则join之后的数组只有2行，df2会去掉一行
print(df1.join(df2))

# df2 join df2  df2有3行，df1只有2行，则不够的一行 会以NaN填充
print(df2.join(df1))


# merge 两个数组, 按照列进行合并

df3 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list("fax"))
df4 = pd.DataFrame(np.ones((2, 4)), columns=list("abcd"))

print(df3)
print(df4)

# 根据 列"a" 来进行合并列，df4中有2列，则df3中的a列中如果可以匹配到df3中的几个数，则保留几个数，默认是内连接
print(df4.merge(df3, on="a"))
# inner 取并集，默认是inner

# 外连接： 里那个哥哥数据的交集，如果没有的则以NaN补全
print(df4.merge(df3, on="a", how="outer"))

# left 左连接，以左边的为准, 少了补NaN, merge的数组多了就去掉
print(df4.merge(df3, on="a", how="left"))

# right 右连接，少了补NaN，多了去掉左边的
print(df4.merge(df3, on="a", how="right"))
