

import  zmq
import time





if __name__ =='__main__':



    context = zmq.Context()
    recvsub=context.socket(zmq.SUB)
    recvsubaddr='tcp://127.0.0.1:8888'
    recvsub.setsockopt(zmq.SUBSCRIBE,b'')
    recvsub.bind(recvsubaddr)
    recvsub.setsockopt(zmq.RCVTIMEO,2000)

    savereq=context.socket(zmq.REQ)
    savereqaddr='tcp://127.0.0.1:8889'
    savereq.bind(savereqaddr)
    savereq.send(b'startsaving')
    x=savereq.recv()
    # 设定一个延时，以确定如果超时了，我们可以从新穿一次
    print(x)
    i=0
    while True:
        i+=1
        if i==1000:
            break
        try:
            a=recvsub.recv()
            print(a)
        except:
            print('chaoshi ')
    # time.sleep(5)
    savereq.send(b'toclose')
    a=savereq.recv()
    print(a)

    savereq.close()


