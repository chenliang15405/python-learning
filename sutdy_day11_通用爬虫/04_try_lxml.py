"""
使用lxml

"""
from lxml import etree

text = """
       <div>
            <ul>
                <li class="item-1"><a>first item</a></li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-inactive"><a href="link3.html">third item</a></li>
                <li class="item-1"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a>
            </ul>
        </div>
        """

# 将字符串转换为element对象
html = etree.HTML(text)
print(html)
# 查看element对象中包含的字符串
print(etree.tostring(html).decode())

# 获取class为item-1 li下的a的href
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

# 获取class为item-1 li下的a的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)


# 每个li是一条新闻，把url和文本组成字典
for url in ret1:
    item = dict()
    item["href"] = url
    item["text"] = ret2[ret1.index(url)]
    print(item)

# 使用lxml、xpath实现
ret3 = html.xpath("//li[@class='item-1']")
print(ret3)

for item in ret3:
    item_list = {}
    item_list["text"] = item.xpath("./a/text()")[0] if len(item.xpath("./a/text()")) > 0 else None
    item_list["href"] = item.xpath("./a/@href")[0] if len(item.xpath("./a/@href")) > 0 else None
    print(item_list)






