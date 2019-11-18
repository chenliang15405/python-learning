"""服务端框架---动态处理请求的数据信息"""


def index():
    # 通过读取页面，返回静态服务器，景台服务器再返回到浏览器
    # 在python中，所以模块计算路径的时候，都是以入口的py文件来作为位置进行计算
    with open("./templates/index.html", 'r', encoding='UTF-8') as f:
        content = f.read()
    return content


def login():
    with open("./templates/center.html", 'r', encoding='UTF-8') as f:
        return f.read()


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])

    file_name = env["PATH_INFO"]

    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return login()
    else:
        return "hello word"

