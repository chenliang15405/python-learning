from flask import Flask
from orders import app_orders
from cart import app_cart
# 使用蓝图是为了解决引入子模块的循环引用问题，蓝图可以实现一个工程中多个子模块的关联和引入到主模块中


app = Flask(__name__)

# 注册蓝图
# app.register_blueprint(app_orders)

# 注册蓝图的时候，就是说该蓝图是是一个子模块中的独立模块，可以增加url前缀来更好的分离模块
app.register_blueprint(app_orders, url_prefix="/orders")

app.register_blueprint(app_cart, url_prefix="/cart")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
