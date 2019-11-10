"""
在一个函数中修改全局变量，到底是否需要加global，要看是否对全局变量的指向修改，如果没有修改指向，只是修改指向对象中的数据
那么不需要加global，因为该全局变量的引用地址没有变化，但是如果是基本类型，修改值就相当于修改指向，所以需要加global

"""
g_num = 100
g_nums = [11, 22]


def test():
    global g_num

    g_num += 100


def test1():
    # 这里只是修改列表中的数据，所以不需要加global，因为该对象的指向没有变化
    g_nums.append(33)


print(g_num)
print(g_nums)

test()
test1()

print(g_num)
print(g_nums)








