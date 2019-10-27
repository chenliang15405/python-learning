"""
缺省参数：
    在定义函数参数的时候，可以定义一个缺省参数，表示该参数可以传递，也可以不传递，如果不传递，则
    使用定义函数时指定的默认值

    相当于JS中的函数默认参


注意：
   1、 定义缺省参数的时候，缺省参数必须定义在参数列表的末尾
   2、 在调用有多个缺省参数的函数时，如果给某个缺省参数传递数据，必须指定缺省参数名



"""

# 定义函数默认参数，如果没有传递该参数，则使用默认值
def test(name, gender = True, age=18):
    """

    :param name: 姓名
    :param gender: 性别 男生 true 女生 false
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s , age = %d " % (name, gender_text, age))


test("小明")
test("小红", False)
test("小王", age=17)
