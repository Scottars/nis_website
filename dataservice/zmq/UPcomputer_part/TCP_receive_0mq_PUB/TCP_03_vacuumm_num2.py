'''
子系统自身信息：
IP:192.168.127.3
slave：03
port:5001

子系统需要检测的信息
Vacuum value1:03 03 0b 04  data crc1  crc2  ----registerid=0b   datatype=float
Vacuum value2:03 03 0c 04  data crc1  crc2  ----registerid=0c   datatype=float
'''
import threading
import zmq
import time
import socket
import datetime

HWM_VAL = 100000*60*31*5
# HWM_VAL = 100000



def zmq_recv(context, url):
    socket = context.socket(zmq.SUB)

    # socket = context.socket(zmq.REP)
    socket.connect(url)
    socket.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))  # 接收所有消息

    zhanbao = 0
    buzhanbao = 0
    start_time = time.clock()
    while True:
        b = socket.recv();
        # socket.send(b'1')
        # print(b)

        end_time = time.clock()
        if len(b) == 1:
            # print('总计耗时',end_time-start_time)
            break

        size = len(b)
        # print(size)

        # if end_time-start_time > 10:
        #     pass
        #     break
        if size > 10:
            zhanbao = zhanbao + 1

        else:
            buzhanbao = buzhanbao + 1

    print('接收不粘包', buzhanbao)
    print('接收粘包', zhanbao)

def set_keepalive_linux(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds
    """
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)
    return sock


def tcp_recv_zmq_send(context, sub_server_addr, syncaddr, down_computer_addr, port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")
    reveiver_url = "ipc://03_Router"

    socketzmq = context.socket(zmq.ROUTER)
    socketzmq.set_hwm(HWM_VAL)

    socketzmq.connect(reveiver_url)

    sendinglist=[]

    # client = context.socket(zmq.ROUTER)



    # #
    # #为了等待远端的电脑的sub的内容全部都连接上来。进行的延迟
    # time.sleep(3)
    # # 保证同步的另r外的一种方案就是采用req-rep的同步
    # sync_client = context.socket(zmq.REQ)
    # sync_client.connect(syncaddr)
    # #
    # # 发送同步信号
    # sync_client.send(b'')
    #
    # # 等待同步回应,完成同步
    # sync_client.recv()

    # 为了定义一个对象线程
    # 创建一个socket:
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
    tcp_server_socket.bind((down_computer_addr,port))#绑定本机地址和接收端口
    tcp_server_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
    tcp_server_socket.listen(1)#监听（）内为最大监听值
    # tcp_server_socket = set_keepalive_linux(tcp_server_socket)

    s,s_addr= tcp_server_socket.accept()#建立连接（accept（无参数）
    s = set_keepalive_linux(s)

# s.connect(('192.168.127.5', 5001))
    print('we have connected to the tcp data send server!---port is :', port)

    packagenum = 0

    zhanbao = 0
    buzhanbao = 0
    start_time_perf = time.perf_counter()
    start_time_process = time.process_time()
    count = 0
    # 实际上应当启用的市多线程来做这些事情的
    # 每一个线程要做的事情就是接收对应的内容
    # 我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
    start_flag = False
    while True:

        try:
            b = s.recv(10)
        except:
            s.close()  #等待后续的连接
        # print('we are receiving ', b)

        # print(b)
        # print(b)
        if b[0:4]  == b'stop':  ##收到结束指令包
            print('we are ready to exit')
            socketzmq.send_multipart([b'03',b])
            break

        elif b[0:5] == b'start':  ## 收到开始指令
            print('we have received the start')
            start_flag= True
            continue

        if start_flag:
            size = len(b)
            count = count + 1
            timestample = str(datetime.datetime.now()).encode()
            b = b + timestample
            # sendcoststart=time.perf_counter()
            socketzmq.send_multipart([b'03',b]) #THhhis time cost is 4*10^-5  y大致约有40us
            # sendcostend=time.perf_counter()
            # print('Send Time Cost:',sendcostend - sendcoststart)
            # sendinglist.append(b)

    # print('Sending list size ',len(sendinglist))

    print(packagenum)
    end_time_perf = time.perf_counter()
    end_time_process = time.process_time()
    print('the port is: ', port)
    print('程序_process', end_time_process - start_time_process)  # process time 不包含time sleep 的
    print('程序执行perf_count', end_time_perf - start_time_perf)  #
    # print('tcp接收不粘包', buzhanbao)
    # print('tcp接收粘包', zhanbao)
    print('tcp接收包个数', count)

    # socketzmq.send(b)


    socketzmq.close()

    s.close()
    tcp_server_socket.close()




if __name__ == '__main__':
    print('Kaishile ')
    context = zmq.Context()  # 这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚
    sub_server_addr = "tcp://115.156.162.123:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.163.107'
    down_computer_addr = '192.168.127.100'
    down_computer_addr = '127.0.0.1'

    sub_server_addr = "tcp://192.168.127.100:6001"
    syncaddr = "tcp://127.0.0.1:5555"
    # sub_server_addr = "tcp://127.0.0.1:6001"

    port = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010]

    tcp_recv_zmq_send(context,sub_server_addr,syncaddr,down_computer_addr,5003)
    # for i in port:
    #     t2 = threading.Thread(target=tcp_recv_zmq_send,
    #                           args=(context, sub_server_addr, syncaddr, down_computer_addr, port))
    #     t2.start()


