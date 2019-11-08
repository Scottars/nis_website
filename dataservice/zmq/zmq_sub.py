

import zmq


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.127.100:6000")
socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))

while True:
    response = socket.recv()
    print(len(response))

