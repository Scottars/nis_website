'''
子系统自身信息：
IP:192.168.127.3
slave：02
port:5001

子系统需要检测的信息  10Hz
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
# IP_Server='192.168.127.100' #测试


Port = 5002
#当前未采用
url = ('115.156.163.107', 5001)

#time interval for upload speed
Time_interal=0.1

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
    print("we have run 02")


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接,这个建立的是tcp的链接
    client_socket.connect((IP_Server,Port))
    # s=set_keepalive_linux(s)


    print('Some one has connected to me!')
    start_time = time.perf_counter()
    slave = 2
    func = 3
    msg = b'startstart'
    client_socket.send(msg)

    for j in range(10):
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
        time.sleep(Time_interal)   #The sample interval time

        register = 1
        length = 4
        data = slave + 0.1 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time



        register = 2
        length = 4
        data = slave + 0.2 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)

        time.sleep(Time_interal)   #The sample interval time

        register = 3
        length = 4
        data = slave + 0.3 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time

        register = 4
        length = 4
        data = slave + 0.4 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time



        register = 5
        length = 4
        data = slave + 0.5 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


        register = 6
        length = 4
        data = slave + 0.6 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)

        time.sleep(Time_interal)   #The sample interval time


        register = 7
        length = 4
        data = slave + 0.7 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)

        time.sleep(Time_interal)   #The sample interval time

        register = 8
        length = 4
        data==slave+0.8 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time


        register = 9
        length = 4
        data = slave + 0.9 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time


        register = 10
        length = 4
        data = slave + 0 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)


    time.sleep(0.001)

    #发送停止数据信号
    msg = b'stopstopst'
    client_socket.send(msg)
    print('Package nums: 1 000')
    print('Sending Speed: 0.01k/s')
    print('Sending Port: ', Port)
    end_time = time.perf_counter()
    print('Sending Time Cost: ',end_time-start_time)
    client_socket.close()





