"""
python的参数转换器

    python中农已经定义好的内置转换器有：
        1. int 接收整数
        2. float 接收浮点数
        3. path 和默认的（字符串）相似，也接受斜线/

"""

from flask import Flask

app = Flask(__name__)


# 转换器，表示接受参数，并将参数会转换为int类型，视图函数的接收参数名称必须是后面定义的名称
# 127.0.0.1/goods/123
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    """定义的视图函数"""
    return "goods detail page"


# 如果不加转换器类型，则默认是字符串类型参数（除了/的字符）
@app.route("/goods/<goods_num>")
def goods_detail(goods_num):
    """定义的视图函数"""
    return "goods detail page"


if __name__ == '__main__':
    app.run(debug=True)

