"""

想要创建的对象可以迭代，需要重写__iter__方法,并且该方法需要返回一个对象的引用（这个对象中必须包含__iter__ 和__next__方法）

通过该对象自己定义__iter__ 和 __next__方法来完成迭代

"""


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    """想要创建的对象可以迭代，需要重写__iter__方法,并且该方法需要返回一个对象的引用（这个对象中必须包含__iter__ 和__next__方法）"""
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()

classmate.add("张三")
classmate.add("李四")
classmate.add("王五 ")


for i in classmate:
    print(i)


