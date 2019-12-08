from flask import Flask
from flask_script import Manager  # 启动命令的管理类

app = Flask(__name__)

"""
通过flsk的扩展脚本来增加功能，
Manager可以设置服务启动的方式
python xxxx.py runserver -h 0.0.0.0 -p 8000
python xxx.py shell         相当于进入Python交互器，并且已经启动导入该模块
"""
# 创建的管理类
manager = Manager(app)


@app.route("/index")
def index():
    return "login success"


if __name__ == '__main__':
    manager.run()
