"""
int 类型不是可迭代的类型，所以不可以直接迭代
for i in range(10):
    print(i)
这种不是遍历int类型，是遍历一个列表，range(10) 是创建一个1-10的列表

 
元组、列表、字典、字符串都是可迭代类型，数字类型都是不可以迭代的类型


    想要创建的对象可以迭代，需要重写__iter__方法,并且该方法需要返回一个对象的引用（这个对象中必须包含__iter__ 和__next__方法）

"""
from collections.abc import Iterable

print(isinstance("123", Iterable))


""" 自己实现一个可迭代的对象"""
class Classmate(object):

    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    """想要创建的对象可以迭代，需要重写__iter__方法,并且该方法需要返回一个对象的引用（这个对象中必须包含__iter__ 和__next__方法）"""
    def __iter__(self):
        return CalssIterable(self)


# 定义一个迭代器，next方法就是for循环自动调用的方法，通过在上一个对象中返回该对象，实际上迭代的时候，使用的是这个对象
class CalssIterable(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()

classmate.add("张三")
classmate.add("李四")
classmate.add("王五 ")

print("是否是可迭代对象：", isinstance(classmate, Iterable))
calssmate_iter = iter(classmate)
print("判断classmate_iter是否是迭代器:", isinstance(calssmate_iter, Iterable))

print(next(calssmate_iter))


for i in classmate:
    print(i)


