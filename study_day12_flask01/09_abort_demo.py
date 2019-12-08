"""
abort 中断函数使用

"""
from flask import Flask, abort, Response

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def index():
    name = ""
    pwd = ""
    if name != "123" or pwd != "123":
        # 可以使用abort函数终止视图函数的执行
        # 返回前段特定的信息，只可以指定标准的状态码
        abort(404)
        # 通过abort返回响应体信息
        resp = Response("login faild")
        return abort(resp)

    return "login success"


if __name__ == '__main__':
    app.run(debug=True)

