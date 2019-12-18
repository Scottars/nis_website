from pynng import Pub0,Sub0
import time


address='tcp://127.0.0.1:3333'

def server_pub():
    pub_sock=Pub0(dial=address)
    i=0
    while True:
        i=i+1
        time.sleep(1)
        print('we are sending')
        pub_sock.send(b'i am server'+str(i).encode())
        time.sleep(1)
        pub_sock.send(b'we are the world'+str(i).encode())
if __name__=='__main__':

    server_pub()


