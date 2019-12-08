"""
自定义异常处理器

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

    return "login success"


@app.errorhandler(404)
def err_404_handler(err):
    """自定义异常处理函数"""
    # 参数为具体的信息
    return "出现404错误，具体信息： %s" % err


if __name__ == '__main__':
    app.run(debug=True)

