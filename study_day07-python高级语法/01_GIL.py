"""
GIL: 全局解释器锁

    就是说导致python中的多线程是假的多任务，在多线程的程序中，GIL导致每次只能有一个线程在运行
    每个线程在运行的时候都需要先获取GIL锁，保证同一时刻只能有一个线程运行

    多进程是可以利用多核CPU资源
    多线程运行还是会比但线程性能有提升，因为遇到IO阻塞的情况会自动给释放GIL锁，然后让其他的线程执行

怎么解决这个问题：使用c语言的python解释器即可

"""