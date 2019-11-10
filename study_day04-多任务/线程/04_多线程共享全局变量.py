"""
多线程共享全局变量,
只要有一个线程中修改了全局变量，那么其他线程是共享的

"""
import threading
import time


g_num = 100                  


def test1():
    global g_num
    g_num += 1

    print("----test1------ %d" % g_num)


def test2(temp):
    temp.append(33)
    print("----test2------ %d" % g_num)


g_nums = [11, 22]


def main():
    thread1 = threading.Thread(target=test1)
    thread2 = threading.Thread(target=test2, args=(g_nums,))  # 如果传入的方式是元组，那么一个参数的情况下，后面需要带个,
    thread1.start()
    time.sleep(1)

    thread2.start()
    time.sleep(1)

    print("------main------ %d ------ %s" % (g_num, str(g_nums)))


if __name__ == '__main__':
    main()
