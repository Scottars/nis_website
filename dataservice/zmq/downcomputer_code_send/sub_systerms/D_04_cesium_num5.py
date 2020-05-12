'''
子系统自身信息：
IP:192.168.127.4
slave：04
port:5001

子系统需要检测的信息   -10Hz  采集的是温度
加热温度采集1 value1:04 03 13 04  data crc1  crc2  ----registerid=13   datatype=float
加热温度采集2 value1:04 03 14 04  data crc1  crc2  ----registerid=14   datatype=float
加热温度采集3 value1:04 03 15 04  data crc1  crc2  ----registerid=15   datatype=float
加热温度采集4 value1:04 03 16 04  data crc1  crc2  ----registerid=16   datatype=float
加热温度采集5 value1:04 03 17 04  data crc1  crc2  ----registerid=17   datatype=float

'''
IP_Server='192.168.127.4'
IP_Server='115.156.162.123' #测试的时候本电脑使用的IP
IP_Server='127.0.0.1' #测试的时候本电脑使用的IP
# IP_Server='192.168.127.100' #测试

Port = 5004
#当前未采用
# url = ('115.156.163.107', 5003)

#upload speed
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


    print("we have run 04")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接,这个建立的是tcp的链接
    client_socket.connect((IP_Server,Port))

    print('Some one has connected to me!')
    start_time = time.perf_counter()
    slave = 4
    func = 3


    msg = b'startstart'

    client_socket.send(msg)

    for j in range(10):
        '''
        子系统需要检测的信息
        加热温度采集1 value1:04 03 13 04  data crc1  crc2  ----registerid=13   datatype=float
        加热温度采集2 value1:04 03 14 04  data crc1  crc2  ----registerid=14   datatype=float
        加热温度采集3 value1:04 03 15 04  data crc1  crc2  ----registerid=15   datatype=float
        加热温度采集4 value1:04 03 16 04  data crc1  crc2  ----registerid=16   datatype=float
        加热温度采集5 value1:04 03 17 04  data crc1  crc2  ----registerid=17   datatype=float
        '''

        time.sleep(Time_interal)

        register = 19  ###对应0x13
        length = 4
        data = slave + 0.1 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time


        register = 20  ###对应0x14
        length = 4
        data = slave + 0.2 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)

        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time


        register = 21  ###对应0x15
        length = 4
        data = slave + 0.3 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)

        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time


        register = 22  ###对应0x16
        length = 4
        data = slave + 0.4 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # time.sleep(0.0001)

    # high_pricision_delay(0.0001)
        client_socket.send(msg)
        time.sleep(Time_interal)   #The sample interval time

        register = 23  ###对应0x17
        length = 4
        data = slave + 0.5 + j
        msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # high_pricision_delay(0.0001)
        # time.sleep(0.0001)

        client_socket.send(msg)

    time.sleep(0.0001)

    #发送停止数据信号
    msg = b'stopstopst'

# msg = struct.pack('!b',slave)+b'\x03' +  b'stopssss'
    client_socket.send(msg)
    print('Package nums: 1 000')
    print('Sending Speed: 0.01k/s')
    print('Sending Port: ', Port)
    end_time = time.perf_counter()
    print('Sending Time Cost: ',end_time-start_time)
    client_socket.close()
