

import zmq


context = zmq.Context()
url =  "tcp://115.156.162.76:6000"
socketsub = context.socket(zmq.SUB)
socketsub.bind(url)
socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


socketpub = context.socket(zmq.PUB)
socketpub.bind("inproc://main")

while True:
    response = socketsub.recv()

    socketpub.send(response)

