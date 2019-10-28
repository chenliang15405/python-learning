"""

字符串可以通过 " 或者 ' 来定义，如果字符串内部使用 "，外面可以使用' ,如果内部需要使用' 外部则使用" ，或者可以通过\" 转译内部的"

字符串的遍历

for 变量 in 字符串:
    操作...


字符串常用方法：

    1. 统计字符串长度
    len(字符串)

    2. 统计某个字符出现的次数
    字符串.count(字符)

    3. 某个字符出现的位置
    字符串.index(字符)  如果没有找到，则报错
    字符串.find(字符)  如果没有找到，返回-1


    文本对齐：
    1. ljust(width)   文本向左对齐
    2. rjust(width)  文本向右对齐
    3. center(width)  居中, 宽度为多少个长度， 可以选则第二个参数 fillStr: 填充的字符是什么，默认是英文空格


    去除空白字符:
     1.  strip() 方法去除字符串中的空白字符 去除左右两边的字符串


    拆分和链接：
     split([str], [num])  拆分字符串, 如果没有传递参数，则表示以\t \n \r和空格来进行拆分，num表示仅分隔num+1个字符串

     string.join(序列) 以string作为分隔符，将序列中的所有元素链接


字符串的切片：
    包前不包后截取
    字符串[开始索引:结束索引:步长]



"""

str = "123"
print(str.index("1"))
print(str.find("5"))

# 判断空白字符
space_str = "   \t\n\r"
print(space_str.isspace())

# 判断字符串中是否只包含数字
num_str = "1"
print(num_str.isdecimal()) # 只包含数字
print(num_str.isdigit()) # 包含数字，有其他特殊符号也算
print(num_str.isnumeric())  # 包含数字和中文数字

# 查找和替换
str1 = "123456hello"
print(str1.startswith("2"))
print(str1.endswith("hello"))
print(str1.find("h"))
# 替换
# replace方法执行完成会返回一个新的字符串，不改变原有字符串
str1 = str1.replace("6","10")
print(str1)

# 字符串切片
var = str[0:2]
print(var)

# 通过字符串切片试下字符窜逆序
str = "0123456789"
str2 = str[::-1]
str3 = str[-1::-1]
print(str2)
print(str3)

