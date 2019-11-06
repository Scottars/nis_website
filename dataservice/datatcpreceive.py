
import socket
import  struct
import time
def floatToBytes(f):
    bs = struct.pack("f",f)
    return (bs[3],bs[2],bs[1],bs[0])
def bytesToFloat(h1,h2,h3,h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f",ba)[0]
# context = zmq.Context()
# socketzeromq = context.socket(zmq.PUB)
# socketzeromq.bind("tcp://192.168.127.101:6000")

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:

s.connect(('115.156.163.107',5001))

start_time = time.process_time()
while True:
        b = s.recv(1024)
        # print(b)
        # print(len(b))

        # s.send('ok'.encode('utf-8'))
        # print('hello')
        if len(b) ==0:
            break
end_time = time.process_time()
print('消耗时间',end_time-start_time)