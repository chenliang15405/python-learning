"""

"""
class Fibonaci(object):


    def __init__(self, all_nums):
        self.current_num = 0
        self.all_nums = all_nums
        self.a = 0
        self.b = 1

    """想要创建的对象可以迭代，需要重写__iter__方法,并且该方法需要返回一个对象的引用（这个对象中必须包含__iter__ 和__next__方法）"""
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonaci(10)

for i in fibo:
    print(i)

