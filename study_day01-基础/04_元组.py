"""
元祖 Tuple

元祖与列表相似，但是元祖中的数据是不能修改

元祖用 () 定义，使用 , 分隔数据


元祖的常用操作：

   元祖.index(数据) 数据在元祖中的索引
   元祖.count(数据) 数据在元祖中出现的次数


    len(元祖) 元祖的长度


元祖的循环遍历：
    for 变量 in 元祖:
        操作元素



元祖和列表之间的数据转换：

  将元祖转换为列表
    list(元祖)

  将列表转换为列表
    tuple(列表)

"""

info_tuple = ('zhangsan', 18, 1.75)

print(type(info_tuple))

# 通过索引获取数据
print(info_tuple[0])

# 循环遍历
for info in info_tuple:
    print(info)


# 格式化字符串的时候，就是使用了元祖的方式
str_tuple = ('zhangsan', 18, 1.75)
# 格式化字符串
str = "%s 的年龄是 %d 身高是 %.2f " % str_tuple

print(str)