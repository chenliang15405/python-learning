"""
自定义响应信息，状态吗和响应体信息

"""
from flask import Flask, make_response

app = Flask(__name__)


# 通过元组返回响应信息
@app.route("/login", methods=["GET"])
def login():
    # 1. 使用元组，返回自定义的响应信息
    # 响应体  状态码  响应头       其中响应头选填
    # return "login page", "1001"
    return "login page", "1001", {"token": "123", "city1": "city"}


# 通过 make_response 返回响应信息
@app.route("/index", methods=["GET"])
def index():
    resp = make_response("index page")  # 设置响应体信息
    resp.status = "1002"    # 设置状态码
    resp.headers["city"] = "city111"   # 设置响应头

    return resp


if __name__ == '__main__':
    app.run(debug=True)
