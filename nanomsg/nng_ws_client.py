from pynng import Pub0,Sub0
import time


address="ws://127.0.0.1:22315"
# address="tcp://127.0.0.1:22315"

sub=Sub0(dial=address)
sub.subscribe(b'')
i = 1
while True:
    i = i + 1
    print('we are receiving')
    a=sub.recv()

    print('we are receiveing:',a)