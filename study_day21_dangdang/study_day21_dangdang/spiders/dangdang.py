# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from copy import deepcopy
import urllib


"""使用scrapy-redis实现爬虫"""
class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://dangdang.com/']
    redis_key = "dangdang"  # 将start_url放在redsi中，实现分布式爬虫

    def parse(self, response):
        # 大分类分组
        div_list = response.xpath("//div[@class='con flq_body']/div")

        for div in div_list:
            item = dict()
            item["b_cate"] = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [i.strip() for i in item["b_cate"] if len(i.strip()) > 0]
            # 第二个类别分组
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt//text()").extract()
                item["m_cate"] = [i.strip() for i in item["m_cate"] if len(i.strip()) > 0][0]
                # 第三个分类分组
                a_list = dl.xpath(".//dd/a")
                for a in a_list:
                    # 获取标题和链接
                    item["s_cate"] = a.xpath(".//text()").extract_first().strip()
                    item["s_href"] = a.xpath(".//@href").extract_first()
                    if item["s_href"] is not None:
                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.parse_book_list,
                            meta={"item": deepcopy(item)}
                        )

    def parse_book_list(self, response):
        item = response.meta.get("item")
        # 获取书的详细数据
        book_list = response.xpath("//div[@class='con body']/ul/li")
        if book_list is not None and len(book_list) > 0:
            for book in book_list:
                item["name"] = book.xpath(".//p[@class='name']/a/text()").extract_first()
                item["book_href"] = book.xpath(".//p[@class='name']/a/@href").extract_first()
                item["price"] = book.xpath(".//p[@class='price']/span[@class='price_n type0']/span/text()").extract()
                item["price"] = "".join(item["price"])
                item["img"] = book.xpath(".//a/img/@data-original").extract_first()
        else:
            book_list = response.xpath("//div[@id='search_nature_rg']/ul/li")
            for book in book_list:
                item["name"] = book.xpath(".//p[@class='name']/a/text()").extract_first()
                item["book_href"] = book.xpath(".//p[@class='name']/a/@href").extract_first()
                item["price"] = book.xpath(".//p[@class='price']/span[@class='search_now_price']/text()").extract_first()
                item["img"] = book.xpath("./a/img/@data-original").extract_first()
                item["desc"] = book.xpath(".//p[@class='detail']/text()").extract_first()

        print(item)

        # 下一页
        next_url = response.xpath(".//li[@class='next']/a/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list,
                meta={"item": item}
            )
