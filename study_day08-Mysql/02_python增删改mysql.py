"""
增删改需要操作事务

"""
from pymysql import *


def main():
    # 创建链接
    conn = connect(host='localhost', port=3306, user='root', password='123456', database='py', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 执行sql 增加
    count = cursor.execute("""insert into jd(name) values("键盘")""")
    # 更新
    # 删除

    # 受影响的函数
    print(count)

    # 提交所有的操作事务
    conn.commit()
    # 回滚
    # conn.rollback()

    # 关闭链接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
