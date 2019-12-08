# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名字，启动爬虫的时候：scrapy crawl itcast
    allowed_domains = ['itcast.cn']  # 允许爬取的url范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 开始爬取的地址，start_url不受allowed_domains的限制，其他的受限制

    # 数据提取的方法，接收下载中间件downloader传过来的response
    def parse(self, response):
        # div_first = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(div_first)
        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")  # 如果在路径中写//表示不是直接子标签，可能隔了好多个，如果是/表示就是下面的一个

        for li in li_list:
            item = dict()
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            logger.info(item)
            # 通过yield 来将当前的item对象发送到pipeline中, 不能直接传递一个集合过去
            yield item
