import threading

import zmq
import time
import socket


context = zmq.Context()

def zmq_recv():

    socket = context.socket(zmq.SUB)
    # socket = context.socket(zmq.REP)
    socket.connect("inproc://zmqpub")
    socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))  # 接收所有消息

    zhanbao=0
    buzhanbao=0
    start_time = time.clock()
    while True:
        msg=socket.recv()
        print(msg)

def tcp_recv_zmq_send():
    # socketzmq = context.socket(zmq.PUB)
    # socketzmq.bind("tcp://115.156.162.76:6000")

    socketzmq = context.socket(zmq.PUB)
    socketzmq.bind("inproc://zmqpub")

    while True:
        time.sleep(1)
        socketzmq.send('hello'.encode())


if __name__ == '__main__':
    print('Kaishile ')
    t1 = threading.Thread(target=tcp_recv_zmq_send)
    t2 = threading.Thread(target=zmq_recv)
    t1.start()
    t2.start()

