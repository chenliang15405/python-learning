"""
请求的钩子

"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def index():
    print("hello 执行")
    return "login success"


# 相当于程序启动之后在处理第一个请求的时候执行的函数
@app.before_first_request
def index():
    print("第一次请求处理前执行")


@app.before_request
def index():
    print("每次请求之前都被执行")


@app.after_request
def index():
    print("每次请求之后都执行，出现异常则不执行")


@app.teardown_request
def index():
    # 就算请求的路由不存在，也会执行这个函数
    print(request.path)
    print("每次请求之后执行，无论是否出现异常，都执行")


if __name__ == '__main__':
    app.run()




