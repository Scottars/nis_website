from pynng import Pub0,Sub0
import threading



address='tcp://127.0.0.1:3334'

def client_sub():
    sub_sock=Sub0(dial=address)
    sub_sock.subscribe(b'w')
    sub_sock.subscribe(b'i')

    while True:
        print('we are receiving')
        print(sub_sock.recv())


if __name__=='__main__':


    client_sub()

