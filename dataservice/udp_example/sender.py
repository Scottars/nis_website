
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#不需要建立连接：
numm = 100000000
start_perf = time.perf_counter()
data = b'helloworld'
for i in range(140):
    data = data +b'helloworld'
for i in range(numm):
    s.sendto(data, ('192.168.127.201', 8080))
    # print('i',i)
    #接收来自客户端的数据：
    # print(s.recvfrom(1024)[0].decode('utf-8'))
end_perf = time.perf_counter()

print('Package num:',numm)
print('Sending cost:',end_perf-start_perf)
print('Sending speed:',numm / (end_perf-start_perf))

s.close()
