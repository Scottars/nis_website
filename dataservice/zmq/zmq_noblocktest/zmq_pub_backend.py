

import zmq
import  time

context = zmq.Context()
url = "tcp://127.0.0.1:5560"
socketsub = context.socket(zmq.PUB)
socketsub.connect(url)


while True:
    time.sleep(0.01)

    socketsub.send(b'backendend end')
    print('send okay la ')



