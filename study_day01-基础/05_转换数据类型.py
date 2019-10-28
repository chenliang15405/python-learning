"""
数据类型的转换

int(xxx) 转换为int
float(xxx) 转换为 float
str(xxx) 转换为str
list(xxx) 将序列转换为列表
tuple(xxx) 将序列转换为元组
eval(str) 用来计算字符串中有效的python表达式，并返回一个对象 ---- 就是说将字符串中的数据转换为它原本的数据类型

"""

text = input("请输入数字：")

num = int(text)
print(num)
print(type(num))


# 将列表转换为元组
l = [10,20,30]
print(tuple(l))

# 将元组转换为列表
t = (10,20,30)
print(list(t))

# eval 转换
str1 = "1"
str2 = "1.1"
str3 = "[10,20,30]"

print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))

