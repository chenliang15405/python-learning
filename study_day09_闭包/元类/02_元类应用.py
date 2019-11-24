"""
python3中，可以直接通过metaclass 执行元类是哪一个，指定之后
可以通过自定义的元类来创建类

python3中类默认继承object 以及私有属性的访问在方法/属性名前加类名就可以访问 就是通过Python中的
元类来完成的

"""


def upper_attr(class_name, class_parents, class_attr):

    new_attr = {}
    for name, value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type创建类
    return type(class_name, class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = "bip"


print(Foo.BAR)






