# -*- coding: utf-8 -*-
# Broker.py

import sys
import time
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


class Broker(object):
    def __init__(self, xsub_port, xpub_port):
        self.xsub_socket, self.xpub_socket = get_broker(xsub_port, xpub_port)
        self.poller = zmq.Poller()
        self.poller.register(socket=self.xpub_socket, flags=zmq.POLLIN)
        self.poller.register(socket=self.xsub_socket, flags=zmq.POLLIN)
        self.buffer = {}

    def update_buffer(self, msg):
        topic = msg.split(',')[0]
        if topic in self.buffer:
            self.buffer[topic].append(msg)
        else:
            self.buffer.update({topic: [msg]})

    def handler(self):
        while True:
            events = dict(self.poller.poll(1000))
            # events from publishers
            if self.xsub_socket in events:
                msg = self.xsub_socket.recv_string()
                self.xpub_socket.send_string(msg)
                print('[Broker] Forwarded message: %s' % msg)
                self.update_buffer(msg)
            # events from subscribers
            if self.xpub_socket in events:
                topic = ''.join(list(self.xpub_socket.recv_string())[1:])
                if topic in self.buffer:
                	# send history messages
                    [self.xpub_socket.send_string(item) for item in self.buffer[topic]]
                else:
                    self.xsub_socket.send_string(topic)

if __name__ == '__main__':
	# The 1st argument is XSub port number, the 2nd is XPub port number
    broker = Broker(sys.argv[1], sys.argv[2])
    broker.handler()
