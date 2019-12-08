from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


class Config(object):
    # sqlalchemy的连接参数
    # 使用python3 连接mysql需要安装pymysql库，并且uri连接改变，并且创建表的语句不能放在main中，无法运行
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/py_flask"

    # 设置自动跟踪数据库变更
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "fjldjjfilsflewnlnlnl"


app.config.from_object(Config)

db = SQLAlchemy(app)


# 定义数据模型
class Author(db.Model):
    """作者数据模型"""
    __tablename__ = "tbl_author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    books = db.relationship("Books", backref="author")


class Books(db.Model):
    """书籍数据模型"""
    __tablename__ = "tbl_books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_author.id"))


db.drop_all()
db.create_all()

au_xi = Author(name="我吃西红柿")
au_san = Author(name="唐三")
au_tudou = Author(name="天蚕土豆")
db.session.add_all([au_xi, au_san, au_tudou])
db.session.commit()

bo_xi = Books(name="星辰变", author_id=au_xi.id)
bo_san = Books(name="斗罗大陆", author_id=au_san.id)
bo_tudou = Books(name="斗破苍穹", author_id=au_tudou.id)
db.session.add_all([bo_xi, bo_san, bo_tudou])
db.session.commit()


# 创建表单模型类，用于展示页面的表单
class AuthorBookForm(FlaskForm):
    """表单页面模型类"""
    author_name = StringField(label="作者", validators=[DataRequired("作者必填")])
    book_name = StringField(label="书籍", validators=[DataRequired("书籍必填")])
    submit = SubmitField(label="保存")


@app.route("/", methods=["GET", "POST"])
def index():
    form = AuthorBookForm()

    if form.validate_on_submit():
        # 验证表单成功
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Books(name=book_name, author_id=author.id)
        # book = Books(name=book_name, author=author)
        db.session.add(book)
        db.session.commit()

    # 查询数据库数据展示
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li, form=form)


@app.route("/delete_book", methods=["POST"])
def delete_book():
    # 获取参数
    req_dict = request.get_json()
    # 从json中获取数据
    book_id = req_dict.get("book_id")
    # 查数据，并删除
    book = Books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify(code=0, message="OK")


@app.route("/delete_get", methods=["GET"])
def delte_book_get():
    # 获取参数
    book_id = request.args.get("book_id")
    # 查数据，并删除
    book = Books.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
