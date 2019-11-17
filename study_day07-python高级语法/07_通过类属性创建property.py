"""
通过类属性创建property方式：


"""

class Foo(object):
    # 使用 _xx() 定义的属性和方法，在模块中导入的时候是不能使用的，__ 定义的私有方法是不能在类外访问的

    def _get_bar(self):
        print("getter")
        return "1111"

    def _set_bar(self, value):
        print("setter")
        return 'set value' + value

    def _del_bar(self):
        print("delte")
        return '3333'

    BAR = property(_get_bar, _set_bar, _del_bar, 'description.....')


obj = Foo()

obj.BAR # 调用get_bar方法

obj.BAR = '22222'   # 调用set_bar方法

desc = Foo.BAR.__doc__  # 自动给获取description....

print(desc)

del obj.BAR # 调用del_bar方法
