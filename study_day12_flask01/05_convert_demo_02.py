"""
python的参数转换器

"""
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)


# 1. 定义自定义的转换器
class RegexConverter(BaseConverter):
    """自定义转换器，用于处理参数和接收参数"""
    def __init__(self, url_map, regex):  # 第二个参数，是flask初始化此转换器传递的，第三个是自定义的路由规则传递进来的
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，这个regex属性是父类中定义的固定正则表达式属性，flask会根据这个属性定义的规则去匹配路由中的参数
        self.regex = regex


# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter


# 3. 使用自定义的转换器匹配路由参数
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    """定义的视图函数"""
    return "send sms number: %s" % mobile


if __name__ == '__main__':
    app.run(debug=True)

