'''
子系统自身信息：
IP:192.168.127.3
slave：02
port:5003

子系统需要检测的信息  1k/s 的速度
Vacuum value1:02 03 01 04  data crc1  crc2  ----registerid=01   datatype=float
Vacuum value2:02 03 02 04  data crc1  crc2  ----registerid=02   datatype=float
Vacuum value1:02 03 03 04  data crc1  crc2  ----registerid=03   datatype=float
Vacuum value2:02 03 04 04  data crc1  crc2  ----registerid=04   datatype=float
Vacuum value1:02 03 05 04  data crc1  crc2  ----registerid=05   datatype=float
Vacuum value2:02 03 06 04  data crc1  crc2  ----registerid=06   datatype=float
Vacuum value1:02 03 07 04  data crc1  crc2  ----registerid=07   datatype=float
Vacuum value2:02 03 08 04  data crc1  crc2  ----registerid=08   datatype=float
Vacuum value1:02 03 09 04  data crc1  crc2  ----registerid=09   datatype=float
Vacuum value2:02 03 0a 04  data crc1  crc2  ----registerid=10   datatype=float

'''

IP_Server='192.168.127.3'
IP_Server='115.156.162.123' #测试的时候本电脑使用的IP
IP_Server='127.0.0.1' #测试的时候本电脑使用的IP

Port = 5002
#当前未采用
url = ('115.156.163.107', 5001)

import socket
import  time
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
# s.bind(('115.156.163.107', 6001))
import socket

import crcmod
import time

import socket
import  struct
def high_pricision_delay(delay_time):
    '''
    it is seconds
    :param delay_time:
    :return:

    '''
    _ = time.perf_counter_ns()+delay_time*1000000000
    while time.perf_counter_ns() < _ :
        pass

def crccreate(b,length):
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
    return crc16_func(b[0:length])
def crccheckhole(b,length):
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)

    return hex(crc16_func(b[0:length]))==bytesToHex(b[length],b[length+1])
def crccheck(b,length):
    print('传过来的b，和lenght',b,'   ',length)
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
    return crc16_func(b[0:length]) == bytesToInt(b[length], b[length + 1])

def get_send_msgflowbytes(slave,func,register,length,data):
    if length!=4:
        pass
    else:
        # print('data',data)
        a = struct.pack('!bbbbf', slave, func, register, length, data)
        # print(len(a))
        b=struct.pack('H',crccreate(a[0:8], length=8))
        a=a + b
        # print(a)
    return a

if __name__=='__main__':
    #发布url


    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    tcp_server_socket.bind((IP_Server,Port))#绑定本机地址和接收端口
    tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    tcp_server_socket.listen(1)#监听（）内为最大监听值
    client_socket,client_addr= tcp_server_socket.accept()#建立连接（accept（无参数）

    print('Some one has connected to me!')
    start_time = time.perf_counter()
    slave = 2
    func = 3

    for j in range(1000):
        '''
        子系统需要检测的信息
        Vacuum value1:02 03 01 04  data crc1  crc2  ----registerid=01   datatype=float
        Vacuum value2:02 03 02 04  data crc1  crc2  ----registerid=02   datatype=float
        Vacuum value1:02 03 03 04  data crc1  crc2  ----registerid=03   datatype=float
        Vacuum value2:02 03 04 04  data crc1  crc2  ----registerid=04   datatype=float
        Vacuum value1:02 03 05 04  data crc1  crc2  ----registerid=05   datatype=float
        Vacuum value2:02 03 06 04  data crc1  crc2  ----registerid=06   datatype=float
        Vacuum value1:02 03 07 04  data crc1  crc2  ----registerid=07   datatype=float
        Vacuum value2:02 03 08 04  data crc1  crc2  ----registerid=08   datatype=float
        Vacuum value1:02 03 09 04  data crc1  crc2  ----registerid=09   datatype=float
        Vacuum value2:02 03 0a 04  data crc1  crc2  ----registerid=10   datatype=float
        '''
        time.sleep(5)

        register = 1
        length = 4
        data = slave + 0.1
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 2
        length = 4
        data = slave + 0.2
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 3
        length = 4
        data = slave + 0.3
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)

        register = 4
        length = 4
        data = slave + 0.4
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)



        register = 5
        length = 4
        data = slave + 0.5
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 6
        length = 4
        data = slave + 0.6
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)



        register = 7
        length = 4
        data = slave + 0.7
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 8
        length = 4
        data==slave+0.8
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 9
        length = 4
        data = slave + 0.9
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 10
        length = 4
        data = slave + 1.1
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


    time.sleep(0.001)

    #发送停止数据信号
    msg = struct.pack('!b',slave)+b'\x03' + struct.pack('!b', register) + b'sssssss'
    print(len(msg))
    client_socket.send(msg)
    end_time = time.perf_counter()
    print('发送时间耗费',end_time-start_time)
    tcp_server_socket.close()





