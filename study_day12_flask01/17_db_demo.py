"""
flask中通过 sqlalchemy 来操作数据库

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 配置SQLAlchemy
class Config:
    """配置参数"""
    # 链接配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/py"

    # 设置sqlchemy自动根据数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class Role(db.Model):
    """角色表"""
    __tablename__ = "tbl_roles"  # 指定数据表名称

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # 指定关联表
    # 没有加上db.Column() 表示该字段非数据表中字段，仅用来查询用
    users = db.relationship("User", backref="role")  # 这样配置，查询时直接可以用，role.users 查询role关联的user，
                                                     # 后面的backref表示，user对象可以直接通过user.role查询关联的role


# 创建数模型类
class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明数据库的表名

    # db.Column表示该字段会对应到数据表中
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

    # 两个表关联配置
    # 关联表的类型 和 指定外键的关联表的主键
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))


if __name__ == '__main__':
    # 清除数据库中的所有数据
    db.drop_all()

    # 创建所有的表
    db.create_all()

    # 保存数据


