"""
通过request获取表单信息或者请求的参数信息、json格式信息

路由中的参数一般是restful风格的请求，request是获取表单、json、url上的参数

request中保存的请求信息：

data 一般是json数据保存到data中
form 保存请求的表单格式的数据
args 保存查询参数，url后面的参数
cookies 请求中的cookies信息
headers 请求的headers信息
method 请求的http方法
url 请求的url地址
files 请求的上传文件


"""
from flask import Flask, request


app = Flask(__name__)


# 获取表达格式的请求数据
@app.route("/index")
def index():
    # request中包含了前端发送过来的所有请求数据
    # 通过request.form可以直接提取请求体中的表单格式的数据，是一个字典对象，对于字典如果不保证有没有，则使用get()方法获取，没有则会为None，否则通过[]获取的话可能会报错
    name = request.form.get("name")
    age = request.form.get("age")

    return "hello name=%s age=%s" % (name, age)


# 获取json格式的请求数据
@app.route("/json")
def index():
    # request中包含了前端发送过来的所有请求数据
    # request.data 获取的是json格式的数据
    data = request.data
    print("request data: %s" % data)

    return "hello jsondata=%s" % data


# 获取url后面拼接的参数的请求数据
@app.route("/url")
def index():
    # request中包含了前端发送过来的所有请求数据
    # request.args 获取的是url后面拼接的参数
    name = request.args.get("name")
    print("request url name: %s" % name)

    return "hello url=%s" % name


if __name__ == '__main__':
    app.run(debug=True)
