from flask import Blueprint

# 定义蓝图对象
# 需要配置子模块中的默认模版路径，并且如果主模块中已经有该文件，会直接加载主模块中的模版，不会加载子模块的模版
app_cart = Blueprint("app_cart", __name__, template_folder="templates")

# 需要在这里暴露视图函数，将视图加载进来，让主模块知道有这个子模块的视图存在
from .views import get_cart
