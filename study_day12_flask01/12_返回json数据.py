"""
返回json数据的方法：
 1. 使用json模块的json.dumps() 方法，并设置响应头中content-type: application/json
 2. 使用flask模块的jsonify() 方法，接收一个字典类型，可以转换为json，并自动设置响应头，也可以接收key=value类型

"""
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/index", methods=["GET"])
def index():
    data = {
        "name": "python",
        "age": 18
    }
    # 返回json类型，通过json模块手动返回
    json_str = json.dumps(data)

    # 返回json数据，并设置响应头
    return json_str, 200, {"Content-Type": "application/json"}


@app.route("/login", methods=["GET"])
def login():
    data = {
        "name": "python",
        "age": 18
    }
    # 通过falsk的jsonify直接返回json数据

    # 可以返回键值对
    # return jsonify(city="123",token="321")

    # 可以将字典直接返回为json字符串类型
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)