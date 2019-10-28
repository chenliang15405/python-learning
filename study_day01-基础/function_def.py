"""
定义函数的语法：

def 函数名(参数):
    代码...


使用函数/模块：

在另一个文件中，使用import 关键字倒入函数

import 工具包名

工具包名.函数名称()


如果是在当前的包中，可以直接调用函数名() 即可完成调用

"""


def say_hello():
    """
    python中函数的文档注释在这里
    :return:
    """
    print("hello 1")
    print("hello 2")
    print("hello 3")


say_hello()


# 函数的参数


def sum_2_num(num1, num2):
    """对两个数字的求和"""
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_num(1, 2)


# 使用return 关键字返回函数的结果
def sum(num1, num2):
    """计算两个数的求和

    :param num1: 计算的数字1
    :param num2: 计算的数字2
    :return:  返回的和
    """
    return num1 + num2


count = sum(1, 2)
print("计算的求和结果：%d" % count)
