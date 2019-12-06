

import zmq
import  time

context = zmq.Context()
url = "tcp://127.0.0.1:6555"
socketsub = context.socket(zmq.PUB)
socketsub.bind(url)


while True:
    time.sleep(1)

    socketsub.send(b'hello')
    print('send okay la ')

