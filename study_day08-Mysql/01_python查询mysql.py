"""
需要使用的模块：
    pymysql

"""
from pymysql import *


def main():
    # 创建链接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='py', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql
    cursor.execute("select * from jd")
    # 取出数据
    one = cursor.fetchone()
    many = cursor.fetchmany(5)
    data = cursor.fetchall()
    # 从游标中取出数据之后，游标中就会少掉取出的数据，再次取就会没有该数据
    print(one)
    print(many)
    print(data)

    conn.close()


if __name__ == '__main__':
    main()



