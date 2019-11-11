

import zmq


import time


def push__send():


    context = zmq.Context()

    # Socket to send messages on
    sender = context.socket(zmq.PUSH)
    sender.bind("ipc://test2")


    while True:
        time.sleep(1)
        print('发送程序的前面')

        sender.send(b'I am sender 1')
        print('非阻塞')

def pull_recv():
    context = zmq.Context()

    # Socket to send messages on
    sender = context.socket(zmq.PULL)
    sender.connect("ipc://test2")


    while True:
        time.sleep(1)
        print('接收程序的前面')

        sender.recv()
        print('非阻塞')






if __name__ =='__main__':
    import threading
    t1 = threading.Thread(target=push__send)
    t2=threading.Thread(target=pull_recv)
    t1.start()
    t2.start()
