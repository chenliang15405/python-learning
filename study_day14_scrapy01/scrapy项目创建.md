# Scrapy项目创建和技巧

1. 创建一个scrapy项目
`scrapy startproject mySpider`

2. 生成一个爬虫
`scrapy genspider itcast "itcast.cn"`

3. 提取数据   
完善spider、使用xpath方法

4. 保存数据   
pipeline中保存数据

5. 启动scrapy去爬虫
`scrapy crawl itcast`

6. 日志设置  
setting.py中增加：
`LOG_LEVEL="WARNING"`   
`LOG_FILE="./log.log"`   - 如果不设置此属性就是输出到控制台，如果定义了就会输出到文件   
- 再通过import logging模块将日志输出到控制台或者文件找那个
```
import logging
logger = logging.getLogger(__name__)
```