from django.db import models

# Create your models here.

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
