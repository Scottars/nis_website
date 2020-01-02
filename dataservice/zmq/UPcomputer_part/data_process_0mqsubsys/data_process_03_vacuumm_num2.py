'''
子系统自身信息：
IP:192.168.127.3
slave：03
port:5001

子系统需要检测的信息
Vacuum value1:03 03 0b 04  data crc1  crc2  ----registerid=0b   datatype=float
Vacuum value2:03 03 0c 04  data crc1  crc2  ----registerid=0c   datatype=float
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



def subscriber(context,url,sync_addr,exp_id_server,topic,exp_id):
    socket_sub_sub = context.socket(zmq.SUB)
    socket_sub_sub.connect(url)
    # topic=b''
    socket_sub_sub.setsockopt(zmq.SUBSCRIBE,b'')
    socket_sub_sub.setsockopt(zmq.SUBSCRIBE,b'expid')

    # Second, synchronize with publisher
    syncclient = context.socket(zmq.REQ)
    syncclient.connect(sync_addr)

    # send a synchronization request
    syncclient.send(b'')

    # wait for synchronization reply
    syncclient.recv()

    num_package= 0
    db = pymysql.connect(host='localhost', user='scottar', password='wangsai', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()

    #方案2
    #实验批次id
    # sock_exp_id=context.socket(zmq.SUB)
    # sock_exp_id.setsockopt()
    # sock_exp_id.connect(exp_id_server)
    #
    # # Initialize poll set
    # poller = zmq.Poller()
    # poller.register(socket_sub_sub, zmq.POLLIN)
    # poller.register(sock_exp_id, zmq.POLLIN)

    while True:


        # if socks.get(socket_sub_sub) == zmq.POLLIN:

        # 接收xpub的资料，其中已经经过了子系统的筛选
        b = socket_sub_sub.recv()
        if b[0:5] == b'expid':
            exp_id = struct.unpack('!f', b[5:9])[0]
            print(exp_id)
        # print(b)
        # print(len(b))
        #
        # # print('b[4]是多少,',b[4])
        #判断当前是否直接达到了stop的那个按钮的情况
        if b[4] == 115:
            break
        #这一层主要是对哪一个寄存器进行筛选(筛选规则是否需要变化，我们应当根据每一个寄存器当初要发出的每一个寄存器的个数来决定)
        if True :
         # print(len(b))
            if len(b)==36:
                if b[4] == 115:
                    break
                num_package  = num_package + 1
                # print(num_package)

                subsys_id,func,register_id,length,v_data=struct.unpack('!bbbbf',b[0:8])
                data_time=b[10:36]
                sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,%d,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (subsys_id,register_id,exp_id,v_data,str(data_time,encoding='utf-8'))
                cur.execute(sql)
            elif len(b)==46:
                print('处理的粘包的问题')
                if b[17] == 115:
                    print('粘包的情况的最后的一个包',b)
                    break
                num_package = num_package + 1
                subsys_id, func, register_id, length, v_data = struct.unpack('!bbbbf', b[10:18])
                # data_time = b[20:46]
                # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,1,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (
                # subsys_id, register_id, v_data, str(data_time, encoding='utf-8'))
                # cur.execute(sql)
            else:
                print('b长度:',len(b))
                print(b)
                break



            # print(b)

    db.commit()
    print('订阅的是: ',topic,'收到的包的数量: ', num_package)


if __name__ == '__main__':

    #zeroMQ的通信协议可以采用的ipc
    context = zmq.Context()
    # url = "tcp://127.0.0.1:6005"
    url = "ipc://main"  #虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
                        #而如果是inproc 则是在线程间寻找inproc 对应的协议，很有可能就没有这样的协议

    sync_addr = 'ipc://main_sync_server'

    exp_id_server='ipc://exp_id_server'

    import threading
    #这个时候定义一个需要订阅子系统
    # main_content=b'\x05'   #目前这个用来订阅各个子系统的内容，然后内部对数据进行分析
    # main_content=b''sub

    #这个定义了这个系统包含了哪些寄存器
    sub_content = [struct.pack('!b',1),struct.pack('!b',2),struct.pack('!b',3),struct.pack('!b',4),struct.pack('!b',5),struct.pack('!b',6),struct.pack('!b',7),struct.pack('!b',8),struct.pack('!b',9),struct.pack('!b',10)]
    # sub_content = [struct.pack('!b',1),struct.pack('!b',2),struct.pack('!b',6)]
    #传入一个第几次实验的参数  #默认认为是第0次实验
    exp_id = 0
    #启动该进程对该子系统中的数据进行处理
    subscriber(context,url,sync_addr,exp_id_server,sub_content[2],exp_id)
    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''
