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
    sub_server_addr = "tcp://115.156.162.123:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.163.107'
    down_computer_addr = '127.0.0.1'
    sub_server_addr = "tcp://192.168.127.100:6001"
    syncaddr = "tcp://127.0.0.1:5555"
    # sub_server_addr = "tcp://127.0.0.1:6001"

    port = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010]

    dealerserver="tcp://127.0.0.1:9000"
    dealerpart = context.socket(zmq.ROUTER)
    # dealerpart.setsockopt(zmq.IDENTITY, b'sub')

    dealerpart.bind(dealerserver)

    #we need know that whether or not you have fininshed the data receive.

    # # Initialize poll set
    poller = zmq.Poller()
    poller.register(dealerpart, zmq.POLLIN)
    #The queue to send the data to the proxy
    Data_send_list=[]
    Done_list = []
    flag = False #This is the flag we have send the all data
    while True:
        socks = dict(poller.poll())
        if socks.get(dealerpart) == zmq.POLLIN:
            id,kong,neirong= dealerpart.recv_multipart()
            print('id',id)
            print('kong',kong)
            print('neirong',neirong)
            dealerpart.send_multipart([b'A',b'',b"This is frow server"])

