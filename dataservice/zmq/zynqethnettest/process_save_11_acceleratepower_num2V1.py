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
import nis_hsdd_configfile
mutex = threading.Lock()
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




def process_threadfunc(context):
    receiver_subaddr= nis_hsdd_configfile.level_2_11_leadintoutpower_sub_addr
    receiver_sub = context.socket(zmq.SUB)
    receiver_sub.setsockopt(zmq.SUBSCRIBE,b'')

    receiver_sub.set_hwm(10000000)
    receiver_sub.connect(receiver_subaddr)
    receiver_sub.setsockopt(zmq.RCVTIMEO,1000)

    counter= 0
    global flagtoreceive
    db = pymysql.connect(host='localhost', user='scottar', password='wangsai', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()

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
                print("Counter num:",counter)
                if counter==100000:

                    endperf=time.perf_counter()
                    thetime=str(datetime.datetime.now()).encode()
                    print('The last package received time:',thetime)
                    print('Total Package we have received:',counter)
                    print('Processing and saving time cost:',endperf-startperf)
                    # break
                    #     tmptpsend+=tmpb[4:8]
                # for i in range(10):
                #     tmpb = b[i * 36:(i + 1) * 36]
                #     subsys_id, func, register_id, length, v_data = struct.unpack('!bbbbf', tmpb[0:8])
                #     try:
                #         data_time = tmpb[10:36]
                #         sql = "INSERT INTO v_data_monitor (subsys_id,register_id,exp_id,v_data,v_data_time) values (%d,%d,%d,%f,str_to_date('\%s\','%%Y-%%m-%%d %%H:%%i:%%s.%%f'))" % (
                #         subsys_id, register_id, exp_id, v_data, str(data_time, encoding='utf-8'))
                #         cur.execute(sql)
                #     except:
                #         print('date time error ')


            except:
                print('Timeout in receiver')



def daemon_thread(context):
    print('we are in damenon thread')

    daemon_zmq= context.socket(zmq.REP)
    daemon_zmqaddr = nis_hsdd_configfile.level_3_11_leadingoutpower_req_addr
    daemon_zmq.connect(daemon_zmqaddr)
    daemon_zmq.setsockopt(zmq.RCVTIMEO,1000)



    process_thread=threading.Thread(target=process_threadfunc,
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
                    stop_thread(process_thread)

                    pass
                daemon_zmq.send(b'stop process thread received')

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
    #这个时候定义一个需要订阅子系统

    t1=threading.Thread(target=daemon_thread,args=(context,))
    t1.start()
    '''
    由于我们的这些进程实际上切换的还算是比较频繁的，我们是否应当考虑将其写入到一个脚本中，然后采用多线程的工作而不是多进程的工作的方式，因为如果是多进程的工作的话
    导致切换过程中消耗的资源太大，实际上就不太好了哦哦、  可能还会导致整体彗星的速度变慢
    
    '''

