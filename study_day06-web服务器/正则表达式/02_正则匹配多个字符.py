"""
正则的匹配的字符个数

    * 前面的字符可以出现无限次或者0次
    + 前面的一个字符出现1次或者无限次，至少有1次
    ? 前一个字符出现1次或者0次。要么1次，要么没有
    {m} 前一个字符出现固定的次数
    {m, n} 前一个字符出现m到n次


    ^ 匹配开头
    $ 匹配结尾

"""
import re

# {} 中表示前面的字符匹配最多和最少出现的次数
ret = re.match("正则匹配多个字符\d{1,2}", "正则匹配多个字符35")
print(ret.group())


ret = re.match("\d{11}", "130930393039")
print(ret.group())

content = "fjdflds" \
          "jldfsfldsl" \
          "mfsd"

# re.S 表示让 . 可以匹配\n
ret1 = re.match(".*", content, re.S)
print(ret1.group())


email = "laowang@163.com"
ret3 = re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$", email)

if ret3:
    print("符合要求", ret3.group())
else:
    print("不符合要求")