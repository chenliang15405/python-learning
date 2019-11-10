"""
创建线程的方式有两种：
    先倒入 threading 包
    1. 直接创建线程对象，然后调用start()方法, target中指定的是方法名称
    thread1 = threading.Thread(target=test1)

    如果需要传递参数，那么可以通过args传递参数，在该方法中的参数列表中接收
    传入的参数方式是元组，那么一个参数的情况下，后面需要带个,
    thread1 = threading.Thread(target=test1, args=(变量))



    2. 通过继承Thread类创建线程
    (1) 定义线程类，重写run方法
    class MyThread(threading.Thread):
        def run(self):
            for i in range(3):
                print("这是创建的线程 %d" % i)

    (2) 然后创建该对象，调用start()方法
    t = MyThread()
    t.start()

"""
import threading

# 通过继承创建对象
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("这是创建的线程 %d" % i)


t = MyThread()
t.start()


# 直接创建线程
def test1():
    print("直接创建线程-----")


def main():
    thread1 = threading.Thread(target=test1)
    thread1.start()

main()