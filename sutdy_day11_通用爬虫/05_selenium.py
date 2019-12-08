"""
selenium 是web自动测试化工具，用于操作浏览器页面

PhantomJs 是请求浏览器页面，并且能够执行该页面的js，将浏览器加载到内存中执行

"""
from selenium import webdriver
import time


# 实例化一个浏览器
options = webdriver.ChromeOptions()

# 指定地址
options.binary_location = r"H:\Google\Chrome\Application\chrome.exe"

# 加载驱动
driver = webdriver.Chrome(chrome_options=options)

# 发送请求
driver.get("http://www.baidu.com")

# 进行页面截屏
driver.save_screenshot("./baidu.png")

# 元素定位方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

"""
页面元素定位
用法：
find_element_by_id(返回一个)
find_elments_by_xpath(返回一个列表）
find_elemnts_by_link_text（通过文本获取超链接元素，可以在获取其中的属性）


selenium的使用
1. 先定位到元素，然后再获取`.text`或者get_attribute方法获取属性
2. find_element 返回一个element，如果没有会报错
3. find_elements 返回一个列表，如果没有就是空列表 

如果页面中含有iframe或者frame，那么需要先切换到frame中，才能定位到元素中
driver.switch_to.frame()切换

selenium在请求第一页的时候会等待页面加载完成才获取数据，但是在点击翻页之后，会直接获取数据，此时
可能会报错，因为数据还没有加载出来，需要time.sleep(3)

"""

time.sleep(3)
# 退出浏览器
driver.quit()
