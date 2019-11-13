# -*- coding: utf-8 -*-
# Subscriber.py

import argparse
from dataservice.zmq.zmq_pub_xsub_xpub_example.utl import get_broker,get_publisher,get_subscriber
import zmq
def get_publisher(address, port):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    connect_addr = 'tcp://%s:%s' % (address, port)
    socket.connect(connect_addr)
    return socket

def get_subscriber(address, port, topics):
	# Subscriber can register one more topics once
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    connect_addr = 'tcp://%s:%s' % (address, port)
    socket.connect(connect_addr)
    if isinstance(topics, str):
        socket.subscribe(topics)
    elif isinstance(topics, list):
        [socket.subscribe(topic) for topic in topics]
    return socket

def get_broker(xsub_port, xpub_port):
    context = zmq.Context()

    xsub_socket = context.socket(zmq.XSUB)
    xsub_addr = 'tcp://*:%s' % xsub_port
    xsub_socket.bind(xsub_addr)
    # make xsub receive any message
    xsub_socket.send(b'\x01')

    xpub_addr = 'tcp://*:%s' % xpub_port
    xpub_socket = context.socket(zmq.XPUB)
    xpub_socket.bind(xpub_addr)
    # make xpub receive verbose messages
    xpub_socket.setsockopt(zmq.XPUB_VERBOSE, 1)

    # zmq.proxy(xsub_socket, xpub_socket)
    return xsub_socket, xpub_socket



class Subscriber(object):
    def __init__(self, broker_address, broker_port, topics):
        self.topics = topics
        self.socket = get_subscriber(broker_address, broker_port, topics)

    def subscribe(self):
        while True:
            msg = self.socket.recv_string()
            print('[Subscriber] Received message: %s' % msg)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topics', type=str, help='Topics separated by comma')
    parser.add_argument('-a', '--address', type=str, help='Broker address')
    parser.add_argument('-p', '--port', type=str, help='Broker port number')
    args = parser.parse_args()
    topics = args.topics.split(',')
    sub = Subscriber(args.address, args.port, topics)
    sub.subscribe()
