"""
selenium 是web自动测试化工具，用于操作浏览器页面

PhantomJs 是请求浏览器页面，并且能够执行该页面的js，将浏览器加载到内存中执行

PhantomJs 使用报错：selenium.common.exceptions.WebDriverException: Message: 'phantomjs' executable needs to be in PATH.

1. 下载phantomJs --- 下载链接
2. 将phantomjs.exe 放到python的根目录下
3. 这样应该就可以了，如果还是不可以，那么就配置一个环境变量，path中加上phantomjs.exe的绝对路径即可

"""
from selenium import webdriver
import time


# 实例化一个浏览器
driver = webdriver.PhantomJS()

# 设置窗口的大小
# driver.set_window_size(1920, 1080)

# 最大化窗口
driver.maximize_window()

# 发送请求
driver.get("http://www.baidu.com")

# 进行页面截屏
driver.save_screenshot("./baidu.png")

# 元素定位方法
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()

# 获取cookie
cookies = driver.get_cookies()
print(cookies)

cookies = {i["name"]:i["value"] for i in cookies}
print(cookies)

time.sleep(3)
# 退出浏览器
driver.quit()
