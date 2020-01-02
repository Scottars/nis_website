

import zmq
import time

context = zmq.Context()
url="ipc://sub_server_proxy"
url="tcp://127.0.0.1:5555"
url="tcp://115.156.162.76:5555"


socketpub = context.socket(zmq.PUB)
socketpub.connect(url)



while True:
    time.sleep(1)
    response = socketpub.send(b'newworld')
    print('we have sent one')


