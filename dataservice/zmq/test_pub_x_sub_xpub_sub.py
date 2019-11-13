

import zmq
import zmq


import time


def push__send_1(url,id):
    context = zmq.Context()
    # Socket to send messages on
    sender = context.socket(zmq.PUB)
    sender.connect(url)


    while True:
        time.sleep(0.001)
        # print('发送程序的前面')

        sender.send(b'I am sender'+ str(id).encode())
        # print('非阻塞')

def push__send_2(url,id):
    context = zmq.Context()
    # Socket to send messages on
    sender = context.socket(zmq.PUB)
    sender.connect(url)


    while True:
        time.sleep(1)
        # print('发送程序的前面')

        sender.send(b'I am sender'+ str(id).encode())
        # print('非阻塞')

def pull_recv(context,url):
    # context = zmq.Context()

    # Socket to send messages on
    recver = context.socket(zmq.XSUB)

    recver.setsockopt(zmq.SUBSCRIBE,'',0)  # 接收所有消息
    recver.bind(url)


    while True:
        time.sleep(10)
        # print('接收程序的前面')

        msg = recver.recv()
        print('actual data',msg)
        # print('非阻塞')






if __name__ =='__main__':
    import threading

    # context = zmq.Context()
    url = "tcp://115.156.163.107:6000"  #要是要采用多线程，这个时候的context的上下文就要采用的是同一个上下文。
                            #如果采用的是不同的上下文，我们就可以采用的是不同的上下文ipc
    # for i  in range(100):
    #     id= i
    #
    #     t1 = threading.Thread(target=push__send,args=(url,id))
    #     t1.start()

    id=111
    t1 = threading.Thread(target=push__send_1,args=(url,id))
    t1.start()
    id=2222
    t2 = threading.Thread(target=push__send_2,args=(url,id))
    t2.start()

    # t2=threading.Thread(target=pull_recv,args=(context,url))
