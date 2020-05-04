'''
子系统自身信息：
IP:192.168.127.10
slave：10
port:5001

子系统需要检测的信息
电源电压采样 value1:10 03 07 02  data crc1 crc2----registerid=07   datatype=int
电源电流采样 value1:10 03 08 04 data crc1 crc2----registerid=08   datatype=float

'''


import zmq
import struct
import threading
import pymysql
import datetime
import crcmod
import time

import socket
import  struct

def processerfuc(context,url,sync_addr,exp_id_server,topic,exp_id):
    expid_url = "tcp://127.0.0.1:6005"#虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
    reveiver_url = "ipc://10_Router"


    expid_sub = context.socket(zmq.SUB)
    # socket_sub_sub.set_hwm(100000)
    expid_sub.connect(expid_url)
    expid_sub.setsockopt(zmq.SUBSCRIBE,topic)
    #
    expid_sub.setsockopt(zmq.SUBSCRIBE,b'expid')

    receiver_dealer = context.socket(zmq.DEALER)
    # sock_et_sub_sub.set_hwm(100000)
    receiver_dealer.setsockopt(zmq.IDENTITY, b'10')
    receiver_dealer.set_hwm(10000000)
    receiver_dealer.bind(reveiver_url)



    # # Second, synchronize with publisher
    # syncclient = context.socket(zmq.REQ)
    # syncclient.connect(sync_addr)
    #
    # # send a synchronization request
    # syncclient.send(b'')
    #
    # # wait for synchronization reply
    # syncclient.recv()

    # num_package= 0
    # db = pymysql.connect(host='localhost', user='scottar', password='123456', db='nis_hsdd', port=3306, charset='utf8')
    # cur = db.cursor()

    #方案2
    #实验批次id
    # sock_exp_id=context.socket(zmq.SUB)
    # sock_exp_id.setsockopt()
    # sock_exp_id.connect(exp_id_server)

    #process monitoring
    sock_monitor_url = "tcp://127.0.0.1:8010"
    sock_process_monitor=context.socket(zmq.REP)
    sock_process_monitor.connect(sock_monitor_url)

    # # Initialize poll set
    poller = zmq.Poller()
    poller.register(expid_sub, zmq.POLLIN)
    poller.register(receiver_dealer,zmq.POLLIN)
    poller.register(sock_process_monitor, zmq.POLLIN)
    counter= 0
    while True:
        socks = dict(poller.poll())

        if socks.get(sock_process_monitor) == zmq.POLLIN:
            print(sock_process_monitor.recv())
            sock_process_monitor.send(b'I am alive  ' + sock_monitor_url.encode())



        if socks.get(expid_sub) == zmq.POLLIN:

            # 接收xpub的资料，其中已经经过了子系统的筛选
            b = expid_sub.recv()
            print('msg we receive',b)
            if b[0:5] == b'expid': #注意实验id的分发
                exp_id = struct.unpack('!f', b[5:9])[0]
                print(exp_id)
                continue
        if socks.get(receiver_dealer) == zmq.POLLIN:
            b = receiver_dealer.recv()
            #判断当前是否直接达到了stop的那个按钮的情况
            if b[4] == 115:
                break
            counter += 1
            print("Counter num:",counter)

            #这一层主要是对哪一个寄存器进行筛选(筛选规则是否需要变化，我们应当根据每一个寄存器当初要发出的每一个寄存器的个数来决定)
            # if True :
            #     # print(len(b))
            #     if len(b)==36:
            #         if b[4] == 115:
            #             break
            #         num_package  = num_package + 1
            #         # print(num_package)
            #
            #         subsys_id,func,register_id,length,v_data=struct.unpack('!bbbbf',b[0:8])
            #         data_time=b[10:36]
            #         sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,%d,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (subsys_id,register_id,exp_id,v_data,str(data_time,encoding='utf-8'))
            #         cur.execute(sql)
            #     elif len(b)==46:
            #         print('处理的粘包的问题')
            #         if b[17] == 115:
            #             print('粘包的情况的最后的一个包',b)
            #             break
            #         num_package = num_package + 1
            #         subsys_id, func, register_id, length, v_data = struct.unpack('!bbbbf', b[10:18])
            #         # data_time = b[20:46]
            #         # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,1,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (
            #         # subsys_id, register_id, v_data, str(data_time, encoding='utf-8'))
            #         # cur.execute(sql)
            #     else:
            #         print('b长度:',len(b))
            #         print(b)
            #         break
            #
            #
            #
            #     # print(b)
            #
            # db.commit()
            # print('订阅的是: ',topic,'收到的包的数量: ', num_package)


if __name__ == '__main__':

    #zeroMQ的通信协议可以采用的ipc
    context = zmq.Context()
    import threading





    # url = "tcp://127.0.0.1:6005"
    url = "ipc://main"  #虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
    #而如果是inproc 则是在线程间寻找inproc 对应的协议，很有可能就没有这样的协议

    sync_addr = 'ipc://main_sync_server'

    exp_id_server='ipc://exp_id_server'

    import threading
    #这个时候定义一个需要订阅子系统
    main_content=b'\x03\03'   #目前这个用来订阅各个子系统的内容，然后内部对数据进行分析
    # main_content=b''sub

    #这个定义了这个系统包含了哪些寄存器
    # sub_content = [struct.pack('!b',1),struct.pack('!b',2),struct.pack('!b',3),struct.pack('!b',4),struct.pack('!b',5),struct.pack('!b',6),struct.pack('!b',7),struct.pack('!b',8),struct.pack('!b',9),struct.pack('!b',10)]
    sub_content = [struct.pack('!b',12),struct.pack('!b',13)]   #12 和 13 分别对应0b  和 0c
    #传入一个第几次实验的参数  #默认认为是第0次实验
    exp_id = 0
    #启动该进程对该子系统中的数据进行处理
    processerfuc(context,url,sync_addr,exp_id_server,sub_content[1],exp_id)


    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''



