"""
使用多任务实现多线程同时执行

"""
import threading
import time


def main():
    print("这是一个线程的运行")
    time.sleep(2)


def b():
    print("b函数执行")
    time.sleep(1)


if __name__ == '__main__':
    # 多线程运行
    for i in range(5):
        thread = threading.Thread(target=main)
        thread1 = threading.Thread(target=b)
        thread.start()
        thread1.start()
