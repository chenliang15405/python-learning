"""
模块就是工具包，使用时需要进行导入

模块的导入方式：
    1. import 导入
    import 模块名1, 模块名2
    提示： 在导入模块时，每个模块应该独占一行
        import 模块1
        import 模块2

    可以给模块指定别名:
        import 模块名1 as 模块别名

        注意： 模块别名应该符合大驼峰命名法


    2. from... import 导入

     从 模块 导入 某一个工具， 按需导入
     from 模块名1 import 工具名

    这种导入方式，调用的时候不需要使用模块名 可以直接使用

    from 模块名 import *
    这种导入方式，可以将模块中的所有工具导入，并且调用的时候，不用使用模块名来调用，可以直接使用

    注意：
        如果不同的模块中导入的相同的函数或者属性，那么后定义的会覆盖上面导入的
        所以，如果有相同的导入的函数，可以使用 as 关键字重名名

        from 模块名 import 工具名 as 别名


导入模块时的搜索顺序
    1. 先搜索当前目录下的模块名，有就直接导入
    2. 如果没有找到，再搜索指定的系统目录

    所以，模块的名称不要和系统的模块名称重名



在导入模块时，在模块中直接执行的代码，会在导入的文件中，直接执行

所以需要使用 __name__ 属性保证，模块中直接执行的代码不需要执行，
作用： 在被导入的时候，不执行测试代码
       在模块中运行的时候，是执行该代码


"""

import random

# 使用 __file__属性可以查看当前导入的模块的路径
print(random.__file__)



# 所以，需要在模块中写的测试代码，在别人导入的时候是不需要执行的，那么使用__name__ 判断

def say_hello():
    print("say hello")

# 判断是否是自定执行该代码
if __name__ == "__main__":
    print(__name__)

    say_hello()



