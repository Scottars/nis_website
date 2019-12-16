from pynng import Pub0
import time


address="ws://127.0.0.1:22315"
# address = 'tcp://127.0.0.1:22315'

pub=Pub0(listen=address)
i = 1
while True:
    i = i + 1
    time.sleep(1)
    print('we are sending-----')
    pub.send(b'asyn masg')
