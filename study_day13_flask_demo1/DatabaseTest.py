import unittest
from author_book import Author, db, app


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        """initial"""
        app.testing = True
        # switch database database
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/py_flask_test"
        db.create_all()

    def test_add_author(self):
        author = Author(name="测试")
        db.session.add(author)
        db.session.commit()

        # 查询是否由该数据
        result = Author.query.filter_by(name="测试").first()
        print(result)
        self.assertIsNotNone(result)

    def tearDown(self):
        """在所有的测试执行之后再执行的函数，用于清理操作"""
        db.session.remove()
        db.drop_all()
