"""
匹配分组： 可以通过分组的方式获取到匹配正则的对应数据

    |  匹配左右任意一个表达式
    (ab) 将括号中的字符作为一个分组，可以通过正则匹配到的返回值 .group(num) 获取匹配到的括号中的数据，num是第几个括号中的数据
    \num 引用分组 num 匹配到的字符串
    (?P<name>) 分组起别名
    (?P=name) 引用别名为name分组匹配到的字符串


"""
import re

ret = re.match(r"^([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "laowang@126.com")
# 获取匹配到的数据
print(ret.group())
# 获取匹配到的分组数据,获取第一个括号中匹配到的数据
print(ret.group(1))
print(ret.group(2))


# 通过分组匹配正则
html_str = "<body><h1>1232321131</h1></body>"

# 通过分组获取前面正则表示的内容,前面的正则匹配需要加上()
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str)
print(ret.group())

# 给分组起别名 并且引用别名
ret = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str)
print(ret.group())


