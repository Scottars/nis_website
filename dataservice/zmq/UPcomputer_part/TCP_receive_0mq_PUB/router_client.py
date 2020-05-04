
'''
子系统自身信息：
IP:192.168.127.3
slave：03
port:5001

子系统需要检测的信息
Vacuum value1:03 03 0b 04  data crc1  crc2  ----registerid=0b   datatype=float
Vacuum value2:03 03 0c 04  data crc1  crc2  ----registerid=0c   datatype=float
'''
import threading
import zmq
import time
import socket
import datetime


if __name__ == '__main__':
    context = zmq.Context()  # 这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚


    routerserver="tcp://127.0.0.1:9000"
    routerpart = context.socket(zmq.REQ)
    # routerpart.setsockopt(zmq.IDENTIFY)
    routerpart.setsockopt(zmq.IDENTITY, b'A')

    routerpart.connect(routerserver)

    #we need know that whether or not you have fininshed the data receive.


    while True:
        time.sleep(0.1)
        routerpart.send(b'hello world')
        # id ,kong ,msg = routerpart.recv_multipart()
        print(routerpart.recv_multipart())
        # print(msg)
        # print(routerpart.recv_multipart())




###测试--REQ 与 ROUTER 的测试流程是通过的.
###因此考虑协调需求,由于req是一个阻塞类的模型.各部分的子线程,都可以发送一个req , 然后等待这个主线程的响应
