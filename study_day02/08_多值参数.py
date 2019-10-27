"""
多值参数: 表示定义函数时，参数的个数是不确定的

python中有两种多值参数：
    1. 参数名前增加一个 * 可以接收元组
    2. 参数名前增加两个 * 可以接收字典

一般给多值参数命名时，使用一下两个名字：
    *args   存放元组参数，前面有一个*
    **kwargs 存放字典参数，前面有两个**

"""


def test(num, *args, **kwargs):
    print("第一个参数 %s" % num)
    print(f"多值元组参数{args}")
    print(f"多值字典参数{kwargs}")


test(1)
test(1, 2, 3, 4, 5, 6)
# 会自动将这些参数封装到对应的类型变量中
test(1, 2, 3, 4, 5, 6, name="小明", age=18, gender=True)

"多值函数的求和"


def sum_num(*args):
    # 接收到的是一个元组，所以遍历求和
    result = 0
    for item in args:
        result += item

    return result


# 这样传递的是单独的数，使用多值函数，如果不使用多值函数，也可以传递一个元组
# result = sum_num((1, 2, 3, 4, 5)) 
result = sum_num(1, 2, 3, 4, 5)

print("多值函数求和为： %d" % result)
