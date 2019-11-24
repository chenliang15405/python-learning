from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    """自定义模型管理器--图书类型"""

    def all(self):
        # 调用父类的all，获取所有的数据
        books = super().all()
        # 过滤
        books = books.filter(isDelete=False)
        return books


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称，CharField 表示是一个字符串，最大长度为20
    btitle = models.CharField(max_length=20)
    # 发布日期， DateField 表示是日期类型
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0, null=True, blank=True)  # null表示是否可以为null,默认为false, null是约束数据库的，blank是约束后台的表单数据
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 是否删除
    isDelete = models.BooleanField(default=False)

    # 如果自定义模型管理器，返回的对象名称必须叫做objects,因为查询的时候就是 BookInfo.objects.all()
    objects = BookInfoManager()  # 自定义模型管理器获取对象

    def __str__(self):
         return self.btitle

    # 定义模型对应的数据表
    class Meta:
        db_table = "bookinfo"  # 指定模型类对应的表名


# 英雄人物类
"""
 关系属性： 建立图书类和人物类的之间的一对多的关系
"""
class HeroInfo(models.Model):
    """英雄人物表"""
    # 名称
    hname = models.CharField(max_length=20)
    # BooleanField说明是bool类型，defaulzt指定默认值
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)

    # 指定关系属性，建立图书类和英雄人物类之间的一对多关系
    # 创建表之后的字段名称： 关系属性名_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)

    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    # 代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True,  on_delete=models.CASCADE)



