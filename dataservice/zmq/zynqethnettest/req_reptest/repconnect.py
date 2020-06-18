import  zmq


import  time


if __name__ == "__main__":
    context = zmq.Context()

    req_zmq=context.socket(zmq.REP)
    req_zmqaddr = 'tcp://192.168.127.200:20011'
    req_zmq.connect(req_zmqaddr)
    count=0
    while   True:
        # try:

            b = req_zmq.recv()
            count+=1
            if count == 10:
                time.sleep(1)
            print(count,b)
            req_zmq.send(b"world ")

        # except:
        #     print('recv time out ')






