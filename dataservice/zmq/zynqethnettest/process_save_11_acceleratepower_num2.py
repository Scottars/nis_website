'''
子系统自身信息：
IP:192.168.127.11
slave：11
port:5001

子系统需要检测的信息
电源电压采样 value1:05 03 07 data crc1 crc2----registerid=07   datatype=int
电源电流采样 value1:05 03 08 data crc1 crc2----registerid=08   datatype=float

'''


import zmq
import struct
import threading
import pymysql
import datetime
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

import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")

    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    try:
        _async_raise(thread.ident, SystemExit)
    except :
        print("Already clear the thread")



def datasavethread(context,datatosave,savingpubaddr):
    db = pymysql.connect(host='localhost', user='scottar', password='wangsai', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()
    # context = zmq.Context()
    savingpub=context.socket(zmq.PUB)

    savingpub.connect(savingpubaddr)
    lengthtosave=len(datatosave)
    # lengthtosave=100
    percentsend=1000
    j=100
    print('in this sleep')
    # time.sleep(20)
    # savingpub.send((str(j) + ',' + str(lengthtosave)).encode())
    lengthtosave=100
    for j in  range(lengthtosave):
        # if j%percentsend==0:
        z=(str(j * 100 / lengthtosave)).encode()
        print('we are in thr for')
        print(z)
        savingpub.send(z)
        time.sleep(1)
        # savingpub.send(str(j)+','+str(lengthtosave))x洗碗
        # item=datatosave[j]
        # for i in range(10):
        #     tmpb = item[i * 36:(i + 1) * 36]
        #     subsys_id, func, register_id, length, v_data = struct.unpack('!bbbbf', tmpb[0:8])
        #     data_time = tmpb[10:36]
        #     sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,%d,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (
        #     subsys_id, register_id, exp_id, v_data, str(data_time, encoding='utf-8'))
        #     cur.execute(sql)
    savingpub.send(str(100).encode())

    db.commit()



def processerfuc(context,url,sync_addr,exp_id_server,topic,exp_id):
    expid_url = "tcp://127.0.0.1:6005"#虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
    # reveiver_url = "ipc://11_Router"
    reveiver_url = "tcp://192.168.127.201:5011"


    expid_sub = context.socket(zmq.SUB)
    # socket_sub_sub.set_hwm(100000)
    expid_sub.connect(expid_url)
    expid_sub.setsockopt(zmq.SUBSCRIBE,topic)
    #
    expid_sub.setsockopt(zmq.SUBSCRIBE,b'expid')

    receiver_dealer = context.socket(zmq.SUB)
    # sock_et_sub_sub.set_hwm(100000)
    # receiver_dealer.setsockopt(zmq.IDENTITY, b'11')
    receiver_dealer.setsockopt(zmq.SUBSCRIBE,b'')

    receiver_dealer.set_hwm(10000000)
    receiver_dealer.connect(reveiver_url)


    displaypubaddr='tcp://192.168.127.200:8011'
    displaypub = context.socket(zmq.PUB)
    displaypub.bind(displaypubaddr)



    saverep=context.socket(zmq.REP)
    saverepaddr='tcp://127.0.0.1:8889'
    saverep.connect(saverepaddr)


    # flagaddr = 'tcp://127.0.0.1:8889'
    # flagpub = context.socket(zmq.PUB)
    # flagpub.connect(flagaddr)



    # # Second, synchronize with publisher
    # syncclient = context.socket(zmq.REQ)
    # syncclient.connect(sync_addr)
    #
    # # send a synchronization request
    # syncclient.send(b'')
    #
    # # wait for synchronization reply
    # syncclient.recv()

    num_package= 0

    #方案2
    #实验批次id
    # sock_exp_id=context.socket(zmq.SUB)
    # sock_exp_id.setsockopt()
    # sock_exp_id.connect(exp_id_server)

    #process monitoring
    sock_monitor_url = "tcp://127.0.0.1:8011"
    sock_process_monitor=context.socket(zmq.REP)
    sock_process_monitor.connect(sock_monitor_url)

    # # Initialize poll set
    poller = zmq.Poller()
    poller.register(expid_sub, zmq.POLLIN)
    poller.register(receiver_dealer,zmq.POLLIN)
    poller.register(sock_process_monitor, zmq.POLLIN)
    poller.register(displaypub,zmq.POLLIN)
    # poller.register(flagpub,zmq.POLLIN)
    poller.register(saverep,zmq.POLLIN)
    counter= 0
    tmptpsend = b''
    datalist=[]

    while True:
        socks = dict(poller.poll())

        if socks.get(sock_process_monitor) == zmq.POLLIN:
            print(sock_process_monitor.recv())
            sock_process_monitor.send(b'I am alive  ' + sock_monitor_url.encode())



        if socks.get(expid_sub) == zmq.POLLIN:

            # 接收xpub的资料，其中已经经过了子系统的筛选
            b = expid_sub.recv()
            print('msg we receive',b)
            if b[0:5] == b'expid': #注意实验id的分发
                exp_id = struct.unpack('!f', b[5:9])[0]
                print(exp_id)
                continue
        if socks.get(receiver_dealer) == zmq.POLLIN:
            b = receiver_dealer.recv()
            counter += 1
            if counter ==1:
                startperf=time.perf_counter()
                thetime=str(datetime.datetime.now()).encode()
                print('The first package received time:',thetime)
            print("Counter num:",counter)
            if counter==100000:

                endperf=time.perf_counter()
                thetime=str(datetime.datetime.now()).encode()
                print('The last package received time:',thetime)
                print('Total Package we have received:',counter)
                print('Processing and saving time cost:',endperf-startperf)
                # break
                #     tmptpsend+=tmpb[4:8]
            tmptpsend += b

            datalist.append(b)
            if counter % 10 == 0:
                displaypub.send(tmptpsend)
                tmptpsend = b''

        if socks.get(saverep) == zmq.POLLIN:
            # 如果来了这个信号,我们就选择去启动数据存储线程， 这个flag 由主线程自动化的发过来，这个是采用在高速数据存储的子系统上面，非高速的子系统就不必要了
            # 对于这种高速的，我们如何确定什么时候开始进行数据存储。
            b=saverep.recv()
            savingpubaddr="tcp://127.0.0.1:8888"
            if b==b'startsaving':
                print('ready to run datasavethread')
                # t = threading.Thread()
                t = threading.Thread(target=datasavethread, args=(context,datalist,savingpubaddr))
                t.start()
                # time.sleep(5)
                # stop_thread(t)
                datalist = []
                #此时应当告诉主线程，我现在能够继续进行新的数据解析过程了。
                saverep.send(b'start saving thread,ready to recv data')
            else:
                print(t)
                stop_thread(t)
                print('we have thie thread')
                saverep.send(b'stopped the thread')





if __name__ == '__main__':

    #zeroMQ的通信协议可以采用的ipc
    context = zmq.Context()
    import threading





    # url = "tcp://127.0.0.1:6005"
    url = "ipc://main"  #虽然这个协议是进程间的，但是是不是可以理解为在进程间寻找要链接的内容。
    #而如果是inproc 则是在线程间寻找inproc 对应的协议，很有可能就没有这样的协议

    sync_addr = 'ipc://main_sync_server'

    exp_id_server='ipc://exp_id_server'

    import threading
    #这个时候定义一个需要订阅子系统
    main_content=b'\x03\03'   #目前这个用来订阅各个子系统的内容，然后内部对数据进行分析
    # main_content=b''sub

    #这个定义了这个系统包含了哪些寄存器
    # sub_content = [struct.pack('!b',1),struct.pack('!b',2),struct.pack('!b',3),struct.pack('!b',4),struct.pack('!b',5),struct.pack('!b',6),struct.pack('!b',7),struct.pack('!b',8),struct.pack('!b',9),struct.pack('!b',10)]
    sub_content = [struct.pack('!b',12),struct.pack('!b',13)]   #12 和 13 分别对应0b  和 0c
    #传入一个第几次实验的参数  #默认认为是第0次实验
    exp_id = 0
    #启动该进程对该子系统中的数据进行处理
    processerfuc(context,url,sync_addr,exp_id_server,sub_content[1],exp_id)


    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''

