"""
python的参数转换器

"""
from flask import Flask, redirect, url_for
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

    def to_python(self, value):
        print("to_python被调用")
        # value是在路径进行正则匹配的时候提取的参数，这里决定返回给视图函数的参数到底是什么
        return value

    def to_url(self, value):
        # 这个url是别的视图函数通过url_for重定向过来，携带参数的时候，可以对携带参数进行处理的方法
        return value


class MobileConverter(BaseConverter):
    def __init__(self, url_map):
        super(MobileConverter, self).__init__(url_map)
        self.regex = r'1[34578]\d{9}'


# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters["mobile"] = MobileConverter


# 3. 使用自定义的转换器匹配路由参数
@app.route("/send/<mobile:mobile_num>")  # 定义的mobile的转换器会进行正则匹配，不过这种事固定的，上面的re转换器是通用的，可以根据传递的正则匹配不同的参数
def send_sms(mobile_num):
    """定义的视图函数"""
    return "send sms number: %s" % mobile_num

@app.route("/index")
def send_sms():
    url = url_for("send_sms", mobile_num="18911111111")
    return redirect(url)



if __name__ == '__main__':
    app.run(debug=True)

