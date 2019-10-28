"""
列表（数组）
[] 就是定义一个空列表

方法：
    列表.sort() 升序排序
    列表.sort(reverse=True) 降序排序
    列表.reverse() 逆序

    列表.index(数据) 获得数据第一次出现的索引
    列表.insert(索引,数据) 在指定的索引出插入数据
    列表.append(数据) 在末尾追加数据
    列表.extend(列表2) 将列表2的数据追加到列表1
    列表.remove(数据)删除第一个出现的指定数据
    列表.pop() 删除末尾数据
    列表.pop(索引) 删除指定索引的数据


    del 列表[索引]  也可以实现删除对应的数据
     ps: del 关键字本质上将一个比变量从内存中删除

    len(列表) 统计元素的长度

    列表。count(数据) 统计数据在列表中出现的次数


列表的循环遍历：
    for 变量 in 列表:
        对元素操作

"""

name_list = ['zhangsan', 'lisi', 'wangwu']

name_list.sort()

print(name_list)

# 修改
name_list[1] = '李四'
print(name_list)

# 增加
name_list.append("增加数据")
print(name_list)

# 删除
name_list.remove("lisi")
# 删除末尾数据
name_list.pop()
print(name_list)

# 通过关键字删除列表中数据
del name_list[1]
"""
 del 关键字本质上将一个比变量从内存中删除
"""
print(name_list)


# 列表的长度
length = len(name_list)
print(length)


num_list = [1, 2, 3, 4, 5]
# 迭代遍历
for num in num_list:
    print(num)

