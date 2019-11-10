"""
yield就是 让线程放弃当前执行的优先级，执行其他线程中的内容，然后再运行yield后的内容

并且yield是让函数变为生成器，通过next()来执行，无法直接调用

"""
import time


def task_1():
    while True:
        print("-----1-----")
        time.sleep(1)
        yield


def task_2():
    while True:
        print("-----2-----")
        time.sleep(1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()

    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()