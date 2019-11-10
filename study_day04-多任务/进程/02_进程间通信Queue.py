"""
进程是相互隔离的资源，所以通信的方式需要借助Queue队列完成

    关于Queue的使用

"""
import multiprocessing


def download_from_web(q):
    data = [11, 22, 33]

    for temp in data:
        q.put(temp)

    print("下载器已经将数据下载完成")


def analysis_data(q):
    waitting = list()
    # 从队列中取出数据
    while True:
        if q.empty():
            break

        data = q.get()
        waitting.append(data)

    print(waitting)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()

    # 创建多个进程，将队列的引用当作参数传递到进程中
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

