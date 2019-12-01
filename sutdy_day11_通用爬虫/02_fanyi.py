"""
百度翻译

"""
import json
import requests
import sys


class FanYi:

    def __init__(self, word):
        self.header = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, " \
                      "like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 "}
        self.word = word
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/sug"

    def parse_url(self, url, params):
        response = requests.post(url, headers=self.header, data=params)
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):
        print(dict_response)
        ret = dict_response["trans"][0]["dst"]
        print("result is : ", ret)

    def run(self):
        # 1.获取语言类型
        # 准备参数
        lang_detect_data = {"query": self.word}
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]

        # 2. 发送请求，翻译
        # 准备参数
        data = {"query": self.word, "from": "zh", "to": "en"} if lang == "zh" else \
                                                {"query": self.word, "from": "en", "to": "zh"}
        response = self.parse_url(self.trans_url, data)
        # 获取翻译结果
        self.get_ret(response)


if __name__ == '__main__':
    word = sys.argv[1]
    f = FanYi(word)
    f.run()


