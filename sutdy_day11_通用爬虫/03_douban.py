"""
豆瓣api请求

"""
import json
from sutdy_day11_通用爬虫.parse_url import parse_url
from pprint import pprint

url = "https://api.douban.com/v2/movie/imdb/tt0111161?apikey=0df993c66c0c636e29ecbb5344252a4a"


html_str = parse_url(url)

# json.loads() 将json字符串转换为python类型
ret = json.loads(html_str)
print(ret)
# 可以使用美化输出
pprint(ret)

# json.dumps()可以将python类型转换为json字符串
with open("douban.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=4))
    # f.write(str(ret))


# 使用json.load()提取文件对象中的数据
with open("douban.json", "r", encoding="utf-8") as f:
    ret1 = json.load(f)
    print(ret1)


# json.dump() 能够将python类型放入对象中
with open("douban1.json", "w", encoding="utf-8") as f:
    json.dump(ret, f, ensure_ascii=False, indent=4)