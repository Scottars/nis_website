'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=float
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''

import threading
import zmq
import time
import socket
import datetime
import struct
HWM_VAL = 100000*60*31*5

HWM_VAL = 1000

global flag_start

#这个线程用于交互线程
'''
1.Able to tell if the udp receiving thread is alive 
2.Able to tell if 
'''
sub_server_addr = "tcp://115.156.162.123:6000"
syncaddr = "tcp://115.156.162.76:5555"
down_computer_addr = '115.156.163.107'
# down_computer_addr = '127.0.0.1'
down_computer_addr = '192.168.127.11'
down_computer_addr = '192.168.127.100'

down_computer_addr = '127.0.0.1'

# sub_server_addr = "tcp://127.0.0.1:6001"
sub_server_addr = "tcp://192.168.127.100:6002"


# syncaddr = "tcp://127.0.0.1:5555"
syncaddr = "tcp://192.168.127.100:5556"

port = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010]
import threading
import time
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)



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


def tcp_recv_zmq_send(context, port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")
    # reveiver_url = "ipc://11_Router"
    reveiver_url = "tcp://192.168.127.201:5011"

    socketzmq = context.socket(zmq.PUB)
    socketzmq.set_hwm(HWM_VAL) #设定水位应当是在绑定之前进行.


    socketzmq.bind(reveiver_url)
    time.sleep(3)






    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind(("192.168.127.201", 8080))
    client_socket.settimeout(1)
    print('we have connected to the tcp data send server!---port is :', port)
    packagenum = 0

    count = 0
    # 实际上应当启用的市多线程来做这些事情的
    # 每一个线程要做的事情就是接收对应的内容
    # 我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
    global flag_start
    flag_start = True
    strtosend=b''
    num=0
    # b = b'startstart'


    while True:
            try:
                b, addr = client_socket.recvfrom(10)
                # b = b'startstart'
                # print(count)
                if count==1000000:
                    break
                if count==1:
                    start_time_perf = time.perf_counter()
                    start_time_process = time.process_time()
                count = count + 1
                timestample = str(datetime.datetime.now()).encode()
                b = b + timestample

                # strtosend+=b
                # num +=1
                # if num==10:
                # socketzmq.send(strtosend)
                #     strtosend=b''
                #     num=0
            except socket.timeout:
                print('In  udp time out')

                    # print('守护线程,守护进程')

    print(packagenum)
    end_time_perf = time.perf_counter()
    end_time_process = time.process_time()
    print('Receiving port is: ', port)
    print('Package num:', count)
    print('receing time cost:', end_time_perf - start_time_perf)
    print('Receiving speed',count/(end_time_perf-start_time_perf))

    socketzmq.close()




def zmq_monitor_thread(context):
    global flag_start
    monitored_zmq = context.socket(zmq.REP)
    monitored_zmqaddr = "tcp://192.168.127.200:8011"
    # monitored_zmq.setsockopt(zmq.IDENTITY,b'udp_11')

    monitored_zmq.connect(monitored_zmqaddr)
    # monitored_zmq.setsockopt(zmq.RCVTIMEO,2000)
    udpthread = threading.Thread(target=tcp_recv_zmq_send,
                                 args=(context, sub_server_addr, syncaddr, down_computer_addr, 5011))

    jiange=0
    while True:
        # time.sleep(1)


        try:
            x = monitored_zmq.recv()
            print('the recvmsg is',x)

            if x==b'start':
                flag_start = True
                monitored_zmq.send(b'start received')

            elif x==b'stop':
                flag_start = False
                monitored_zmq.send(b'stop received')
            elif x==b'udp alive?':
                print('in here')
                if udpthread.is_alive():
                    print('send yes')
                    monitored_zmq.send(b'yes')
                else:

                    monitored_zmq.send(b'no')
            elif x==b'run udp thread':
                udpthread = threading.Thread(target=tcp_recv_zmq_send,
                                             args=(context, sub_server_addr, syncaddr, down_computer_addr, 5011))
                udpthread.start()
                monitored_zmq.send(b'run udp thread received')
            elif x==b'stop udp thread':
                stop_thread(udpthread)
                monitored_zmq.send(b'stop udp thread received')
            else:
                monitored_zmq.send(b'zmq thread alive')

        except:
            print('time out in zmq')


if __name__ == '__main__':
    print('Kaishile ')
    context = zmq.Context()  # 这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚
    sub_server_addr = "tcp://115.156.162.123:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.163.107'
    # down_computer_addr = '127.0.0.1'
    down_computer_addr = '192.168.127.11'
    down_computer_addr = '192.168.127.100'

    down_computer_addr = '127.0.0.1'

    # sub_server_addr = "tcp://127.0.0.1:6001"
    sub_server_addr = "tcp://192.168.127.100:6002"


    # syncaddr = "tcp://127.0.0.1:5555"
    syncaddr = "tcp://192.168.127.100:5556"



    port = [5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010]

    #将这个以线程的方式进行启动,此时另外的线程就可以实时的对此线程进行一定判断,并且对一个全局变量进行监控了.以接收epics的控制.
    # tcp_recv_zmq_send(context,sub_server_addr,syncaddr,down_computer_addr,5011)
    # for i in port:

    # t1= threading.Thread(target=zmq_monitor_thread,
    #                      args=(context,))
    # t1.start()

    # udpthread = threading.Thread(target=tcp_recv_zmq_send,
    #                          args=(context, 5011))
    # udpthread.start()

    tcp_recv_zmq_send(context,5011)