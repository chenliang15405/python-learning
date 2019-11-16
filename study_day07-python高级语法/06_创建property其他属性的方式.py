"""
在对象中，可以通过定义property的三种方式，来触发属性的更新等情况并进行计算：

    1。 获取数据: 必须返回一个值，并且没有参数，可以通过计算返回一个值

        @property
        def price(self):
            return 100

    2. setter：  通过@<propertyname>.setter的定义形式，当给property装饰的变量赋值的时候触发此方法
        @price.setter
        def price(self, value):
            # 传递的参数是赋值时的参数
            self.xxx = value


    3. deleter: 通过@<propertyname>.deleter，当删除该property变量的时候触发此方法
        @price.deleter
        def price(self):
            del self.xxx

"""
class Goods(object):

    def __init__(self):
        self.origin_price = 100

        self.discount = 0.8

    @property
    def price(self):
        new_price = self.origin_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.origin_price = value

    @price.deleter
    def price(self):
        del self.origin_price


obj = Goods()

obj.price
obj.price = 200
del obj.price
