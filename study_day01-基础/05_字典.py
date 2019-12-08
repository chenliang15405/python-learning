"""

字典和列表的区别

  字典存储的是无序的对象集合
  列表存储的是有序的对象集合
  字典中存储的数据是无序的

字典使用 {} 定义，存储的是 键值对，使用 , 分隔

注意：
    键必须是唯一的
    值可以使用任何数据类型，但是键只能使用 字符串、数字 或者 元祖


常用操作：
   1. 取值
   字典[key]
    ps: 如果取的值不存在，则报错

   2. 增加/修改
    字典[key] = value
     ps: 如果该key不存在，则新增，如果key存在，则修改

   3. 删除
    字典.pop(key)
    删除指定的key, 如果key不存在，则报错


   4. 统计键值对数量
   len(字典)  获取字典的长度

   5. 合并字典
    （1）字典1.update(字典2)
     字典1 将字典2 合并到自己的字典中，如果字典1中已经包含该key value，那么就会被字典2的覆盖

    （2）如果需要给字典中添加多个键值对，也可以使用update方法，字典1.update({key1=value1, key2=value2})

   6. 清空字典
   字典.clear()


字典的循环遍历

    for key in 字典:
        操作

    其中： key 是字典中的每个 key，可以通过key获取字典中的value



"""

xiaoming = {
    "name": "xiaoming",
    "age": 18,
    "height": 1.75
}


# 取值
name = xiaoming["name"]
print(name)

# 增加/ 秀挂
xiaoming["name"] = "1111"
name = xiaoming["name"]
print(name)

xiaoming["width"] = "222" # 新增
print(xiaoming)


# 删除
xiaoming.pop("width")
print(xiaoming)


# 合并字典
temp_dict = {"width": 999}

xiaoming.update(temp_dict)

print(xiaoming)


# 清空字典
xiaoming.clear()
print(xiaoming)