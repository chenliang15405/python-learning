from flask import render_template
from . import app_cart
# . 代表当前模块，如果是__init__，则可以不写，默认为__init__为包下的默认文件


@app_cart.route("/get_cart")
def get_cart():
    return render_template("cart.html")
