"""
class中的特殊属性：property属性

    定义方式：
        通过@property装饰器来定义，仅有self参数
        调用时无需括号
        必须返回一个值

        @property
        def name(self):
            return xxx

        该属性必须返回一个值，通过对象直接调用属性名

"""

class Goods:

    @property
    def size(self):
        return 100


obj = Goods()
data = obj.size
print(data)

