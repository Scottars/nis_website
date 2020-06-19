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
mutex = threading.Lock()
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
        
        ## 关于上面的这个线程的停止过程，我们是没有办法去停止一个阻塞过程的


global flagtosave
flagtosave =False
global exp_id
exp_id=0
global data_list
data_list=[]
global flagtoreceive
flagtoreceive= False

def saving_threadfunc(context):

    db = pymysql.connect(host='localhost', user='scottar', password='wangsai', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()
    # context = zmq.Context()
    savingpubaddr = "tcp://127.0.0.1:8888"

    savingpub=context.socket(zmq.PUB)
    global data_list
    mutex.acquire()
    datatosave =data_list
    mutex.release()

    savingpub.connect(savingpubaddr)
    lengthtosave=len(datatosave)
    # lengthtosave=100
    # percentsend=1000
    # j=100
    print('in this sleep')
    # time.sleep(20)
    # savingpub.send((str(j) + ',' + str(lengthtosave)).encode())
    lengthtosave=100
    for j in  range(lengthtosave):
        # if j%percentsend==0:\
        z=(str(j * 100 / lengthtosave)).encode()
        # print('Saving length',lengthtosave,'curren row',j)
        savingpub.send(z)
        time.sleep(1)
        # savingpub.send(str(j)+','+str(lengthtosave))

        if not flagtosave:
            print('in here')
            break

    #     item=datatosave[j]
    #     for i in range(10):
    #         tmpb = item[i * 36:(i + 1) * 36]
    #         subsys_id, func, register_id, length, v_data = struct.unpack('!bbbbf', tmpb[0:8])
    #         try:
    #             data_time = tmpb[10:36]
    #             sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,%d,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (
    #             subsys_id, register_id, exp_id, v_data, str(data_time, encoding='utf-8'))
    #             cur.execute(sql)
    #         except:
    #             print('date time error ')
    # savingpub.send(str(100).encode())

    db.commit()


def process_threadfunc(context):
    receiver_subaddr= 'tcp://192.168.127.201:5011'
    receiver_sub = context.socket(zmq.SUB)
    receiver_sub.setsockopt(zmq.SUBSCRIBE,b'')

    receiver_sub.set_hwm(10000000)
    receiver_sub.connect(receiver_subaddr)
    receiver_sub.setsockopt(zmq.RCVTIMEO,1000)



    displaypubaddr='tcp://192.168.127.200:10011'
    displaypub = context.socket(zmq.PUB)
    displaypub.bind(displaypubaddr)

    counter= 0
    tmptpsend = b''
    global data_list,flagtoreceive
    while True:
        # time.sleep(1)
        if flagtoreceive:
            try:
                b = receiver_sub.recv()
                counter += 1
                if counter ==1:
                    startperf=time.perf_counter()
                    thetime=str(datetime.datetime.now()).encode()
                    print('The first package received time:',thetime)
                    for i in range(10):
                        tmpb = b[i * 36:(i + 1) * 36]

                        tmptpsend += tmpb[4:8]
                print("Counter num:",counter)
                if counter==100000:

                    endperf=time.perf_counter()
                    thetime=str(datetime.datetime.now()).encode()
                    print('The last package received time:',thetime)
                    print('Total Package we have received:',counter)
                    print('Processing and saving time cost:',endperf-startperf)
                    # break
                    #     tmptpsend+=tmpb[4:8]
                for i in range(10):
                    tmpb = b[i * 36:(i + 1) * 36]

                    tmptpsend += tmpb[4:8]
                data_list.append(b)
                if counter % 10 == 0:

                    displaypub.send(tmptpsend)
                    tmptpsend = b''
            except:
                print('Timeout in receiver')



def daemon_thread(context):
    print('we are in damenon thread')

    daemon_zmq= context.socket(zmq.REP)
    daemon_zmqaddr = "tcp://192.168.127.200:9011"
    daemon_zmq.connect(daemon_zmqaddr)
    daemon_zmq.setsockopt(zmq.RCVTIMEO,1000)



    process_thread=threading.Thread(target=process_threadfunc,
                                    args=(context,))
    saving_thread = threading.Thread(target=saving_threadfunc,
                                     args=(context,))


    global flagtosave,flagtoreceive,data_list,exp_id

    while True:

        try:
            b = daemon_zmq.recv()
            print('Msg received:',b)
            if b==b'process alive?':
                if process_thread.is_alive():

                    print('we are sending process alive')
                    daemon_zmq.send(b'process yes')
                else:
                    print('we are sending process no')
                    daemon_zmq.send(b'process no')

            elif b==b'run process thread':
                if process_thread.is_alive():
                    print('it is alive and we sopped the thread')
                    flagtoreceive = False
                    time.sleep(1)
                    stop_thread(process_thread)
                    pass
                else:
                    print('start process thread')
                    flagtoreceive = False
                process_thread = threading.Thread(target=process_threadfunc,
                                                  args=(context,))
                flagtoreceive = True
                process_thread.start()
                # 从新开始该线程的时候，我们将重新更新data list
                data_list=[]
                daemon_zmq.send(b'run process thread received')
            elif b == b'stop process thread':
                if process_thread.is_alive():
                    print('the thread is alvie ')
                    print(process_thread)
                    flagtoreceive = False
                    # time.sleep(0.1)
                    time.sleep(1)

                    stop_thread(process_thread)
                    print('we have stoppend th e  data ')
                    # stop_thread(process_thread)

                else:
                    flagtoreceive = False

                    pass
                daemon_zmq.send(b'stop process thread received')


            elif b == b'run saving thread':
                if saving_thread.is_alive():
                    print('saving thread is alive ')
                    flagtosave = False

                    stop_thread(saving_thread)
                    # stop_thread(saving_thread)
                else:
                    print('t is not none but is not alive which is the saving is done')
                    flagtosave = False

                    stop_thread(saving_thread)
                    # stop_thread(saving_thread)

                flagtosave = True
                saving_thread = threading.Thread(target=saving_threadfunc,
                                                 args=(context,))

                saving_thread.start()
                daemon_zmq.send(b'start saving thread received')
            elif b == b'stop saving thread':
                flagtosave = False

                stop_thread(saving_thread)

                print('we have thie thread')
                daemon_zmq.send(b'stop saving thread received')

            elif b[0:6]== b'exp_id':
                exp_id = int(b[6:].decode("utf-8"))
                print(exp_id)
                print('new exp id is:',exp_id)
                daemon_zmq.send(b'exp_id received')

        except zmq.error.Again:
            print('daemon received timeout')




if __name__ == '__main__':

    #zeroMQ的通信协议可以采用的ipc
    context = zmq.Context()
    import threading







    import threading
    #这个时候定义一个需要订阅子系统
    main_content=b'\x03\03'   #目前这个用来订阅各个子系统的内容，然后内部对数据进行分析

    t1=threading.Thread(target=daemon_thread,args=(context,))
    t1.start()
    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''

