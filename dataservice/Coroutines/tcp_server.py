from gevent import monkey,spawn;monkey.patch_all()
from threading import Thread
from socket import *

def talk(conn):    #跟建好的连接进行通讯
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip,port,backlog=5):
    s = socket()
    s.bind((ip,port))
    s.listen(backlog)
    print('已经越过了backlog')

    while True:
        conn, addr = s.accept()   #建连接
        print('addr',addr)
        print(addr)

        # 通信
        g=spawn(talk,conn)     #提交一个协程任务，进行通讯。在多个客户端之间来回切换
                             #切的速度非常快，多个客户端都得到及时响应

    s.close()

if __name__ == '__main__':
    spawn(server,'127.0.0.1',8080).join()
    # server(('127.0.0.1',8080))   #和上面一步效果相同



'''
既然python 中存在了单核多线程的这种特点，并没有完全能利用到多线程的优势的话

#我们不如就仅仅采用协程的方案呢？？？？？？？
#如果是这样子的话，我们不如就在python脚本中采用协程方案，这样我们基本不存在消耗切换资源的情况，是否会更快


或者可以采取其他的语言尽量努力得去采用多线程的多核的方案


1、下位机的模拟的方案：
    是否也应当选用多线程多核的解决方案
    
2、上位机的第一部分的tcp接收的部分可以用多线程多核的方案
    但是用zeromq的时候，实际上，还是要进入到单线程的解决方案当中去






'''
