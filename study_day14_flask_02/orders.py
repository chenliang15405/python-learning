from flask import Blueprint

"""
蓝图就是小模块的抽象的概念，为了防止模块和主类的循环引用问题，给其他模块定义蓝图，来作为在主模块中方便引入并且可以正确定义子模块的路由路径
"""
app_orders = Blueprint("app_routes", __name__)  # 指定当前目录为蓝图的根目录


@app_orders.route("/get_orders")
def get_orders():
    return "get_orders page"
