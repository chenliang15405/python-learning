"""
copy 模块中的方法
    copy.copy() 浅拷贝  只拷贝一层对象到一个新的内存地址中
    copy.deepcopy() 深拷贝 拷贝该对象中的所有属性和对象到新的内存地址中

    注意：
        1. 如果copy.copy()的对象是元组类型，那么copy之后的对象不是一个新的地址，还是一样的地址，因为元组是不可变的,
            但是元组中如果有引用类型，那么copy.copy() 依然是相同的引用地址，但是copy.deepcopy()就会copy一个新的，因为
            里面包含有其他的引用类型改变了深copy的内存地址


"""
import copy

a = [11, 22]
b = [33, 44]

c = [a, b]

d = copy.copy(c)
e = copy.deepcopy(c)

print(id(c))
print(id(d))
print(id(e))


print("-" * 50)
"""使用切片的方式，属于浅拷贝"""

a = [11, 22]
b = [33, 44]

f = [a, b]

g = f[:]

print(id(f))
print(id(g))

print(id(f[0]))
print(id(g[0]))


