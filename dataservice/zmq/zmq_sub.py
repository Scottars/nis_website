

import zmq


context = zmq.Context()
url = "tcp://115.156.162.123:6555"
socketsub = context.socket(zmq.SUB)
socketsub.connect(url)
socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


while True:

    # response = socketsub.recv()
    print('we have get one')


