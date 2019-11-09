"""
正则表达式模块 re

    match 匹配的是字符串的开头，只要符合即可，并不管后面如何
    re.match(正则表达式, 需要处理的字符串)

    . 匹配任意字符，除了\n
    \D 匹配非数字，不是数字
    \s 匹配空白，空格、tab
    \S 匹配非空白
    \w 匹配单词字符，a-z A-Z 0-9 _
    \W 匹配非单词字符

"""
import re

ret = re.match("这是一个数字\d", "这是一个数字3")
# 通过group()方法获取匹配的内容
print(ret.group())

ret = re.match("这是一个数字[1-9]", "这是一个数字5")
# 通过group()方法获取匹配的内容
print(ret.group())

# [] 表示可以匹配到其中一个指定的数字即可
ret = re.match("这是一个数字[1-9abcd]", "这是一个数字a")
# 通过group()方法获取匹配的内容
print(ret.group())