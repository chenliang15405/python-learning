from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

"""
使用折线图表示10-12点之间的数据

matplotlib 默认不显示中文，可以通过设置font中文，来显示

mac/linux下查看系统的字体： fc-list   fc-list :lang=zh

修改中文的方式:
    1. matplotlib.rc 可以修改
    2. matplotliba中的font_manager

"""

# windows和linux设置字体的方式：
# font = {
#     'family': "MicroSoft YaHei",
#     'weight': 'bold',
#     'size': 'larger'
# }
# matplotlib.rc("font", **font)
# matplotlib.rc("font", family="MicroSoft YaHei", weight='bold')


# 另一种设置字体的方式
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")



y = [random.randint(20, 35) for i in range(120)]

x = range(0, 120)


# 调整图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置x轴显示的刻度内容
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]

# 设置刻度，并使用步长来设置刻度的密集和稀疏
plt.xticks(x[::3], _xticks_labels[::3], rotation=45, fontproperties=my_font)  # rotation设置旋转的角度，fontproperties设置字体

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(度)", fontproperties=my_font)
plt.title("10-12点的每分钟温度变化折线图", fontproperties=my_font)


# 绘画
plt.plot(x, y)

plt.show()






