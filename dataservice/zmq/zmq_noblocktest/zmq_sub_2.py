

import zmq


context = zmq.Context()
url="ipc://main"

socketsub = context.socket(zmq.SUB)
socketsub.connect(url)
socketsub.setsockopt(zmq.SUBSCRIBE,b'')

while True:

    response = socketsub.recv()
    print(response)
    print('we have get one in socket sub 2 ')


