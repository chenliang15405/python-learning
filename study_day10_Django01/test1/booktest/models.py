from django.db import models

# Create your models here.

"""
模型类.objects属性可以调用如下函数，实现对模型对应的数据表查询：
get() ： 返回表中满足条件的一条且只能有一条的数据，如果实际查询到多条则报错，返回一个模型对象
all(): 返回数据表中的所有数据，返回值是QuerySet类型
filter():  返回满足条件的数据
exclude() 返回不满足条件的数据
order_by() 
BookInfo.objects.all().order_by("id") 升序   BookInfo.objects.all().order_by("-id") 降序 

模糊查询：
    contains
    startswith
    endswith

范围查询 in

比较查询：
    大于：gt
        BookInfo.objects.filter(id__gt=3)
    小于等于：
        lte
 
"""



# 设计和表对应的类，模型类，orm会自动根据实体创建表
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称，CharField 表示是一个字符串，最大长度为20
    btitle = models.CharField(max_length=20)
    # 发布日期， DateField 表示是日期类型
    bpub_date = models.DateField()

    def __str__(self):
         return self.btitle


# 英雄人物类
"""
 关系属性： 建立图书类和人物类的之间的一对多的关系
"""
class HeroInfo(models.Model):
    """英雄人物表"""
    # 名称
    hname = models.CharField(max_length=20)
    # BooleanField说明是bool类型，default指定默认值
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)

    # 指定关系属性，建立图书类和英雄人物类之间的一对多关系
    # 创建表之后的字段名称： 关系属性名_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
