# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class StudyDay14Scrapy01Pipeline(object):

    def process_item(self, item, spider):
        # 用来处理spider处理好的数据，保存到数据库或者其他处理
        item["hello"] = "world"
        return item


# 可以定义多个处理的方法，上一个方法处理完成之后，return数据到这个方法，再进行出处理，
# 方法的优先级在setting.py中定义权重，小的先执行
class StudyDay14Scrapy01Pipeline1(object):

   def process_item(self, item, spider):
        print(item)
        return item
