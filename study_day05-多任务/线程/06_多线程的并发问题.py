"""
多线程同时修改一个变量，会出现并发问题


"""
import threading
import time

g_num = 100


def test1(temp):
    global g_num
    for i in range(temp):
        g_num += 1
    print("----test1------ %d" % g_num)


def test2(temp):
    global g_num
    for i in range(temp):
        g_num += 1
    print("----test1------ %d" % g_num)


def main():
    thread1 = threading.Thread(target=test1, args=(1000000,))
    thread2 = threading.Thread(target=test2, args=(1000000,))  # 如果传入的方式是元组，那么一个参数的情况下，后面需要带个,
    thread1.start()
    thread2.start()

    # 睡眠5秒，等待执行完成
    time.sleep(5)
    print("------main------ %d ------" % g_num)


if __name__ == '__main__':
    main()
