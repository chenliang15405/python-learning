"""
定义查询数据库的方法

"""
from pymysql import *


def findAll(sql):
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    cursors = conn.cursor()
    cursors.execute(sql)
    content = cursors.fetchall()
    cursors.close()
    conn.close()
    return content
