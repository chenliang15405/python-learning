from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/set_cookie")
def index():
    resp = make_response("success")

    # 设置cookie，默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie("python", "123")

    # 通过max_age设置过期时间，单位 秒
    resp.set_cookie("python1", "321", max_age=3600)

    return resp


@app.route("/get_cookie")
def index():
    # 所有的请求信息都在request中
    c = request.cookies.get("python")
    return c


@app.route("/delete_cookie")
def index():
    resp = make_response("del success")
    resp.delete_cookie("python")
    return resp


if __name__ == '__main__':
    app.run()
