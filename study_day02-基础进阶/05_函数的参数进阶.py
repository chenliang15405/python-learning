"""
在函数内部，对参数进行赋值语句，不会影响函数调用时传递的外部参数，相当于在函数内部修改局部变量的引用，
不会影响外部变量的引用，无论是可变参数还是不可变采纳数

注意： 对于可变类型变量如果使用赋值语句，就是重新定义了这个参数变量的地址值，不会修改原有变量
        但是，如果是修改这个参数变量中的数据，那么是会修改外部变量的数据的！！



"""


def test(num, num_list):

    num =  100
    num_list = [4,5,6]

    print("函数内部不可变参数num的值为： %d" %num)
    print(f"函数内部可变参数列表num_list的值为{num_list}")

num = 99
num_list = [1, 2 ,3]
test(num, num_list)

print("不可变参数num的值为： %d" % num)
print(f"可变参数列表num_list的值为{num_list}")


"修改可变类型变量的数据"
def test2(list):

    list.append(5)
    print(f"函数内部赋值之后的list的值为{list}")


list = [3, 2, 1]
test2(list)

print(f"外部调用函数赋值之后的list的值为{list}")
