from gevent import monkey
monkey.patch_all()  # 3 自动切换 - time.sleep() recv() accept() 时间/网络IO相关->非阻塞
import gevent
import time


def work(no):
    for i in range(5):
        print("work%s..." % no)
        time.sleep(1)   # gevent.sleep()

def main():
    # 1 创建协程 并且 启动  参数1表示入口 参数2....
    g1 = gevent.spawn(work, 1)
    g2 = gevent.spawn(work, 2)
    g3 = gevent.spawn(work, 3)

    # 2 等待任务执行完成
    # g1.join()
    # g2.join()
    # g3.join()
    # 阻塞等待所有协程执行完成    目的: 进程存活 协程才能执行
    gevent.joinall([g1,g2,g3])

if __name__ == '__main__':
    main()