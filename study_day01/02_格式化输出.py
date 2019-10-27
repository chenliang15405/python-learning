'''
格式化符号有：
%s 格式化字符串  也可以直接将其他类型的变量格式化为字符串填充
%d 有符号的十进制整数   %03d 表示位数不足时补全，如果位数足够则不改变
%f 浮点数  保留小数位的方式： %.2f 保留2位小数
%u 无符号的十进制数据（格式化正数）

如果有多个需格式化的内容，则通过 %(x, y) 语法填充

'''

'''
f'{表达式}' 也可以用来格式化字符串

不同点： f'{表达式}' 相对于 %s 比较高效

'''

age = 18
name = "TOM"
weight = 60.6
num=111

#1. 年龄18岁
print("年龄%d岁" %age)

#2. 姓名为tom
print("姓名为%s" %name)

#3. 体重为60.6
print("体重为%.2f" %weight)

#4. 学号是001
print("学号是%03d" %num)

#5. 名字是tom 年龄18岁
print("名字是%s,年龄%d岁" %(name, age))

#6 名字是tom 年龄18岁
print("名字是%s,年龄%s岁" %(name, age))

#7.名字是tom 年龄18岁
print(f'名字是{name},年龄是{age}岁')