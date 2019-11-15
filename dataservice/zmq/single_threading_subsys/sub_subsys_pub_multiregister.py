

import zmq

Gas_NUM_SUBSCRIBERS_EXPECTED = 10



def broker_proxy():
    #创建本进程使用的上下文
    context = zmq.Context()

    #建立sub 套接字以供远端的多个不同子系统的pub 进行链接使用
    url =  "tcp://115.156.162.76:6000"
    socketsub = context.socket(zmq.SUB)
    socketsub.bind(url)
    #订阅内容设定为所有的套接字的所有的消息都要订阅
    socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


    #建立自身的分发系统，采用的是进程间的通信的机制，或者采用的是线程间的通信的机制
    socketpub = context.socket(zmq.PUB)
    # urlzmq = "tcp://127.0.0.1:6005"
    urlzmq = "ipc://main"
    socketpub.bind(urlzmq)


    # #connect同步自身子系统不同寄存器的订阅者，只有当自身子系统的所有的订阅者都已经发出订阅同步信号的情况下，才算完成订阅
    # sync_addr = 'ipc://sync_05_gascontrol'
    # syncservice = context.socket(zmq.REP)
    # syncservice.bind(sync_addr)
    #
    #   # Get synchronization from subscribers
    # subscribers = 0
    # while subscribers < Gas_NUM_SUBSCRIBERS_EXPECTED:
    #     # wait for synchronization request
    #     msg = syncservice.recv()
    #     # send synchronization reply
    #     syncservice.send(b'')
    #     subscribers += 1
    #     print("+1 subscriber (%i/%i)" % (subscribers, Gas_NUM_SUBSCRIBERS_EXPECTED))
    #
    # print('同步了本地的订阅者')
    #
    # #开始同步远端的pub端，目前是仅仅有一个同步端，实际上未来可能有很多的pub端
    # # ，需要我们进行同步只有当他们准备好了，也就是，我们得到了我们需要订阅的数量
    # #然后对面才能进行信息的发布，否则我们这边的第一层的sub就会丢失一定的消息
    # syncaddr = "tcp://115.156.162.76:5555"
    # sync_server = context.socket(zmq.REP)
    # sync_server.bind(syncaddr)
    #
    # #接收同步信号
    # # sync_server.recv()
    #
    # #发送已经接收到同步信号的回应,完成同步
    # # sync_server.send(b'')
    # Gas_NUM_PUBLISHERS_EXPECTED = 10
    # publishers = 0
    # while publishers < Gas_NUM_PUBLISHERS_EXPECTED:
    #     # wait for synchronization request
    #     msg = sync_server.recv()
    #     # send synchronization reply
    #     sync_server.send(b'')
    #     publishers += 1
    #     print("+1 subscriber (%i/%i)" % (publishers, Gas_NUM_PUBLISHERS_EXPECTED))
    #
    #
    # print('同步了远端')


    while True:
        response = socketsub.recv()
        print(response)
        socketpub.send(response)

if __name__=='__main__':


    broker_proxy()






