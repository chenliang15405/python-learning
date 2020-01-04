import pandas as pd
import numpy as np

# 创建数据
t = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("WXYZ"))
print(t)

# 设置为nan
t.iloc[1:, :2] = np.nan
print(t)

# 判断 null的数组
print(pd.isnull(t))

# 判断不为null
print(pd.notnull(t))

# 不为null的数组，W列
print(t[pd.notnull(t["W"])])

print(pd.notnull(t["W"]))

# 删除 NAN的行或者列
print(t.dropna(axis=0))  # axis为0 表示行索引，删除有NAN的行

print(t.dropna(axis=1))  # 删除有NAN的列

print(t.dropna(axis=0, how="all"))  # 表示该行全部为NaN才删除，否则不删除

# 删除的方式
print(t.dropna(axis=0, how="all"))  # 表示该行全部为NaN才删除，否则不删除

print(t.dropna(axis=0, how="any"))  # 表示该行中只要有NaN就删除

# 删除时是否修改原数组
# t.dropna(axis=0, how="any", inplace=True)
# print(t)

# 填充数组
print(t.fillna(100))

# 填充均值
print(t.fillna(t.mean()))

# 可以按照列来选择性填充.再赋值给原数组
t["W"] = t["W"].fillna(t["W"].mean())
print(t)


# 计算平均值的情况，NaN是不会参与计算，0是会参与计算

