#-*-coding:utf-8-*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os,signal,sys
from pyqtgraph.Qt import QtGui,QtCore, USE_PYSIDE, USE_PYQT5,QtWidgets
import  pymysql
import  multiprocessing
import  numpy as np
import ManagerPanel
import struct
import nis_hsdd

import  pyqtgraph as pg
import pyqtgraph.exporters
from pyqtgraph.ptime import time
# 声明一个应用程序
app = QtGui.QApplication([])


import time
import  zmq
import threading
global data_pgpowerx,data_pgpowey
data_pgpowerx=[]
data_pgpowery=[]

global savingprogress11value
savingprogress11value=0

import inspect
import ctypes
import nis_hsdd_configfile
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
    # try:
    _async_raise(thread.ident, SystemExit)
    # except "invalid thread id":
    #     print("Already clear the thread")


import process_manager
class ChildDialogWin2(QDialog,process_manager.Ui_Dialog):
    def __init__(self):
        super(ChildDialogWin2,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("Process Monitor GUI")


        print('we are in init')
        self.button_function_initial()

        self.initilization()

    def button_function_initial(self):
        self.pushButton_3.clicked.connect(self.start_process_monitor)
        self.pushButton_4.clicked.connect(self.stop_process_monitor)

        self.pushButton_15.clicked.connect(self.set_exp_id)


        ####################### Debug Mode ####################

        # self.pushButton_192.clicked.connect(self.run_level_2_11_thread)
        # self.pushButton_194.clicked.connect(self.stop_level_2_11_thread)
        #
        # self.pushButton_187.clicked.connect(self.start_level_2_11_receive)
        # self.pushButton_189.clicked.connect(self.stop_level_2_11_receive)
        #
        # self.pushButton_188.clicked.connect(self.start_level_3_11)
        # self.pushButton_191.clicked.connect(self.stop_level_3_11)


        ###################Menu Mode#########################
        #对于实现udp  数据开始接收应当由内部含事故自行运行
        #水冷
        self.pushButton_26.clicked.connect(self.menu_start_level_2_01_udp)
        self.pushButton_28.clicked.connect(self.menu_stop_level_2_01_udp)
        #供气
        self.pushButton_56.clicked.connect(self.menu_start_level_2_08_udp)
        self.pushButton_57.clicked.connect(self.menu_stop_level_2_08_udp)
        #pgpower
        self.pushButton_56.clicked.connect(self.menu_start_level_2_08_udp)
        self.pushButton_57.clicked.connect(self.menu_stop_level_2_08_udp)


        #
        # self.pushButton_17.clicked.connect(self.run_pararead_thread)
        # self.pushButton_19.clicked.connect(self.stop_pararead_thread)

        # self.pushButton_20.clicked.connect(self.start_epics)
        # self.pushButton_21.clicked.connect(self.stop_epics)

    def initilization(self):
        self.context = zmq.Context()

        #水冷
        self.level_2_req_01 = self.context.socket(zmq.REQ)
        self.level_2_req_01addr =  nis_hsdd_configfile.level_2_01_watercool_req_addr
        self.level_2_req_01.connect(self.level_2_req_01addr)
        self.level_2_req_01.setsockopt(zmq.RCVTIMEO,100) #  设定超时时间为5s
        self.level_2_req_01.setsockopt(zmq.SNDTIMEO,100) #  设定超时时间为5s

        self.level_3_req_01 = self.context.socket(zmq.REQ)
        self.level_3_req_01addr = nis_hsdd_configfile.level_3_01_watercool_req_addr
        self.level_3_req_01.connect(self.level_3_req_01addr)
        self.level_3_req_01.setsockopt(zmq.RCVTIMEO, 100)
        self.level_3_req_01.setsockopt(zmq.SNDTIMEO, 100)

        #供气监测
        self.level_2_req_03 = self.context.socket(zmq.REQ)
        self.level_2_req_03addr =  nis_hsdd_configfile.level_2_03_gascontrol_req_addr
        self.level_2_req_03.connect(self.level_2_req_03addr)
        self.level_2_req_03.setsockopt(zmq.RCVTIMEO,100) #  设定超时时间为5s
        self.level_2_req_03.setsockopt(zmq.SNDTIMEO,100) #  设定超时时间为5s

        self.level_3_req_03 = self.context.socket(zmq.REQ)
        self.level_3_req_03addr = nis_hsdd_configfile.level_3_03_gascontrol_req_addr
        self.level_3_req_03.connect(self.level_3_req_03addr)
        self.level_3_req_03.setsockopt(zmq.RCVTIMEO,100)
        self.level_3_req_03.setsockopt(zmq.SNDTIMEO,100)

        # 引出电源 pg power
        self.level_2_req_08 = self.context.socket(zmq.REQ)
        self.level_2_req_08addr =  nis_hsdd_configfile.level_2_08_leadintoutpower_req_addr
        self.level_2_req_08.connect(self.level_2_req_08addr)
        self.level_2_req_08.setsockopt(zmq.RCVTIMEO,100) #  设定超时时间为5s
        self.level_2_req_08.setsockopt(zmq.SNDTIMEO,100) #  设定超时时间为5s

        self.level_3_req_08 = self.context.socket(zmq.REQ)
        self.level_3_req_08addr = nis_hsdd_configfile.level_3_08_leadingoutpower_req_addr
        self.level_3_req_08.bind(self.level_3_req_08addr)
        self.level_3_req_08.setsockopt(zmq.RCVTIMEO,100)
        self.level_3_req_08.setsockopt(zmq.SNDTIMEO,100)


        # pararead
        self.level_3_req_pararead = self.context.socket(zmq.REQ)
        self.level_3_req_parareadaddr = nis_hsdd_configfile.level_3_para_read_req_addr
        self.level_3_req_pararead.bind(self.level_3_req_parareadaddr)
        self.level_3_req_pararead.setsockopt(zmq.RCVTIMEO,100)
        self.level_3_req_pararead.setsockopt(zmq.SNDTIMEO,100)




        ## Start epics tcp server thread
        self.tcp_epics_thread = tcp_receiving_thread()
        self.tcp_epics_thread.trigger.connect(self.epics_autoprocess)



    def process_monitor(self):
        print('start process monitor ')
        self.flag_monitor= True
        while True:
            if self.flag_monitor:
                time.sleep(1)
                ####################level 2  08##################################
                # 水冷系统
                try:
                    self.level_2_req_01.send(b'udp alive?')
                except:
                    print('level 2 01: sendtime out')

                try:
                    x = self.level_2_req_01.recv()
                    if x == b'udp yes':
                        self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_29.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_202.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_29.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_70.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_29.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_70.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    print('level 2 01: udp not online')
                try:
                    self.level_2_req_01.send(b'udp alive?')
                except:
                    print('level 2 01: sendtime out')

                # 供气系统
                try:
                    x = self.level_2_req_03.recv()
                    if x == b'udp yes':
                        self.pushButton_172.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_43.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_153.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_172.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_43.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_153.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_172.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_43.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_153.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    print('level 2 03: udp not online')
                # 引出电源 pgpwoer 08
                try:
                    x = self.level_2_req_08.recv()
                    if x == b'udp yes':
                        self.pushButton_109.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_59.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_224.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_109.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_59.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_224.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_109.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_59.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_224.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    print('level 2 08: udp not online')


                #########level 3  11###############################
                #水冷系统
                try:
                    self.level_3_req_01.send(b'process alive?')
                except:
                    print('level 3 01: sendtime out')
                try:
                    x = self.level_3_req_01.recv()
                    if x == b'process yes':
                        self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_32.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_203.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_32.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_203.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_32.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_203.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                    print('level 3 01: process not online')
                #  供气系统 03
                try:
                    self.level_3_req_03.send(b'process alive?')
                except:
                    print('level 3 03: sendtime out')
                try:
                    x = self.level_3_req_03.recv()
                    if x == b'process yes':
                        self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_42.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_40.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_40.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    print('level 3 03: process not online')
                #  引出电源系统 08
                try:
                    self.level_3_req_08.send(b'process alive?')
                except:
                    print('level 3 08: sendtime out')
                try:
                    x = self.level_3_req_08.recv()
                    if x == b'process yes':
                        self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_42.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                        self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                    else:
                        self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_40.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                        self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                except:
                    self.pushButton_175.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_40.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    self.pushButton_151.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                    print('level 3 08: process not online')


                ### monitor  para read for epics
                try:
                    print('try to send process 11 alive')
                    self.level_3_req_pararead.send(b'pararead alive?')
                except:
                    print('send time out')
                try:
                    x = self.level_3_req_pararead.recv()
                    print('x', x)
                    if x == b'pararead yes':
                        self.pushButton_18.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")

                        print('Received Msg:', x)
                    else:
                        self.pushButton_18.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                except:
                    self.pushButton_18.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                    print('udp not online')


    def start_process_monitor(self):
        print('we have start udp update process')
        self.process_monitor_thread = threading.Thread(target=self.process_monitor)
        self.process_monitor_thread.start()

    def stop_udp_process_monitor(self):
        print('we have stoppend update udp process ')
        self.flag_monitor = False
        time.sleep(1)
        stop_thread(self.process_monitor_thread)

    def menu_start_level_2_01_udp(self):
        try:
            self.level_2_req_01.send(b'start')
        except:
            print('start udp send timeout')
            pass

        try:
            x = self.level_2_req_01.recv()
            print('we have received ', x)

            if x == b'start received':
                print('can we set this')
                self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_123.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_204.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_123.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_204.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            print('not online')

    def menu_stop_level_2_01_udp(self):
        try:
            self.level_2_req_01.send(b'stop')
        except:
            print('stop udp send time out')
            pass
        try:
            x = self.level_2_req_01.recv()
            if x == b'stop received':
                self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_123.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_204.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                print('Received Msg:', x)
        except:
            self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_123.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_204.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            print('not online')

    def menu_start_level_2_03_udp(self):
        try:
            self.level_2_req_03.send(b'start')
        except:
            print('start udp send timeout')
            pass

        try:
            x = self.level_2_req_03.recv()
            print('we have received ', x)

            if x == b'start received':
                print('can we set this')
                self.pushButton_168.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_125.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_152.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            self.pushButton_168.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_125.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_152.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            print('not online')

    def menu_stop_level_2_03_udp(self):
        try:
            self.level_2_req_03.send(b'stop')
        except:
            print('stop udp send time out')
            pass

        try:
            x = self.level_2_req_03.recv()
            if x == b'stop received':
                self.pushButton_168.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_125.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_152.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                print('Received Msg:', x)
        except:
            self.pushButton_168.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_125.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_152.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            print('not online')

    def menu_start_level_2_08_udp(self):
        try:
            self.level_2_req_08.send(b'start')
        except:
            print('start udp send timeout')
            pass

        try:
            x = self.level_2_req_08.recv()
            print('we have received ', x)

            if x == b'start received':
                print('can we set this')
                self.pushButton_39.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_134.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                self.pushButton_223.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            self.pushButton_39.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_134.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            self.pushButton_223.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
            print('not online')

    def menu_stop_level_2_08_udp(self):
        try:
            self.level_2_req_08.send(b'stop')
        except:
            print('stop udp send time out')
            pass

        try:
            x = self.level_2_req_08.recv()
            if x == b'stop received':
                self.pushButton_39.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_134.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")
                self.pushButton_223.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                print('Received Msg:', x)
        except:
            self.pushButton_39.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_134.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.pushButton_223.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            print('not online')

    def run_level_2_11_thread(self):
        try:
            self.level_2_req_11.send(b'run udp thread')
        except:
            print('run udp thread send ')
        try:
            x = self.level_2_req_11.recv()
            print('we have received ', x)
            if x == b'run udp thread received':
                print('can we set this')
                self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            print('not online')


    def stop_level_2_11_thread(self):
        try:
            self.level_2_req_11.send(b'stop udp thread')
        except:
            print('stop udp thread timeout')
            pass


        try:
            x = self.level_2_req_11.recv()
            print('we have received ', x)
            if x == b'stop udp thread received':
                print('can we set this')
                self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            print('not online')


    def start_level_2_11_receive(self):
        try:
            self.level_2_req_11.send(b'start')
        except:
            print('start udp send timeout')
            pass

        try:
            x = self.level_2_req_11.recv()

            print('we have received ',x)

            if x == b'start received':
                print('can we set this')
                self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
                print('Received Msg:', x)
        except:
            print('not online')
    def stop_level_2_11_receive(self):

        try:
            self.level_2_req_11.send(b'stop')
        except:
            print('stop udp send time out')
            pass

        try:
            x = self.level_2_req_11.recv()
            if x == b'stop received':
                self.pushButton.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

                print('Received Msg:', x)
        except:
            print('not online')

    def start_level_3_11(self):
        print('we are in start level 3 11')
        try:
            self.level_3_req_11.send(b'run process thread')
        except:
            print('send run process thread tiemeout ')
            pass
        try:
            x = self.level_3_req_11.recv()
            if x == b'run process thread received':
                print('start level 3 process is sent')
            else:
                print('not received correctly')
        except:
            print('level 3  11 daemon thread is not online')
    def stop_level_3_11(self):
        print('we are in stop level 3 11')
        try:
            self.level_3_req_11.send(b'stop process thread')
            x = self.level_3_req_11.recv()
            if x == b'stop process thread received':
                print('stop level 3 process is sent')
            else:
                print('not received correctly')
        except:
            print('level 3  11 daemon thread is not online')


    def start_saving_11(self):
        print('In start saving ')
        global savingprogress11value

        self.flag11stop=False
        try:
            self.level_3_req_11.send(b'run saving thread')
        except:
            pass

        try:
            x = self.level_3_req_11.recv()
            savingprogress11value = 0
            self.progressBar.setValue(savingprogress11value)
            self.label_4.setText('Saving')
            self.pushButton_14.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")
            self.timersaving11.start(1000)
            self.Saving11thread.start()
            # 使能停止按钮
            self.pushButton_11.setEnabled(True)
        except:
            print('Timeout In req receive')

    def stop_saving_11(self):
        try:
            self.level_3_req_11.send(b'stop saving thread')
            x = self.level_3_req_11.recv()
            self.label_4.setText('Stop Saving')
            self.pushButton_14.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

        except:
            print('Timeout in stop saving')



        self.timersaving11.stop()

    def saving_progressbar_update(self):
        global savingprogress11value
        print('currenalue ', savingprogress11value)
        self.progressBar.setValue(savingprogress11value)
        if savingprogress11value==100:
            self.label_4.setText('Done')
        print("updating the progress bar")
        pass


    def set_exp_id(self):
        # 通过好几个套接字的接口然后，设定该实验id下去。
        #
        exp_id = self.spinBox.value()

        print(type(exp_id))
        ###########set exp id to level 2 ##############
        ## send id to subsys 11
        try:
            self.level_3_req_11.send(b'exp_id'+str(exp_id).encode())
        except:
            self.label_7.setText('error')
            print('exp_id send time out for 11')

        try:
            x = self.level_3_req_11.recv()
            if x == b'exp_id received':
                self.label_7.setText(str(exp_id))
        except:
            self.label_7.setText('error')

            print('exp_id recv time out for 11 ')
        ## set exp id to pv  para read

        try:
            self.level_3_req_pararead.send(b'exp_id' + str(exp_id).encode())
        except:
            self.label_12.setText('error')
            print('exp_id send time out for 11')

        try:
            x = self.level_3_req_pararead.recv()
            if x == b'exp_id received':
                self.label_12.setText(str(exp_id))
                self.label_14.setText(str(exp_id))
        except:
            self.label_12.setText('error')

            print('exp_id recv time out for pararead ')
        pass

    def run_pararead_thread(self):
        #this is a level 3 function
        try:
            self.level_3_req_pararead.send(b'run pararead thread')
        except:
            print('send run level_3_req_pararead thread tiemeout ')
            pass
        try:
            x = self.level_3_req_pararead.recv()
            if x == b'run pararead thread received':
                print('run level_3_req_pararead is sent')
            else:
                print('not received correctly')
        except:
            print('level_3_req_pararead daemon thread is not online')

    def stop_pararead_thread(self):
        #this is a level 3 function
        try:
            self.level_3_req_pararead.send(b'stop pararead thread')
        except:
            print('send run level_3_req_pararead thread tiemeout ')
            pass
        try:
            x = self.level_3_req_pararead.recv()
            if x == b'stop pararead thread received':
                print('run level_3_req_pararead is sent')
            else:
                print('not received correctly')
        except:
            print('level_3_req_pararead daemon thread is not online')


    def start_epics(self):
        print('start tcp epics thread ')
        self.tcp_epics_thread.start()
        self.tcp_epics_thread.startagain()

    def stop_epics(self):
        print('stop tcp epics thread ')

        self.tcp_epics_thread.stop()
    def epics_autoprocess(self,msg):
        print('get the action in main',msg)

class uitimerthread(QtCore.QThread):
    trigger = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # # Initialize poll set
        # self.poller = zmq.Poller()
        # self.poller.register(self.zmqsub,zmq.POLLIN)
        print('in 0')

        # self.app1=QtGui.QGuiApplication([])
        self.p=pg.plot()

        # self.p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        self.curve = self.p.plot()
        print('in 1')
        self.data = np.random.normal(size=(50, 5000))
        self.ptr = 0
        self.fps = None
        print('in 2')
        self.flagupdate=True
    def run(self):
        print('in run')
        while True:
            # time.sleep(0.01)
            if self.flagupdate:
                time.sleep(0.01)
                self.update()
    def update(self):
        # print('in 4 ')
        # global curve, data, ptr, p, lastTime, fps
        # self.curve.setData(self.data[self.ptr % 10])
        # self.ptr += 1
        global data_pgpower
        # print('datapower',data_pgpower)
        self.curve.setData(data_pgpower)

    def startsub(self):
        print('in ')
        self.flagupdate=True

        # self.run()

    def  stop(self):
        print('stop update')
        self.flagupdate=False


class tcp_receiving_thread(QtCore.QThread):
    '''
    说明：
    此线程的作用模拟底层被控设别而用于接收epics 的对不同进程的控制指令。
    更具体而言：
    1、具有收到管理中心启停的功能
    2、工作在tcp服务器模式下，能够接收到来自ioc发过来的不同进程启停的功能
    3、

    '''
    trigger=QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.flagtcpforepics = True


    def run(self):

        # 通过触发不同的函数的去调用主线程中的函数，这个时候就是属于来自epics 的自动控制
        while True:
            if self.flagtcpforepics:
                print('in tcp receive part')

                self.filestr = "hhaha "
                self.trigger.emit(self.filestr)


            else:
                pass

            time.sleep(1)


    def stop(self):
        self.flagtcpforepics= False
        print('we have stop the thread in stop')
    def startagain(self):
        self.flagtcpforepics = True




if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # main = MainDialogImgBW()
    # main.show()
    # #app.installEventFilter(main)
    # sys.exit(app.exec_())
    import sys

    ui = ChildDialogWin2()
    # ui.setupUi(win)
    ui.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

