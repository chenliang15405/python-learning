import unittest
from login import app
import json
# 导入单元测试模块和login模块中的app


class LoginTest(unittest.TestCase):
    """单元测试"""

    def setUp(self):
        """在执行单元测试之前执行的函数"""
        # 创建web请求客户端，由flask提供
        self.client = app.test_client()

        # 设置falsk工作在测试模式下
        # app.config["TESTING"] = True
        app.testing = True
        # 需要设置为true, 否则代码中报错不会出现详细的错误信息，如果不为true，错误信息为单元测试中会报错的信息s

    def test_empty_user_name_password(self):

        ret = self.client.post("/login", data={})
        # 返回的是视图对象，data是响应体中的数据
        resp = ret.data
        resp = json.loads(resp)

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_correct_user_name_password(self):

        ret = self.client.post("/login", data={"username": "admin", "password": "admin"})
        # 返回的是视图对象，data是响应体中的数据
        resp = ret.data
        resp = json.loads(resp)

        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 0)


if __name__ == '__main__':
    unittest.main()
