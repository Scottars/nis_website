import zmq

local_NUM_SUBSCRIBERS_EXPECTED = 0
remote_NUM_PUBLISHERS_EXPECTED = 1


HWM_VAL = 100000*60*31*5

def broker_proxy():
    #创建本进程使用的上下文
    context = zmq.Context()

    #建立sub 套接字以供远端的多个不同子系统的pub 进行链接使用
    # url =  "tcp://115.156.162.76:6000"
    url =  "tcp://127.0.0.1:6001"

    # url =  "ipc://sub_server_proxy"
    socketsub = context.socket(zmq.DEALER)
    socketsub.set_hwm(HWM_VAL)
    socketsub.bind(url)
    #订阅内容设定为所有的套接字的所有的消息都要订阅
    socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


    #建立自身的分发系统，采用的是进程间的通信的机制，或者采用的是线程间的通信的机制
    socketpub = context.socket(zmq.PUB)
    socketpub.set_hwm(HWM_VAL)
    urlzmq = "tcp://127.0.0.1:6006"
    # urlzmq = "ipc://main"
    socketpub.bind(urlzmq)




    #connect同步自身子系统不同寄存器的订阅者，只有当自身子系统的所有的订阅者都已经发出订阅同步信号的情况下，才算完成订阅
    # sync_addr ='ipc://main_sync_server'
    # syncservice = context.socket(zmq.REP)
    # syncservice.bind(sync_addr)
    #
    #   # Get synchronization from subscribers
    # subscribers = 0
    # while subscribers < local_NUM_SUBSCRIBERS_EXPECTED:
    #     # wait for synchronization request
    #     msg = syncservice.recv()
    #     # send synchronization reply
    #     syncservice.send(b'')
    #     subscribers += 1
    #     print("+1 subscriber (%i/%i)" % (subscribers, local_NUM_SUBSCRIBERS_EXPECTED))
    #
    # print('同步了本地的订阅者')
    #
    # #开始同步远端的pub端，目前是仅仅有一个同步端，实际上未来可能有很多的pub端
    # # ，需要我们进行同步只有当他们准备好了，也就是，我们得到了我们需要订阅的数量
    # #然后对面才能进行信息的发布，否则我们这边的第一层的sub就会丢失一定的消息
    # syncaddr = "tcp://115.156.162.76:5555"
    # sync_server = context.socket(zmq.REP)
    # sync_server.bind(syncaddr)

    #接收同步信号
    # sync_server.recv()

    #发送已经接收到同步信号的回应,完成同步
    sync_server.send(b'')
    publishers = 0
    while publishers < remote_NUM_PUBLISHERS_EXPECTED:
        # wait for synchronization request
        msg = sync_server.recv()
        # send synchronization reply
        sync_server.send(b'')
        publishers += 1
        print("+1 Publisher (%i/%i)" % (publishers, remote_NUM_PUBLISHERS_EXPECTED))


    print('同步了远端')

    import  time
    numpage=0


    while True:
        response = socketsub.recv()
        # time.sleep(1)
        # response=b'hello world'
        numpage = numpage  + 1
        print(numpage)
        # socketpub.send(response)

def broker_proxy_push():
    #创建本进程使用的上下文
    context = zmq.Context()

    #建立sub 套接字以供远端的多个不同子系统的pub 进行链接使用
    # url =  "tcp://115.156.162.76:6000"
    # url =  "tcp://127.0.0.1:6001"
    url =  "tcp://192.168.127.100:6002"

    # url =  "ipc://sub_server_proxy"
    socketsub = context.socket(zmq.DEALER)
    socketsub.set_hwm(HWM_VAL)
    socketsub.setsockopt(zmq.IDENTITY, b'sub')

    socketsub.bind(url)
    #订阅内容设定为所有的套接字的所有的消息都要订阅
    # socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


    # worker = context.socket(zmq.SUb)
    # worker.setsockopt(zmq.IDENTITY, b'sub')
    # worker.bind(url)


    #
    # #建立自身的分发系统，采用的是进程间的通信的机制，或者采用的是线程间的通信的机制
    # sender = context.socket(zmq.PUSH)
    # sender.set_hwm(HWM_VAL)
    # # url =  "tcp://127.0.0.1:6006"
    # url =  "ipc://main"
    # sender.bind(url)
    #
    # #connect同步自身子系统不同寄存器的订阅者，只有当自身子系统的所有的订阅者都已经发出订阅同步信号的情况下，才算完成订阅
    # sync_addr ='ipc://main_sync_server'
    # syncservice = context.socket(zmq.REP)
    # syncservice.bind(sync_addr)
    #
    #   # Get synchronization from subscribers
    # subscribers = 0
    # while subscribers < local_NUM_SUBSCRIBERS_EXPECTED:
    #     # wait for synchronization request
    #     msg = syncservice.recv()
    #     # send synchronization reply
    #     syncservice.send(b'')
    #     subscribers += 1
    #     print("+1 subscriber (%i/%i)" % (subscribers, local_NUM_SUBSCRIBERS_EXPECTED))
    # #
    # # print('同步了本地的订阅者')
    # #
    # # #开始同步远端的pub端，目前是仅仅有一个同步端，实际上未来可能有很多的pub端
    # # ，需要我们进行同步只有当他们准备好了，也就是，我们得到了我们需要订阅的数量
    # #然后对面才能进行信息的发布，否则我们这边的第一层的sub就会丢失一定的消息
    # syncaddr = "tcp://115.156.162.76:5555"
    # syncaddr = "tcp://127.0.0.1:5555"
    syncaddr = "tcp://192.168.127.100:5556"
    sync_server = context.socket(zmq.REP)
    sync_server.bind(syncaddr)

    # #接收同步信号
    # sync_server.recv()
    #
    # #发送已经接收到同步信号的回应,完成同步
    # sync_server.send(b'')
    print("we are syncing the remote punlisher")
    publishers = 0
    while publishers < remote_NUM_PUBLISHERS_EXPECTED:
        # wait for synchronization request
        msg = sync_server.recv()
        # send synchronization reply
        sync_server.send(b'')
        publishers += 1
        print("+1 Publisher (%i/%i)" % (publishers, remote_NUM_PUBLISHERS_EXPECTED))


    print('同步了远端')

    import  time
    numpage=0



    while True:
        # print('we are reiving ')
        # time.sleep(0.1)
        request = socketsub.recv()
        numpage += 1
        print(numpage)



'''
    这个地方为什么要做一个中介
    因为，
    如果不中介的话，
        1、我的subscribe 端 就要订阅所有的publisher 端
        2、同时，同步的情况也是相对比较麻烦----------所谓同步,是表示,publish 和 sub端平衡起来
    如果有中介解决
        1、可以解决同步的问题......对时间时间信息的处理
        2、其两端的部分，都可以各自变化，不会彼此受到影响
'''
if __name__=='__main__':


    broker_proxy_push() #不增加同步的方案,容易造成数据接收的丢失
    # broker_proxy()






