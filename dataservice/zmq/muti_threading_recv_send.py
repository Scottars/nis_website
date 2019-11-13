import threading
import zmq
import time
import socket


def zmq_recv(context,url):

    socket = context.socket(zmq.SUB)
    # socket = context.socket(zmq.REP)
    socket.connect(url)
    socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))  # 接收所有消息

    zhanbao=0
    buzhanbao=0
    start_time = time.clock()
    while True:
        b = socket.recv();
        # socket.send(b'1')
        # print(b)

        end_time = time.clock()
        if len(b)==0:
            # print('总计耗时',end_time-start_time)
            break

        size = len(b)
        # print(size)

        # if end_time-start_time > 10:
        #     pass
        #     break
        if size>10:
            zhanbao = zhanbao + 1

        else:
            buzhanbao = buzhanbao + 1

    print('接收不粘包',buzhanbao)
    print('接收粘包',zhanbao)

def tcp_recv_zmq_send(context,url,port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")

    socketzmq = context.socket(zmq.PUSH)
    socketzmq.connect(url)
    #
    #
    time.sleep(3)
    #为了定义一个对象线程
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('115.156.163.107', port))
    # s.connect(('192.168.127.5', 5001))
    f = open('testtxt','w')
    print('we have connected to the tcp data send server!---port is :',port)

    packagenum=0

    zhanbao=0
    buzhanbao=0
    start_time_clock = time.clock()
    start_time_perf = time.perf_counter()
    start_time_process = time.process_time()
    count =0
    #实际上应当启用的市多线程来做这些事情的
    #每一个线程要做的事情就是接收对应的内容
    #我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
    while True:
        b = s.recv(20)
        # print(len(b))
        # print(b)
        # s.send(b'i')
        # packagenum = packagenum + 1
        # print(b)
        size=len(b)
        count = count + 1
        # if count==10000:
        #     break
        # r.set('name',b)
        # f.write(str(b)+'\n')

        if len(b) ==0:
            print('我们一直不在这')
            socketzmq.send(b)
            pass
            break
        if size>10:
            zhanbao = zhanbao + 1
            # print(size)

        else:
            buzhanbao = buzhanbao + 1

        # print(len(b))
        socketzmq.send(b)  #显然，zeromq 这句话几乎消耗了很多很多的时间
        # x=socketzmq.recv()

    print(packagenum)
    end_time_clock = time.clock()
    end_time_perf = time.perf_counter()
    end_time_process = time.process_time()
    print('the port is: ',port)
    print('程序的clock time消耗: ',end_time_clock - start_time_clock)
    print('程序_process',end_time_process- start_time_process)  #process time 不包含time sleep 的
    print('程序执行perf_count',end_time_perf-start_time_perf)   #
    print('tcp接收不粘包',buzhanbao)
    print('tcp接收粘包',zhanbao)
    socketzmq.close()

    s.close()


if __name__ == '__main__':
    print('Kaishile ')
    context = zmq.Context()  #这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚
    url = "tcp://115.156.162.123:6000"
    # t1 = threading.Thread(target=zmq_recv,args=(context,url))
    # t1.start()

    port=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010]
    for i in port:
        t2 = threading.Thread(target=tcp_recv_zmq_send,args=(context,url,i))
        t2.start()

