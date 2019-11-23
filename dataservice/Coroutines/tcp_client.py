from threading import Thread,current_thread
from socket import *

import os

def client():
    client = socket()
    client.connect(('127.0.0.1', 8080))

    while True:
        data = '%s hello' % current_thread().name
        client.send(data.encode('utf-8'))
        res = client.recv(1024)
        print(res.decode('utf-8'))


if __name__ == '__main__':
    for i in range(1000):    #建500个线程连接服务端进行通信，相当于并发500个客户端
        t=Thread(target=client)
        t.start()
