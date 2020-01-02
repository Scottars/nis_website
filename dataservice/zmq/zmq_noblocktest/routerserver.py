import zmq
import  time

context=zmq.Context()

url="tcp://127.0.0.1:5001"
router2=context.socket(zmq.REP)

router2.connect(url)

while True:
    time.sleep(0.1)
    # router2.send(b'this is router1')
    # print('we are sending ')
    router2.recv()
    print('we are receiving')
