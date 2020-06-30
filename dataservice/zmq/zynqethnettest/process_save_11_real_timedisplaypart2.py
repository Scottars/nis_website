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
import threading
import pymysql
import datetime

import time
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
    receiver_sub.setsockopt(zmq.RCVTIMEO,1000)
    receiver_sub.connect(receiver_subaddr)



    counter= 0
    tmptpsend = b''
    global data_list,flagtoreceive
    while True:

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

                    # tmptpsend += tmpb[4:8]
            except:
                print('Timeout in receiver')




if __name__ == '__main__':

    #zeroMQ的通信协议可以采用的ipc
    context = zmq.Context()
    import threading
    process_threadfunc(context)



