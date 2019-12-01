import json

from selenium import webdriver
import time


class DouYuSprider:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r"H:\Google\Chrome\Application\chrome.exe"
        self.driver = webdriver.Chrome(chrome_options=options)

        self.start_url = "https://www.douyu.com/directory/all"

    def move_scroll(self):
        """移动滚动条，加载图片，否则图片懒加载，无法获取数据"""
        # 设置窗口最大
        self.driver.maximize_window()
        for i in range(10):
            js = "var action=document.documentElement.scrollTop={}"
            js = js.format((i+1)*1000)
            print(js)
            self.driver.execute_script(js)
            time.sleep(2)

    def get_content_list(self):
        """获取数据"""
        # 先拖动滚动条，因为图片懒加载
        self.move_scroll()

        content_list = self.driver.find_elements_by_xpath("//ul[@class='layout-Cover-list']/li")
        print(len(content_list))
        list = []
        for li in content_list:
            item = dict()
            item["room_img"] = li.find_element_by_xpath(".//img[@class='DyImg-content is-normal ']").get_attribute('src')
            item["room_title"] = li.find_element_by_xpath(".//h3[@class='DyListCover-intro']").text
            item["room_cate"] = li.find_element_by_xpath(".//div[@class='DyListCover-info']/span").text
            item["root_pnum"] = li.find_element_by_xpath(".//span[@class='DyListCover-hot']").text
            item["author_name"] = li.find_element_by_xpath(".//h2[@class='DyListCover-user']").text
            print(item)
            list.append(item)
        next_url = self.driver.find_elements_by_xpath("//li[@class=' dy-Pagination-next']/span[@class='dy-Pagination-item-custom']")
        next_url = next_url[0] if len(next_url) > 0 else None
        print(next_url.text)
        return list, next_url

    def click_tip(self):
        """点击提示按钮"""
        time.sleep(2)
        tip_html = self.driver.find_elements_by_xpath("//div[@class='ZoomTip']/span[@class='ZoomTip-tipHide']")
        tip_btn = tip_html[0] if len(tip_html) > 0 else None
        if tip_btn is not None:
            tip_btn.click()
        else:
            print("页面比例100%")

    @staticmethod
    def save_content_list(content_list):
        """保存数据到文件"""
        print(len(content_list))
        with open("douyu.txt", 'w', encoding="utf-8") as f:
            for item in content_list:
                f.write(json.dumps(item, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        """实现主要逻辑"""
        # 1. start_url
        # 2. 发送请求，获取响应
            # 已经将响应的数据保存到driver中
        self.driver.get(self.start_url)
        # 去掉小提示
        self.click_tip()
        # 3. 提取数据，提取下一页的元素
        list, next_url = self.get_content_list()
        # 4. 保存数据
        DouYuSprider.save_content_list(list)
        # 5. 点击下一页元素，循环获取
        while next_url is not None:
            next_url.click()
            # 需要睡眠，否则会直接发送请求，数据还没有渲染出来
            time.sleep(3)
            list, next_url = self.get_content_list()
            # 4. 保存数据
            DouYuSprider.save_content_list(list)


if __name__ == '__main__':
    dy = DouYuSprider()
    dy.run()
