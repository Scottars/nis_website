'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=float
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''

import pymysql
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
    # exp_id_server="tcp://115.156.162.76:6000"
    exp_id_server="tcp://127.0.0.1:4002"

    # exp_id_server="ipc://sub_server_proxy"


    #zeromq experiment part
    import zmq
    context = zmq.Context()
    socketzmqpub = context.socket(zmq.PUB)
    socketzmqpub.bind(exp_id_server)    #系统分发id，各个子系统，都将练习商去

    # #tcp 连接,用于接收时序系统发过来的最新的id。
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    tcp_server_socket.bind(('127.0.0.1',4001))#绑定本机地址和接收端口
    tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    tcp_server_socket.listen(1)#监听（）内为最大监听值
    client_socket,client_addr= tcp_server_socket.accept()#建立连接（accept（无参数）

    print('Some one has connected to me!')

    # num_package= 0
    db = pymysql.connect(host='localhost', user='scottar', password='123456', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()

    #各个子系统也应当具有这个实验id 的校验的环节，就自己查询后的结果，以及pub分发后的id

    start_flag = False

    print("we have connected to this ")
    while  True:
        # msg = client_socket.recv(100);
        # print(msg)
        #系统逻辑: 接收来自时序系统的信号。
        try:
            b = client_socket.recv(10)
            print("reveiver:",b)
        except:
            client_socket.close()  # 等待后续的连接
            # print('we are receiving ', b)

            # print(b)
            # print(b)
            # b[0 1 2 3 ] b[4]
        if b[0:4] == b'stop':  # 停止指令的接收

            print('we are ready to exit')
            socketzmqpub.send(b)
            break

        elif b[0:5] == b'start':  ## 我们开始分发这次实验的id
            print('we have received the start')
            start_flag = True
            continue

        if start_flag:
            #查询数据库中最新的实验id
            sql = "SELECT max(subsys_id) FROM v_data_monitor"
            cur.execute(sql)
            # print('cur',cur.fetchall())
            idcur=cur.fetchall()[0][0]
            # print('-----',idcur[0][0])


            #将最新的实验id分发下去；
            # socketzmqpub.send(b)
            socketzmqpub.send(b'expid'+struct.pack('I',idcur+1))





