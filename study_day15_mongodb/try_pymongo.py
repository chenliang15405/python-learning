"""
python中直接操作mongodb
"""
from pymongo import MongoClient


# 实例化mongolient, 建立连接
client = MongoClient(host="127.0.0.1", port=27017)
collection = client["test"]["t1"]  # mongodb中直接使用该数据库和集合就相当于创建了

# 插入一条数据
# ret = collection.save({"name": "zhangsan", "age": 18})  # save方法在id存在的情况下会更新，insert会报错
ret = collection.insert({"name": "zhangsan", "age": 19})
print(ret)

# 插入多条数据-- 数据类型必须是字典类型, mongodb中存储的是BSON
data_list = [{"name": "test{}".format(i) for i in range(10)}]
collection.insert_many(data_list)

# 查询一个记录, 就算符合条件的有多条，但是也只会查询出来一条
t = collection.find_one({"name":"zhangsan"})
print(t)

# 查询所有记录
cursor = collection.find({"name": "zhangsan"})
# find查询的结果是游标对象，是一个可迭代对象，类似于读文件的指针，读取一次指针到结尾就不会再读出来数据
for i in cursor:
    print(i)

for j in cursor:
    print(j)  # 此时游标的指针已经到结尾了

# 更新一条数据
"""更新数据时，需要加上$set 否则会将原始数据替换为更新的数据，其他的属性不会合并"""
collection.update_one({"name": "zhangsan"}, {"$set": {"new_zhangsan"}})

# 更新全部数据
collection.update_many({"name": "zhangsan"}, {"$set": {"name": "new_test"}})

# 删除一条数据
collection.delete_one({"name": "mew_zhangsan"})

# 删除所有条件的数据
collection.delete_many({"name": "new_test"})

