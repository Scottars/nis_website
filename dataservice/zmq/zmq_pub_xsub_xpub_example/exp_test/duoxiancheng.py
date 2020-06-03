'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=int
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

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

def floatToBytes(f):
    bs = struct.pack("f",f)
    return (bs[3],bs[2],bs[1],bs[0])
def bytesToFloat(h1,h2,h3,h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f",ba)[0]
def bytesToHex(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return hex(struct.unpack("=H", ba)[0])
#注意这个地方的解包的地方H 与 h 的关系

def bytesToInt(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return struct.unpack("=H", ba)[0]

def crccheckhole(b,length):
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)

    return hex(crc16_func(b[0:length]))==bytesToHex(b[length],b[length+1])
def crccheck(b,length):
    print('传过来的b，和lenght',b,'   ',length)
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
    return crc16_func(b[0:length]) == bytesToInt(b[length], b[length + 1])

def database_write_float(b):
    # data = bytesToFloat(b[4], b[5], b[6], b[7])
    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (
    # b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print(b[2])
    pass
#定义gas control 部分的测试
#01 1479A 流量计的数值， float
def Gas_Control_05_03_01(b):
    database_write_float(b)

#02 627D  气压计的数值 float
def Gas_Control_05_03_02(b):
    database_write_float(b)

    # print('register 02')

#03 CDG_025D 气压的数值  float
def Gas_Control_05_03_03(b):
    database_write_float(b)
    # print('register 03')
#04 供气阀门的状态16位，2个字节
def Gas_Control_05_03_04(b):
    pass
    # data = bytesToInt(b[4], b[5])
    #能够过去，肯定也就能够还原成1111 0000  1111 0000 的形式

    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print('register 04')

#14  读取当前是否处气压的 puff模式 1个字节0xff 0x00
def Gas_Control_05_03_14(b):
    data =b[4]
    # 能够过去，肯定也就能够还原成1111 0000  1111 0000 的形式
    #
    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (
    # b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print('register 14')
#15  读取真空度的设定值 float
def Gas_Control_05_03_15(b):
    database_write_float(b)
    # print('register 15')

##16 读取流量计的设定值 float
def Gas_Control_05_03_16(b):
    database_write_float(b)
    # print('register 16')
#17  读取puff模式下，气压设定值
def Gas_Control_05_03_17(b):
    database_write_float(b)
    # print('register 17')
#18   读取pid 三个参数设定值  p i d 3*float=12个字节
def Gas_Control_05_03_18(b):
    # print('register 18')
    pass
def register_case_03(x,b):
    cases={
        b'\x01': Gas_Control_05_03_01,
        b'\x02': Gas_Control_05_03_02,
        b'\x03': Gas_Control_05_03_03,
        b'\x04': Gas_Control_05_03_04,
        b'\x14': Gas_Control_05_03_14,
        b'\x15': Gas_Control_05_03_15,
        b'\x16': Gas_Control_05_03_16,
        b'\x17': Gas_Control_05_03_17,
        b'\x18': Gas_Control_05_03_18,
    }
    func=cases.get(x,None)
    return func(b)





def processerfuc(context,url,sync_addr,exp_id_server,topic,exp_id):
    expid_url = "tcp://127.0.0.1:6005"#虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
    reveiver_url = "inproc://11_Router"


    expid_sub = context.socket(zmq.SUB)
    # socket_sub_sub.set_hwm(100000)
    expid_sub.connect(expid_url)
    expid_sub.setsockopt(zmq.SUBSCRIBE,topic)
    #
    expid_sub.setsockopt(zmq.SUBSCRIBE,b'expid')

    receiver_dealer = context.socket(zmq.DEALER)
    # sock_et_sub_sub.set_hwm(100000)
    receiver_dealer.setsockopt(zmq.IDENTITY, b'11')
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

    num_package= 0
    db = pymysql.connect(host='localhost', user='scottar', password='123456', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()

    #方案2
    #实验批次id
    # sock_exp_id=context.socket(zmq.SUB)
    # sock_exp_id.setsockopt()
    # sock_exp_id.connect(exp_id_server)

    #process monitoring
    sock_monitor_url = "tcp://127.0.0.1:8011"
    sock_process_monitor=context.socket(zmq.REP)
    sock_process_monitor.connect(sock_monitor_url)

    # # Initialize poll set
    poller = zmq.Poller()
    poller.register(expid_sub, zmq.POLLIN)
    poller.register(receiver_dealer,zmq.POLLIN)
    poller.register(sock_process_monitor, zmq.POLLIN)
    counter= 0
    start_time = time.perf_counter()

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
            counter += 1
            if counter == 1:
                thetime = str(datetime.datetime.now()).encode()
                print('The first package received time in  data process time:',thetime)
            if counter == 1000000:
                thetime = str(datetime.datetime.now()).encode()
                print('The last package received time in  data process time:',thetime)

                break
            #这一层主要是对哪一个寄存器进行筛选(筛选规则是否需要变化，我们应当根据每一个寄存器当初要发出的每一个寄存器的个数来决定)

            # db.commit()
    end_time = time.perf_counter()
    print("Dealer receiving time cost:",end_time-start_time)

def tcp_recv_zmq_send(context, sub_server_addr, syncaddr, down_computer_addr, port):
        # socketzmq = context.socket(zmq.PUB)
        # socketzmq.bind("tcp://115.156.162.76:6000")
        reveiver_url = "inproc://11_Router"
        # reveiver_url = "tcp://192.168.127.200:5011"
        HWM_VAL = 1000000000

        print('herewe are ')

        socketzmq = context.socket(zmq.ROUTER)
        socketzmq.set_hwm(HWM_VAL)

        socketzmq.connect(reveiver_url)

        sendinglist=[]

        tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
        tcp_server_socket.bind((down_computer_addr,port))#绑定本机地址和接收端口
        tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
        tcp_server_socket.listen(1)#监听（）内为最大监听值
        # tcp_server_socket = set_keepalive_linux(tcp_server_socket)

        print('before accepts')
        s,s_addr= tcp_server_socket.accept()#建立连接（accept（无参数）
        # s.connect(('192.168.127.5', 5001))
        print('we have connected to the tcp data send server!---port is :', port)

        packagenum = 0


        start_time_perf = time.perf_counter()
        start_time_process = time.process_time()
        count = 0
        # 实际上应当启用的市多线程来做这些事情的
        # 每一个线程要做的事情就是接收对应的内容
        # 我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
        start_flag = True
        exp_id=10
        data_time = str(datetime.datetime.now()).encode()
        print("The first package in monitor program：",data_time)
        while True:

            # try:  #许久没有接收到下位机来的消息，首先会有一个keep  alive 的数据包的出现，如果太久没有了就直接关闭当前socket
            b = s.recv(10)
            count = count + 1
            data_time = str(datetime.datetime.now()).encode()
            b = b + data_time
            socketzmq.send_multipart([b'11',b])
            if count==1000000:
                print("The last package in monitor program:",data_time)
                break


        print(packagenum)
        end_time_perf = time.perf_counter()
        print('Receiving port is: ', port)
        print('Package num in monitor program:', count)
        print('Receiving time cost in monitor program:', end_time_perf - start_time_perf)  #


        socketzmq.close()

        s.close()
        tcp_server_socket.close()


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
    # processerfuc(context,url,sync_addr,exp_id_server,sub_content[1],exp_id)
    sub_server_addr = "tcp://192.168.127.100:6002"
    syncaddr = "tcp://192.168.127.100:5556"

    down_computer_addr = '192.168.127.201'

    t1 = threading.Thread(target=processerfuc,args=(context,url,sync_addr,exp_id_server,sub_content[1],exp_id))
    t2 = threading.Thread(target=tcp_recv_zmq_send,args=(context,sub_server_addr,syncaddr,down_computer_addr,5011))
    t1.start()
    t2.start()
    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''

