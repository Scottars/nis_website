import zmq
import  time

context=zmq.Context()

url="tcp://127.0.0.1:5001"
router1=context.socket(zmq.DEALER)

router1.bind(url)

# while True:
for i in range(4):
    # time.sleep(1)
    router1.send_multipart([b'',b'this is router1'])  #第一个的空白的字节是用来验证身份使用的
    print('we are sending ')

    #下面这两个recv是阻塞的，也就是说，我们上面可以控制得到好多个客户端，这样以确定，我们能够正常已经正常的将我们的所有的实验的数据传输给了多个的客户端
    router1.recv()   #rep 会自动返回一个空的字节，用来表示已经传递成功了
    print(router1.recv())   #正式表示我能够得到下位机的回复

