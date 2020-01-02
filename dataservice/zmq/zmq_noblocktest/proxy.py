import zmq

# Prepare our context and sockets
context = zmq.Context()
frontend = context.socket(zmq.REP)
frontend.connect("tcp://127.0.0.1:5559")


backend = context.socket(zmq.SUB)
backend.bind("tcp://127.0.0.1:5560")
backend.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

numberpack=0
# Switch messages between sockets
while True:
    socks = dict(poller.poll())

    if socks.get(frontend) == zmq.POLLIN:

        message = frontend.recv()
        print('we are are front end')
        frontend.send(b'we are ready')
        print(message)

    if socks.get(backend) == zmq.POLLIN:
        # print('we are are backend end')
        numberpack = numberpack + 1
        print('后端的数据',numberpack)
        message = backend.recv()
        # print(message)

