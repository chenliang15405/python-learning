"""
生成器是特殊的迭代器

    使用关键字 yield  ，如果函数中包含中yield，那么这个函数就是生成器对象，就不是调用函数了


"""

def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a + b
        current_num += 1

# 函数中有yield，就不是调用函数，就是调用一个生成器对象
obj = create_num(10)

# 迭代器对象可以调用next方法获取下一个值
ret = next(obj)
print(ret)

# for i in obj:
#     print(i)



