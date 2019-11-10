"""
通过进程池创建进程

"""
import multiprocessing
import os, time, random


def main(msg):
    print("%s 开始执行，进程号为：%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)


# 创建进程池
p = multiprocessing.Pool(3)
# 通过进程池调用目标
for i in range(10):
    # 通过apply_async调用目标
    p.apply_async(main, (i,))

print("---start-----")
p.close()
p.join() # 等待进程池中的所有子进程执行完毕之后再真正关闭进程池，必须放在close之后
print("-----end-----")
