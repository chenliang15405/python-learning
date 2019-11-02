"""
python2+ 使用的是ASCII 编码格式, ASCII没有包含中文
    如果需要在python2.x中使用utf-8, 那么需要在文件的第一行增加：
    # *-* coding:utf8 *-*
    也可以使用：# coding=utf8
    并且在定义中文的字符串的时候，前面加个 u
    str = u"中文"


python3中默认使用的就是UTF-8

"""