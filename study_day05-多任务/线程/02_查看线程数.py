"""
通过方法查询线程数

 只有通过调用threading创建出来的线程对象的start()方法才会创建线程

"""
import threading
import time


def test1():
    for i in range(5):
        print("-----test1----%d--------" % i)
        time.sleep(1)


def test2():
    for i in range(5):
        print("----test2-----%d--------" % i)
        time.sleep(1)


def main():
    thread1 = threading.Thread(target=test1)
    thread2 = threading.Thread(target=test2)
    thread1.start()
    thread2.start()

    while True:
        print(threading.enumerate())
        print("线程数量：%d" % len(threading.enumerate()))
        if len(threading.enumerate()) <= 1:
            break

        time.sleep(1)


if __name__ == '__main__':
    main()

