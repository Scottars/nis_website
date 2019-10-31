
import socket

import struct

import threading
import  time


import crcmod
import binascii

import socket
import  struct
# import zmq
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
def crcbytesToHex(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return hex(struct.unpack("=H", ba)[0])
#注意这个地方的解包的地方H 与 h 的关系

def crcbytesToInt(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return struct.unpack("=h", ba)[0]

def crccheckhole(b,length):
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)

    return hex(crc16_func(b[0:length]))==crcbytesToHex(b[length],b[length+1])
def crccheck(b,length):
    print('传过来的b，和lenght',b,'   ',length)
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
    return crc16_func(b[0:length]) == crcbytesToInt(b[length], b[length + 1])

#为了定义一个对象线程
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:


s.connect(('192.168.127.5', 5001))

b=b'\x05\x03\x01\x04AX\x00\x00\xd6\xca'

crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
print(crcbytesToHex(b[8],b[9]))
print(b[8],b[9])  #214 d6   202 ca
print(hex(crc16_func(b[0:8])))




#实际上应当启用的市多线程来做这些事情的
#每一个线程要做的事情就是接收对应的内容
#我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
while True:
    b = s.recv(1024)
    print('传过来的数值是:',b)
    print('传过来的长度是多少',len(b))
    if  crccheckhole(b,length=8):
        print('crccheck is okay')

        #this level is to get which
        if b[0]==struct.unpack('=b',b'\x05')[0]:
            #this level is to get read or write or on off
            if b[1]==struct.unpack('=b',b'\x03')[0]:
                #this level is to get which register
                if b[2]==struct.unpack('=b',b'\x01')[0]:

                    #this level is to get the data length
                    if b[3]==4:
                        data=bytesToFloat(b[4],b[5],b[6],b[7])
                        print('读取得到什么什么数值',data)

                    elif b[3]==8:
                        print("it's double type")

                elif b[2]==struct.unpack('=b',b'\x02')[0]:
                    print('寄存器02')
                    data = bytesToFloat(b[4], b[5], b[6], b[7])
                    print('读取得到什么什么数值', data)


            elif b[2]==struct.unpack('=b',b'\x05')[0]:
                print('另外一个功能码05')
            #对于05功能码，只有当开关量变化的时候，才给我发一个反馈的消息，告诉我发生了改变（或者与史晨昱的数据库相互结合着使用）
            elif b[1]==struct.unpack('=b',b'\x06')[0]:
                print('另外一个功能码06')
            elif b[1] == struct.unpack('=b', b'\x08')[0]:
                print('另外一个功能码08')






        else:
            print('Not our data')
    else:
        print('crc 校验错误')




s.close()