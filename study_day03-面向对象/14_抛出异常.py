"""
抛出异常：
    1. 创建一个Exception对象
    2. 使用`raise`关键字抛出异常


"""


def input_password():

    pwd = input("请输入密码:")

    if len(pwd) > 8:
        return pwd

    print("主动抛出异常")
    # 创建异常对象, 指定错误信息
    ex = Exception("密码长度不够")
    raise ex


# 处理异常
try:
    input_password()
except Exception as result:
    print(result)


