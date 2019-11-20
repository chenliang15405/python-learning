"""服务端框架---动态处理请求的数据信息"""

# 定义字典，用来存储路由
g_url_route = dict()


# 定义装饰器
def router(url):

    def set_func(func):
        # 将路由的url和调用的对应的方法存储到字典中，在请求的时候通过路由信息调用对应的方法
        g_url_route[url] = func

        def call_func(*args, **kwargs):
            func()
        return call_func
    return set_func


@router("/index.html")
def index():
    # 通过读取页面，返回静态服务器，景台服务器再返回到浏览器
    # 在python中，所以模块计算路径的时候，都是以入口的py文件来作为位置进行计算
    with open("./templates/index.html", 'r', encoding='UTF-8') as f:
        content = f.read()
    return content


@router("/center.html")
def center():
    with open("./templates/center.html", 'r', encoding='UTF-8') as f:
        return f.read()


def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])

    file_name = env["PATH_INFO"]

    return g_url_route[file_name]()

