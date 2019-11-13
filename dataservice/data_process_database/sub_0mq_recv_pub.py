

import zmq



def broker_proxy():
    context = zmq.Context()
    url =  "tcp://115.156.162.123:6000"
    socketsub = context.socket(zmq.SUB)
    socketsub.bind(url)
    socketsub.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))


    socketpub = context.socket(zmq.PUB)
    socketpub.bind("tcp://127.0.0.1:6005")

    while True:
        response = socketsub.recv()
        # print(response)
        socketpub.send(response)

if __name__=='__main__':


    broker_proxy()