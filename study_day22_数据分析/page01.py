"""
通过matplotlib 来进行图形的绘画

"""
from matplotlib import pyplot as plt


x = range(2, 26, 2)
y = [10, 15, 25, 13.5, 33, 50, 22, 15, 10, 20, 26, 30]

# 设置图形的大小
plt.figure(figsize=(20,8), dpi=80)


# 设置x轴的刻度和y轴的刻度
_xticks_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xticks_labels[::2])   # 可以通过切片的方式来设置步长
plt.yticks(range(min(y), max(y)+1)[::2])


# 绘图
plt.plot(x, y)

# 保存图片
# plt.savefig("./t1.png")

# 展示图形
plt.show()
