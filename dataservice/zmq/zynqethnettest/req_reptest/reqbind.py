import  zmq


import  time


if __name__ == "__main__":
    context = zmq.Context()

    req_zmq=context.socket(zmq.REQ)
    req_zmqaddr = 'tcp://192.168.127.200:20011'
    req_zmq.setsockopt(zmq.RCVTIMEO, 100)
    req_zmq.setsockopt(zmq.SNDTIMEO, 100)
    req_zmq.bind(req_zmqaddr)
    while   True:
        time.sleep(1)
        try:
            req_zmq.send(b"hello ")
        except:
            print('send time out')
        try:
            b = req_zmq.recv()
            print(b)

        except:
            print('recv time out ')






