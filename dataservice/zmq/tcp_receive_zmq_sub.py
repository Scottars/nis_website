
import zmq
import pymysql


import socket
import pymysql

import crcmod
import time

import socket
import  struct

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
def bytesToHex(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return hex(struct.unpack("=H", ba)[0])
#注意这个地方的解包的地方H 与 h 的关系

def bytesToInt(a1, a2):
    ba = bytearray()
    ba.append(a1)
    ba.append(a2)
    return struct.unpack("=H", ba)[0]

def crccheckhole(b,length):
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)

    return hex(crc16_func(b[0:length]))==bytesToHex(b[length],b[length+1])
def crccheck(b,length):
    print('传过来的b，和lenght',b,'   ',length)
    crc16_func = crcmod.mkCrcFun(0x18005, initCrc=0xFFFF, rev=True, xorOut=0x0000)
    return crc16_func(b[0:length]) == bytesToInt(b[length], b[length + 1])

def database_write_float(b):
    # data = bytesToFloat(b[4], b[5], b[6], b[7])
    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (
    # b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print(b[2])
    pass
#定义gas control 部分的测试
#01 1479A 流量计的数值， float
def Gas_Control_05_03_01(b):
    database_write_float(b)

#02 627D  气压计的数值 float
def Gas_Control_05_03_02(b):
    database_write_float(b)

    # print('register 02')

#03 CDG_025D 气压的数值  float
def Gas_Control_05_03_03(b):
    database_write_float(b)
    # print('register 03')
#04 供气阀门的状态16位，2个字节
def Gas_Control_05_03_04(b):
    pass
    # data = bytesToInt(b[4], b[5])
    #能够过去，肯定也就能够还原成1111 0000  1111 0000 的形式

    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print('register 04')

#14  读取当前是否处气压的 puff模式 1个字节0xff 0x00
def Gas_Control_05_03_14(b):
    data =b[4]
    # 能够过去，肯定也就能够还原成1111 0000  1111 0000 的形式
    #
    # sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (5,%d,1,%f,NOW(6));" % (
    # b[2], data)
    # cur.execute(sql)
    # db.commit()
    # print('register 14')
#15  读取真空度的设定值 float
def Gas_Control_05_03_15(b):
    database_write_float(b)
    # print('register 15')

##16 读取流量计的设定值 float
def Gas_Control_05_03_16(b):
    database_write_float(b)
    # print('register 16')
#17  读取puff模式下，气压设定值
def Gas_Control_05_03_17(b):
    database_write_float(b)
    # print('register 17')
#18   读取pid 三个参数设定值  p i d 3*float=12个字节
def Gas_Control_05_03_18(b):
    # print('register 18')
    pass
def register_case_03(x,b):
    cases={
        b'\x01': Gas_Control_05_03_01,
        b'\x02': Gas_Control_05_03_02,
        b'\x03': Gas_Control_05_03_03,
        b'\x04': Gas_Control_05_03_04,
        b'\x14': Gas_Control_05_03_14,
        b'\x15': Gas_Control_05_03_15,
        b'\x16': Gas_Control_05_03_16,
        b'\x17': Gas_Control_05_03_17,
        b'\x18': Gas_Control_05_03_18,
    }
    func=cases.get(x,None)
    return func(b)






context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket = context.socket(zmq.REP)
socket.connect("ipc://zmqpub")
socket.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))  # 接收所有消息

zhanbao=0
buzhanbao=0
start_time = time.clock()
while True:
    b = socket.recv();
    # socket.send(b'1')
    # print(b)

    end_time = time.clock()
    if len(b)==0:
        print('总计耗时',end_time-start_time)
        break

    size = len(b)
    # print(size)

    # if end_time-start_time > 10:
    #     pass
    #     break
    if size>10:
        zhanbao = zhanbao + 1

    else:
        buzhanbao = buzhanbao + 1


    # if  crccheckhole(b,length=4+b[3]):
    #     # print('crccheck is okay')
    #     #this level is to get which
    #     if b[0]==struct.unpack('=b',b'\x05')[0]:
    #         #this level is to get read or write or on off
    #         if b[1]==struct.unpack('=b',b'\x03')[0]:
    #             #this level is to get which register
    #             register_case_03(struct.pack('=b',b[2]), b)
    #
    #         elif b[1]==struct.unpack('=b',b'\x05')[0]:
    #
    #             print('另外一个功能码05')
    #         #对于05功能码，只有当开关量变化的时候，才给我发一个反馈的消息，告诉我发生了改变（或者与史晨昱的数据库相互结合着使用）
    #         elif b[1]==struct.unpack('=b',b'\x06')[0]:
    #             print('另外一个功能码06')
    #         elif b[1] == struct.unpack('=b', b'\x08')[0]:
    #             print('另外一个功能码08')
    #
    #
    #
    #
    #
    #
    #     else:
    #         print('Not our data')
    # else:
    #     print('crc 校验错误')

print('不战报',buzhanbao)
print('战报',zhanbao)
