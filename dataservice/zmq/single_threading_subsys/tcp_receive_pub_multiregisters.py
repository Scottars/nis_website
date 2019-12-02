import threading
import zmq
import time
import socket
import datetime

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
        if len(b)==1:
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

def tcp_recv_zmq_send(context,sub_server_addr,syncaddr,down_computer_addr,port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")

    socketzmq = context.socket(zmq.PUB)
    socketzmq.connect(sub_server_addr)
    # #
    # #为了等待远端的电脑的sub的内容全部都连接上来。进行的延迟
    # time.sleep(3)
    # 保证同步的另外的一种方案就是采用req-rep的同步
    # sync_client = context.socket(zmq.REQ)
    # sync_client.connect(syncaddr)
    # #
    # #发送同步信号
    # sync_client.send(b'')
    #
    # #等待同步回应,完成同步
    # sync_client.recv()





    #为了定义一个对象线程
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect((down_computer_addr, port))
    # s.connect(('192.168.127.5', 5001))

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
        print(b)


        if b[7] ==115:
            print('我们一直不在这')
            # socketzmq.send(b)
            pass
            break


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

        if size>10:
            zhanbao = zhanbao + 1
            # print(size)

        else:
            buzhanbao = buzhanbao + 1

        timestample = str(datetime.datetime.now()).encode()
        b = b + timestample
        # print(len(b))
        # socketzmq.send(b)  #显然，zeromq 这句话几乎消耗了很多很多的时间
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
    sub_server_addr = "tcp://115.156.162.76:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.162.76'
    tcp_recv_zmq_send(context,sub_server_addr,syncaddr,down_computer_addr,5002)

    # port=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010]
    #
    #
    # for i in port:
    #
    #     t2 = threading.Thread(target=tcp_recv_zmq_send,args=(context,sub_server_addr,syncaddr,down_computer_addr,i))
    #     t2.start()




##关于实验的几点呢的说明：
'''
    下位机以1ms的速度发送，而且是发送直接发下去，忽略了nagle算法的情况下，仍然会出现比较严重的战报的问题，出现这种问题的原因是下位机的处理的速度不够快
    下位机每隔1ms的速度发送，连续两个寄存器持续发送，总计发送1000次，也就是2000个包，出现的tcp的不粘包的个数是266个，出现tcp粘包的个数是266个。
    
    显然，这种情况的粘包的情况，太麻烦，这个时候，我们需要的解决方案：
    1、下位机直接加入时间的处理
    2、尽量保证不粘包，上位机对其给出时间。
    
    
    ###############啊 噗噗噗，   居然发现忘记插网线了，那么我们当时测试得到的结果应该走的无线网络，所以慢慢慢了很多，当前换成有线网络测试结果：
    下位机以0.0001s，也就是0.1ms的速度点进行发送战报的情况是：1964 不粘包，18个毡包。
    
    
'''
