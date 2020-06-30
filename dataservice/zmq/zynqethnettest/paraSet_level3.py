'''
    这个文件的代码作用是接收来自于控制中心的id，如果接收到来自于控制中心最新的id 之后，就 进行对epics 中心的pv变量的读取。

'''


import threading
import  zmq
import  time


# 停止线程
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
    except:
        print("Already clear the thread")


# 读取pv变量线程
# 将读取得到的pv变量的数值与相对应的系统实验的id对应在一起存储到数据库当中。
def pararead_threadfunc():

    while  True:
        time.sleep(1)
        print('we are reading para from epcis ')




# 守护线程

def paraRead_daemon_thread(context):
    daemon_zmq = context.socket(zmq.REP)
    daemon_zmqaddr = "tcp://192.168.127.200:11011"
    daemon_zmq.connect(daemon_zmqaddr)
    daemon_zmq.setsockopt(zmq.RCVTIMEO,1000)

    pararead_thread = threading.Thread(target=pararead_threadfunc,args=())

    while True:

        try:
            b = daemon_zmq.recv()

            if b == b'pararead alive?':
                if pararead_thread.is_alive():
                    print('we are sending process alive')
                    daemon_zmq.send(b'pararead yes')
                else:
                    print('we are sending process no')
                    daemon_zmq.send(b'pararead no')

            elif b == b'run pararead thread':
                if pararead_thread.is_alive():
                    print('it is alive and we sopped the thread to start again')
                    stop_thread(pararead_thread)
                    pass
                else:
                    print('directly start process thread')

                pararead_thread = threading.Thread(target=pararead_threadfunc,
                                                  args=())
                pararead_thread.start()

                daemon_zmq.send(b'run pararead thread received')
            elif b == b"stop pararead thread":
                if pararead_thread.is_alive():
                    print('the thread is alvie ')

                    stop_thread(pararead_thread)


                else:
                    print('dayin dangqinag ')

                    pass
                daemon_zmq.send(b'stop pararead thread received')
            elif b[0:6]== b'exp_id':
                exp_id = int(b[6:].decode("utf-8"))
                print(exp_id)
                print('new exp id is:',exp_id)
                daemon_zmq.send(b'exp_id received')
            else:
                pass
        except:
            print('Timeout in daemon receiver')







if __name__ == "__main__":
    context = zmq.Context()

    t1 = threading.Thread(target=paraRead_daemon_thread,args=(context,))
    t1.start()