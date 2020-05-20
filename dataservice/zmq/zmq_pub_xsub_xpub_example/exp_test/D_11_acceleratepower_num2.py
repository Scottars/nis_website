'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息     上传速度100k/s
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=float
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''

IP_Server='192.168.127.11'
IP_Server='115.156.162.123' #测试的时候本电脑使用的IP
IP_Server='127.0.0.1' #测试的时候本电脑使用的IP
# IP_Server='192.168.127.100' #测试

Port = 5011
#当前未采用
url = ('115.156.163.107', 5001)


#upload speed
Time_interal=0.00001   #100 k/s

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


def get_send_msgflowbytes(slave,func,register,length,data):
    if length == 2:
        a = struct.pack('!bbbbh', slave, func, register, length, data)  #h 代表的是short
        # print(len(a))
        b=struct.pack('H',crccreate(a[0:6], length=6))
        a=a + b + b'xx'
    elif length==4:
        # print('data',data)
        a = struct.pack('!bbbbf', slave, func, register, length, data)
        # print(len(a))
        b=struct.pack('H',crccreate(a[0:8], length=8))
        a=a + b
            # print(a)
    return a

if __name__=='__main__':

    print("we have run 11")


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接,这个建立的是tcp的链接
    client_socket.connect((IP_Server,Port))


    print('we have connected to the server!')
    start_time = time.perf_counter()
    slave = 17
    func = 3
    #临时的
    register = 7
    length = 4
    data = slave + 0.1
    msg = b'startstart'
    client_socket.send(msg)
    msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。

    for j in range(1000000):
        '''
          子系统需要检测的信息   采集速度1Mhz
        电源电压采样 value1:10 03 07 04  data crc1  crc2  ----registerid=07   datatype=float
        电源电流采样 value1:10 03 08 04  data crc1  crc2  ----registerid=08   datatype=float
        '''

        # time.sleep((Time_interal))
        high_pricision_delay(Time_interal)

        #
        # register = 7
        # length = 4
        # data = slave + 0.1 + j
        # msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # 每次最多接收1k字节:
        # high_pricision_delay(0.000001)
        # time.sleep(0.0001)
        client_socket.send(msg)

        #
        # register = 8
        # length = 4
        # data = slave + 0.2 + j
        # msg = get_send_msgflowbytes(slave, func, register, length, data)  # 实际上，这个函数花费了不少的时间。
        # # high_pricision_delay(0.000001)
        # client_socket.send(msg)



    time.sleep(0.001)

    #发送停止数据信号
    msg = b'stopstopst'
    client_socket.send(msg)

    print('Package nums: 1 000')
    print('Sending Speed: 100k/s')
    print('Sending Port: ', Port)
    end_time = time.perf_counter()
    print('Sending Time Cost: ',end_time-start_time)
    client_socket.close()


