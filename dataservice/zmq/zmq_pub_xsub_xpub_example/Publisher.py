# -*- coding: utf-8 -*-
# Publisher.py

import csv
import time
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


class Publisher(object):
    def __init__(self, topic, broker_address, broker_port, data, rate):
    	'''
        :param topic: the topic associated with messages
        :param broker_address: broker public IP
        :param broker_port: XSub port number
        :param data: csv file path
        :param rate: publishing rate, unit is second
        '''
        self.topic = topic
        self.pub_socket = get_publisher(broker_address, broker_port)
        self.data = data
        self.rate = rate

    def publish_data(self):
        with open(self.data, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                row.insert(0, self.topic)
                record = ','.join(row)
                self.pub_socket.send_string(record)
                print('[Publisher] Published message: %s' % record)
                time.sleep(self.rate)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', type=str, help='Topic')
    parser.add_argument('-a', '--address', type=str, help='Broker public IP address')
    parser.add_argument('-p', '--port', type=str, help='Broker XSub port number')
    parser.add_argument('-f', '--file', type=str, help='Data file path')
    parser.add_argument('-r', '--rate', type=int, help='Publishing rate in second')
    args = parser.parse_args()
    pub = Publisher(args.topic, args.address, args.port, args.file, args.rate)
    pub.publish_data()
