'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=float
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''

IP_Server='192.168.127.11'
Port = 5001

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
    if length!=4:
        a = struct.pack('!bbbbh', slave, func, register, length, data)  #h 代表的是short
        # print(len(a))
        b=struct.pack('H',crccreate(a[0:8], length=8))
        a=a + b
    else:
        # print('data',data)
        a = struct.pack('!bbbbf', slave, func, register, length, data)
        # print(len(a))
        b=struct.pack('H',crccreate(a[0:8], length=8))
        a=a + b
        # print(a)
    return a

if __name__=='__main__':
    #需要绑定的地址
    exp_id_server="tcp://115.156.162.76:6000"
    # exp_id_server="ipc://sub_server_proxy"


    #zeromq experiment part
    import zmq
    context = zmq.Context()
    socketzmqpub = context.socket(zmq.PUB)
    socketzmqpub.connect(exp_id_server)

    # #tcp 连接
    # tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    # tcp_server_socket.bind(('192.168.127.101',5003))#绑定本机地址和接收端口
    # tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    # tcp_server_socket.listen(1)#监听（）内为最大监听值
    # client_socket,client_addr= tcp_server_socket.accept()#建立连接（accept（无参数）

    print('Some one has connected to me!')
    start_time = time.perf_counter()
    slave = 17
    func = 3





    while  True:
        # msg = client_socket.recv(100);
        # print(msg)

        # subsys_id,func,register_id,length,v_data=struct.unpack('!bbbbf',msg[0:8])
        v_data = 123
        time.sleep(1)
        print('v_data 是多少?',v_data)
        #可以每次系统改变,都重启一次数据解析的脚本,如何异步不阻塞的对多个不同的客户端进行
        socketzmqpub.send(b'expid'+struct.pack('!f',v_data))





