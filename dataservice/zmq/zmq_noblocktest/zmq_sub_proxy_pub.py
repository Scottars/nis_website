

import zmq


context = zmq.Context()
# url="ipc://sub_server_proxy"
url="tcp://115.156.162.76:5555"


socketsub = context.socket(zmq.SUB)
socketsub.bind(url)
socketsub.setsockopt(zmq.SUBSCRIBE,b'')

url="ipc://mainserver"
socketpub = context.socket(zmq.PUB)
socketpub.bind(url)


numberpack = 1
while True:

    response = socketsub.recv()
    numberpack = numberpack + 1
    print(numberpack)
    print('we have get one',response)

    socketpub.send(response)


