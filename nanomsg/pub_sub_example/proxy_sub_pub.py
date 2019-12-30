from pynng import Pub0, Sub0
import threading

addresssub = 'ipc://asyncserversub'
addresspub = 'ipc://asyncserverpub'



def proxy_subpub():
    sub_sock = Sub0(listen=addresssub)
    sub_sock.subscribe(b'')

    pub_sock = Pub0(listen=addresspub)
    while True:
        print('we are receiving')
        msg=sub_sock.recv()
        print(msg)
        pub_sock.send(msg)


if __name__ == '__main__':
    proxy_subpub()
