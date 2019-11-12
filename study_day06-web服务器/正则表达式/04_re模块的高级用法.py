"""
1. search：
    可以通过分组获取正则匹配到的第一个字符串

2. findall：
    可以获取正则匹配到的所有的内容，返回一个列表

3. sub(re, replaceStr, str)：
        使用正则匹配字符串中的内容，并使用第二个参数替换，并返回最后的字符串

4. split(re, str):
     使用正则表达式来进行切割，返回一个列表


"""
import re

# 如果有多个匹配到的内容，则取第一个
ret = re.search(r"\d+", "阅读次数为 99999")
print(ret.group())


ret = re.findall(r"\d+", "阅读次数为 99999, 点赞数为：66666")
print(ret)

#  替换
ret = re.sub(r"\d+", "998", "python = 997")
print(ret)


ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
print(ret)


