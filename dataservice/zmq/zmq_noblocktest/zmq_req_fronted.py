

import zmq
import  time

context = zmq.Context()
url = "tcp://127.0.0.1:5559"
socketsub = context.socket(zmq.REQ)
socketsub.bind(url)


socketsub.send(b'hello from front end')
print('send okay la ')
msg= socketsub.recv()
print(msg)
