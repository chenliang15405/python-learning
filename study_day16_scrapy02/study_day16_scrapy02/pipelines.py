# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class StudyDay16Scrapy02Pipeline(object):

    def open_spider(self, spider):
        # 在爬虫开启的时候执行的代码
        client = MongoClient(host="127.0.0.1", port=27017)
        self.collection = client["test"]["t2"]


    def process_item(self, item, spider):
        print(item)
        # 保存到数据库找中，并且将该类型转换为字典类型才可以保存
        self.collection.insert(dict(item))
        return item
