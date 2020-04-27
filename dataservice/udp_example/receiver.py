import threading
import zmq
import time
import socket
import datetime


def tcp_recv_zmq_send(context, sub_server_addr, syncaddr, down_computer_addr, port):
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")

    # 为了定义一个对象线程
    # 创建一个socket:
    # 建立IPv4,UDP的socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字

    # 绑定端口：
    # tcp_server_socket.bind(("192.168.1.100", 8080))
    s.bind(("192.168.1.100", 8080))

    # 不需要开启listen，直接接收所有的数据
    # print('Bind tcp on 8080')
    # tcp_server_socket.listen(1)  # 监听（）内为最大监听值
    # client_socket, client_addr = tcp_server_socket.accept()  # 建立连接（accept（无参数）
    #

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
    while True:

        # 接收来自客户端的数据,使用recvfrom
        b, addr = s.recvfrom(1024)
        # b,addr = client_socket.recvfrom(12)
        print(b)

        count = count + 1
        if count == 10000:
            break
        # r.set('name',b)
        # f.write(str(b)+'\n')

        # if size>10:
        #     zhanbao = zhanbao + 1
        #     # print(size)
        #
        # else:

        #     buzhanbao = buzhanbao + 1

        # timestample = str(datetime.datetime.now()).encode()
        # b = b + timestample
        # print(len(b))
        # socketzmq.send(b)  #显然，zeromq 这句话几乎消耗了很多很多的时间
        # x=socketzmq.recv()

    print(packagenum)
    end_time_perf = time.perf_counter()
    end_time_process = time.process_time()
    print('the port is: ', port)
    print("数据个数", count)
    print('程序_process', end_time_process - start_time_process)  # process time 不包含time sleep 的
    print('程序执行perf_count', end_time_perf - start_time_perf)  #
    print('数据的速度', count / (end_time_perf - start_time_perf))
    # client_socket.close()
    s.close()


if __name__ == '__main__':
    print('Kaishile ')
    context = zmq.Context()  # 这个上下文是真的迷，到底什么情况下要用共同的上下文，什么时候用单独的上下文，找时间测试清楚
    sub_server_addr = "tcp://115.156.162.76:6000"
    syncaddr = "tcp://115.156.162.76:5555"
    down_computer_addr = '115.156.162.76'
    tcp_recv_zmq_send(context, sub_server_addr, syncaddr, down_computer_addr, 8080)
    #
    # port=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010]
    #
    #
    # for i in port:

    # t2 = threading.Thread(target=tcp_recv_zmq_send,args=(context,sub_server_addr,syncaddr,down_computer_addr,i))
    # t2.start()
#


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
