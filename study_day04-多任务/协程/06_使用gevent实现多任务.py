"""
协程还是使用一个线程，一个任务执行会中断去执行另一个，然后再回来继续执行， 协程的特点

通过yield关键字，让协程停止，然后执行其他的，然后触发之后再回来执行这个


"""
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()












