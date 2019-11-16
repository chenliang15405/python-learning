"""
使用pymysql防止sql注入:

         参数是列表类型，sql中通过%s 来占位
         cursor.execute(sql, params)

"""
from pymysql import *


def main():
    # 创建链接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='py', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql 防止sql注入，使用参数的形式，不要使用拼接参数
    sql = "select * from jd where name=%s"

    # 构建参数列表, 如果sql中有多个%s，那么就需要多个列表中的参数
    params = ["MAC"]

    count = cursor.execute(sql, params)

    # 受影响的函数
    print(count)

    print(cursor.fetchall())

    # 提交所有的操作事务
    conn.commit()
    # 回滚
    # conn.rollback()

    # 关闭链接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()





