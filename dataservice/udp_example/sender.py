
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#不需要建立连接：
for data in [b'Michael', b'ALice', b'FF']:
    #发送数据到客户端：
    s.sendto(data, ('115.156.162.76', 9999))
    #接收来自客户端的数据：
    print(s.recvfrom(1024)[0].decode('utf-8'))
s.close()
