import zmq
import  time

context=zmq.Context()

url="tcp://127.0.0.1:5001"
router1=context.socket(zmq.ROUTER)

router1.bind(url)

while True:
    time.sleep(1)
    router1.send(b'this is router1')
    print('we are sending ')

