"""
 dataFrame是pandas中的二维数据， Series是pandas中的一维数组，只有一个行索引
    DataFrame对象既有行索引，又有列索引
    行索引，表明不同的行，横向索引，叫index，0轴 axis=0
    列索引，表明不同的列，纵向索引，叫columns, 1轴 axis=1

"""
import pandas as pd
import numpy as np

t = pd.DataFrame(np.arange(12).reshape((3, 4)))

# 生成的是dataFrame对象，有列索引和行索引
print(t)

print("*" * 100)

# 自定义行索引和列索引的 表示值, index 行索引，columns 列索引
t1 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("WYZH"))

print(t1)


# 通过字典创建的dataFrame对象，key作为列索引，行索引是 个数
d1 = {"name": ["xiaoming", "xiaohong"], "age": [18, 19], "tel": [10086, 10010]}

t2 = pd.DataFrame(d1)

print(t2)


d2 = [{"name": "xiaoming", "age": 18, "tel": 10086}, {"name": "xiaohong", "tel": 10086}, {"name": "xiaowang", "age": 17}]

t3 = pd.DataFrame(d2)
print(t3)


