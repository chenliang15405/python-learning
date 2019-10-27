"""
列表的+= 操作本质上是在执行列表的extend方法，不会修改变量的引用

如果是不可变类型变量例如 字符串、整数等的+=操作，是赋值操作，会修改变量引用

"""


def test(num, num_list):
    print("函数开始")
    num += num

    # 列表的+= 本质上调用extend方法，
    # num_list.extend(num_list)
    num_list += num_list

    print(num)
    print(num_list)

    print("函数结束")

num = 1
num_list = [1, 2, 3]

test(num, num_list)

print(num)
print(num_list)
