from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(11,31)
y1 = [1, 0, 2, 2, 3,4,5,6,2,3,0,0,1,2,3,9,3,1,2,3]
y2 = [0,1,1,2,3,6,7,8,9,5,6,1,2,3,4,3,2,1,1,1]


# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
# 增加图列，就是标识线的区分
"""
在绘制折线的时候，可以设置多个属性
plt.plot(
    x,
    y,
    color='r',  # 颜色 
    linestyle='--',  # 线条的形状
    linewidth=5, # 线条的宽度
    alpha=0.5  # 透明度
)

"""

plt.plot(x, y1, label="自己", color='#ccc', linestyle='--', linewidth=5)
plt.plot(x, y2, label="同桌", color='cyan', linestyle=':')

# 设置x轴的刻度
_xticks_label = ["{}岁".format(i) for i in x]

plt.xticks(x, _xticks_label, fontproperties=my_font)

# 设置y轴刻度
plt.yticks(range(0, 10))

# 绘制网格
plt.grid(alpha=0.5)

# 添加图例
# 可以设置图例的位置
plt.legend(prop=my_font, loc="upper left")

# 展示图表
plt.show()


