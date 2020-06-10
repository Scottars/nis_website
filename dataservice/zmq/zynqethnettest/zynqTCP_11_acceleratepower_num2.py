'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=float
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''

import threading
import zmq
import time
import socket
import datetime
import struct
HWM_VAL = 100000*60*31*5

HWM_VAL = 100000


def zmq_recv(context, url):
    socket = context.socket(zmq.SUB)
    # socket = context.socket(zmq.REP)
    socket.connect(url)
    socket.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))  # 接收所有消息

    zhanbao = 0
    buzhanbao = 0
    start_time = time.clock()
    while True:
        b = socket.recv();
        # socket.send(b'1')
        # print(b)

        end_time = time.clock()
        if len(b) == 1:
            # print('总计耗时',end_time-start_time)
            break

        size = len(b)
        # print(size)

        # if end_time-start_time > 10:
        #     pass
        #     break
        if size > 10:
            zhanbao = zhanbao + 1

        else:
            buzhanbao = buzhanbao + 1

    print('接收不粘包', buzhanbao)
    print('接收粘包', zhanbao)

def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds
    """
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)
    return sock


def tcp_recv_zmq_send(context, sub_server_addr, syncaddr, down_computer_addr, port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")
    reveiver_url = "ipc://11_Router"

    socketzmq = context.socket(zmq.ROUTER)
    socketzmq.set_hwm(HWM_VAL)

    # socketzmq.connect(reveiver_url)

    sendinglist=[]

    # client = context.socket(zmq.ROUTER)


    # 为了定义一个对象线程
    # 创建一个socket:
    # tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    # tcp_server_socket.bind((down_computer_addr,port))#绑定本机地址和接收端口
    # tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    # tcp_server_socket.listen(1)#监听（）内为最大监听值
    # # tcp_server_socket = set_keepalive_linux(tcp_server_socket)
    #
    # s,s_addr= tcp_server_socket.accept()#建立连接（accept（无参数）
    # s = set_keepalive_linuZZ8888888888888888888888;Bx(s)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接,这个建立的是tcp的链接
    # client_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    IP_Server='192.168.127.202'
    Port=5011
    client_socket.connect((IP_Server,Port))





    # s.connect(('192.168.127.5', 5001))
    print('we have connected to the tcp data send server!---port is :', port)

    packagenum = 0

    zhanbao = 0
    buzhanbao = 0
    start_time_perf = time.perf_counter()
    start_time_process = time.process_time()
    count = 0
    # 实际上应当启用的市多线程来做这些事情的
    # 每一个线程要做的事情就是接收对应的内容
    # 我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
    start_flag = True
    while True:

        # try:  #许久没有接收到下位机来的消息，首先会有一个keep  alive 的数据包的出现，如果太久没有了就直接关闭当前socket
        flag= epics的消息
        hertbeat
        ## 方案
        epics 发给信息给一个总控单元，由总控单元发消息给第二层的所有的接收模块

        if flagrece:
            b = client_socket.recv(10) #收下位机的信息
            print('I',count)

            if count==1000000:
                break
            # size = len(b)
            count = count + 1
            # timestample = str(datetime.datetime.now()).encode()
            # b = b + timestample
        else:


            # sendinglist.append(b)

    # print('Sending list size ',len(sendinglist))

    print(packagenum)
    end_time_perf = time.perf_counter()
    end_time_process = time.process_time()
    print('Receiving port is: ', port)
    print('Package num:', count)
    print('receing time cost:', end_time_perf - start_time_perf)  #
    # print('tcp接收不粘包', buzhanbao)
    # print('tcp接收粘包', zhanbao)

    # socketzmq.send(b)


    socketzmq.close()

    s.close()
    tcp_server_socket.close()



if __name__ == '__main__':
    print('Kaishile ')
    context = zmq.Context()  # 这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚
    sub_server_addr = "tcp://115.156.162.123:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.163.107'
    # down_computer_addr = '127.0.0.1'
    down_computer_addr = '192.168.127.11'
    down_computer_addr = '192.168.127.100'

    down_computer_addr = '127.0.0.1'

    # sub_server_addr = "tcp://127.0.0.1:6001"
    sub_server_addr = "tcp://192.168.127.100:6002"


    # syncaddr = "tcp://127.0.0.1:5555"
    syncaddr = "tcp://192.168.127.100:5556"



    port = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010]

    tcp_recv_zmq_send(context,sub_server_addr,syncaddr,down_computer_addr,5011)
    # for i in port:
    #     t2 = threading.Thread(target=tcp_recv_zmq_send,
    #                           args=(context, sub_server_addr, syncaddr, down_computer_addr, port))
    #     t2.start()
