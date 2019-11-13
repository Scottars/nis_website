

import zmq


import time


def push__send(context,url):


    # context = zmq.Context()

    # Socket to send messages on
    sender = context.socket(zmq.PUSH)
    sender.bind(url)


    while True:
        time.sleep(1)
        print('发送程序的前面')

        sender.send(b'I am sender 1')
        print('非阻塞')

def pull_recv(context,url):
    # context = zmq.Context()

    # Socket to send messages on
    sender = context.socket(zmq.PULL)
    sender.connect(url)


    while True:
        time.sleep(1)
        print('接收程序的前面')

        sender.recv()
        print('非阻塞')






if __name__ =='__main__':
    import threading

    context = zmq.Context()
    url = "inproc://test2"  #要是要采用多线程，这个时候的context的上下文就要采用的是同一个上下文。
                            #如果采用的是不同的上下文，我们就可以采用的是不同的上下文ipc

    t1 = threading.Thread(target=push__send,args=(context,url))
    t2=threading.Thread(target=pull_recv,args=(context,url))
    t1.start()
    t2.start()
