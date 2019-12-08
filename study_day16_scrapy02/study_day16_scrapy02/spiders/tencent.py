# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://wz.sun0769.com/html/top/report.shtml']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='newsHead clearfix']/table[2]/tr")
        for div in tr_list:
            item = dict()
            item["title"] = div.xpath(".//td[3]/a[1]/@title").extract_first()  # 这个获取的下标是从1开始计算
            item["href"] =  div.xpath(".//td[3]/a[1]/@href").extract_first()
            item["user"] = div.xpath(".//td[5]/text()").extract_first()
            item["publish_date"] = div.xpath(".//td[6]/text()").extract_first()
            # print(item)

            yield scrapy.Request(
                item["href"],   # 再次请求的Url
                callback=self.parse_detail,  # 调用方法进行解析
                meta={"item": item},  # meta标签的作用就是可以传递对象
                dont_filter=True  # 如果再次爬取的页面和当前的domain不一样时需要关掉
            )

        # 翻页
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        print("*"*100)
        print(next_url)
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

    # 解析详情页的数据
    def parse_detail(self, response):
        # item = response.meta.get("item")
        item = response.meta["item"]

        item["content"] = response.xpath("//div[@class='wzy1']//table[2]//div[@class='contentext']/text()").extract()
        item["content_img"] = response.xpath("//div[@class='wzy1']//table[2]//div[@class='textpic']//img/@src").extract()
        # 增加前缀
        item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        # print(item)
        yield item
