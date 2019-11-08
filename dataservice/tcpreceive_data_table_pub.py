
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






if __name__=='__main__':
    # database connect
    # db = pymysql.connect(host='localhost', user='root', password='123456', db='nis_hsdd', port=3306, charset='utf8')
    # cur = db.cursor()

    #为了定义一个对象线程
    # 创建一个socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接:
    s.connect(('115.156.163.107', 5001))

    import zmq
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("ipc://zmqpub")
    # socket.bind("tcp://192.168.127.100:6000")
    #


    packagenum=0

    zhanbao=0
    buzhanbao=0

    start_time_process = time.time()
    start_time_cpu = time.process_time()
    #实际上应当启用的市多线程来做这些事情的
    #每一个线程要做的事情就是接收对应的内容
    #我想epics里面做的也是基本想同样的事情  ---最后写一个自动化的脚本多线程
    while True:
        b = s.recv(20)
        # packagenum = packagenum + 1
        # print(b)
        size=len(b)
        if len(b) ==0:
            socket.send(b)

            break
        if size>10:
            zhanbao = zhanbao + 1
            print(size)

        else:
            buzhanbao = buzhanbao + 1

        # print(len(b))
        # socket.send(b)

    print(packagenum)
    end_time_process = time.time()
    end_time_cpu = time.process_time()
    print('程序执行时间',end_time_process-start_time_process)
    print('程序执行的CPU时间',end_time_cpu-start_time_cpu)
    print('不战报',buzhanbao)
    print('战报',zhanbao)
    socket.close()

    s.close()




