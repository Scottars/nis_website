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



def floatToBytes(f):
    bs = struct.pack("!f",f)
    return (hex(bs[3]),hex(bs[2]),hex(bs[1]),hex(bs[0]))
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


    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    tcp_server_socket.bind(('115.156.163.107',5001))#绑定本机地址和接收端口
    tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    tcp_server_socket.listen(1)#监听（）内为最大监听值
    client_socket,client_addr= tcp_server_socket.accept()#建立连接（accept（无参数）

    print('Some one has connected to me!')

    msg=b'sdfasfdfdb'
    msg=b'\x05\x03\x01\x04?\x99\x99\x9au%'
    # print(msg)
    start_time = time.perf_counter()
    slave = 5

    for j in range(1000):
        func = 3
        register = 1
        length = 4
        data = 12.5

        j=j+0.1

        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。

        # 每次最多接收1k字节:
        high_pricision_delay(0.0001)
        # print(msg)
        # time.sleep(0.0001)
        client_socket.send(msg)
        j=j+0.1
        func = 3
        register = 2
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 3
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 4
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 5
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 6
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 7
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)
        j=j+0.1
        func = 3
        register = 8
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        j=j+0.1
        func = 3
        register = 9
        length = 4
        msg = get_send_msgflowbytes(slave, func, register, length, j)  # 实际上，这个函数花费了不少的时间。
        high_pricision_delay(0.0001)
        client_socket.send(msg)

        # client_socket.recv(1)
        # client_socket.recv(20)
    time.sleep(0.001)
    msg = struct.pack('!b',slave)+b'\x03' + struct.pack('!b', register) + b'sssssss'
    print(len(msg))
    client_socket.send(msg)
    end_time = time.perf_counter()
    print('发送时间耗费',end_time-start_time)
# tcp_server_socket.close()