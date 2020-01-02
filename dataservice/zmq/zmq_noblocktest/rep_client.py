import zmq
import  time

context=zmq.Context()

url="tcp://127.0.0.1:5001"
router2=context.socket(zmq.REP)

router2.connect(url)


while True:
# for i in range(2):
    time.sleep(0.1)
    # router2.send(b'this is router1')
    # print('we are sending ')
    dataweger=router2.recv_multipart()
    print('we are receiving')
    print(dataweger)
    router2.send(b'hhha')

