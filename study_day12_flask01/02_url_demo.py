from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    """定义的视图函数"""
    return 'Hello World!'


# 定义访问的method
@app.route("/post_only", methods=["GET", "POST"])
def post_only():
    return "post only page"


# restful url，通过mehtod区分不同的路由
@app.route("/hello", methods=["GET"])
def hello1():
    return "hello1"


@app.route("/hello", methods=["POST"])
def hello2():
    return "hello2"


@app.route("/hi1")
@app.route("/hi2")
def hello3():
    return "hi 1 2"


# 重定向，将当前的请求重定向到其他的请求或者重定向到项目的其他路由上
@app.route("/login")
def login():
    # 重定向的路由可以通过url_for的函数，通过视图函数名称获取视图路径的url路径
    url = url_for("hello_world")
    print(url)
    return redirect(url)


if __name__ == '__main__':
    # 通过url_map获取整个flask中的路由信息
    print(app.url_map)
    # 启动flask程序
    app.run(debug=True)
