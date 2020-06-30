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


class zmqrecvthread(QtCore.QThread):
    trigger=QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.context=zmq.Context()
        self.zmqsub=self.context.socket(zmq.SUB)
        self.zmqsub.setsockopt(zmq.SUBSCRIBE,b'')
        # self.subaddr='tcp://192.168.127.200:10011'
        self.subaddr='tcp://192.168.127.201:5011'
        # self.subaddr='inproc://iiii'
        print('in the thread init')
        self.zmqsub.connect(self.subaddr)
        self.flag=0
        # # Initialize poll set
        # self.poller = zmq.Poller()
        # self.poller.register(self.zmqsub,zmq.POLLIN)

    def run(self):
        global  data_pgpower
        global pic2
        print('we are running ')
        print(self.subaddr)
        self.flag=1
        i=1
        counter=0
        while True:
            # socks = dict(self.poller.poll())
            #
            # if socks.get(self.zmqsub) == zmq.POLLIN:
            #     '''
            #     data struct:
            #         x_value, y_value
            #         通过端口号进行识别
            #
            #     '''
            try:
                # b = self.zmqsub.recv(zmq.DONTWAIT)
                b = self.zmqsub.recv()
                # print('recbeiving b',b)
                counter+=1
                # print('num',counter,'content:',struct.unpack('!f',b[0:4]))
                for i in range(10):
                    tmpb = b[i * 36:(i + 1) * 36]
                    tmpby = tmpb[4:8]
                    tmpbx = tmpb[10:36]

                    try:
                        xmin = int(tmpbx[-12:-10].decode())
                        xs = float(tmpbx[-9:].decode())
                        x = xmin*60+xs
                        y = struct.unpack('!f', tmpby)[0]

                        # print('x:',x,'y:',y)
                        data_pgpowerx.append(x)
                        data_pgpowery.append(y)
                    except:
                        print('time sample error')

                # print('we get here')
                # pic2.setData(data_pgpower)
                # print(data_pgpower)
            except zmq.Again:
                print('TO recv again')
                pass




    def stop(self):
        self.flag=0
        print('we have stop the thread in stop')



class Savingrecvthread(QtCore.QThread):
    trigger1=QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.context = zmq.Context()
        self.recvsub11 = self.context.socket(zmq.SUB)
        self.recvsub11addr = 'tcp://127.0.0.1:8888'
        self.recvsub11.setsockopt(zmq.SUBSCRIBE, b'')
        self.recvsub11.bind(self.recvsub11addr)
        print('in here 111')
        self.recvsub11.setsockopt(zmq.RCVTIMEO, 2000)

        self.flag11stop = False
    def run(self):
        global savingprogress11value
        print('canwe in here')

        while True:
            if self.flag11stop:
                break
            else:
                try:
                    x = self.recvsub11.recv()
                    print('x',x)
                    step = int(float(x.decode("utf-8")))
                    savingprogress11value = step
                    if step==100:
                        print('already done')
                        break
                except:
                    print('chaoshi')

    def stop(self):
        self.flag11stop=True
        print('we have stop the thread in stop')




class ChildDialogWin(QDialog,nis_hsdd.Ui_Dialog):
    def __init__(self):
        super(ChildDialogWin,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("HSDD Manager GUI")
        self.setMinimumSize(0,0)
        self.p= self.graphicsView
        self.p2=self.graphicsView_2
        self.p3 = self.graphicsView_3


        self.data3 = np.empty(100)
        self.ptr3 = 0
        self.ptrtmp = 0
        self.trix, self.triy = self.triangle_wave(0, 1, 0.01, 2, 2)
        self.initlizefig()

        print('we are in init')

        self.pushButton.clicked.connect(self.testfunc)

        self.pushButton_2.clicked.connect(self.stopupdate)
        self.pushButton_3.clicked.connect(self.startRecving)
        self.pushButton_4.clicked.connect(self.stopRecving)
        self.pushButton_5.clicked.connect(self.clearData)
        self.pushButton_6.clicked.connect(self.exportdataup)
        self.pushButton_7.clicked.connect(self.exportdatadown)
        self.pushButton_9.clicked.connect(self.exportfig)

        self.zmqrecv = zmqrecvthread()
        # self.zmqrecv.__init__()
        # self.zmqrecv.trigger.connect(self.zmqrecvcallback)


    def initlizefig(self):
        self.p.setDownsampling(mode='subsample')
        self.p2.setDownsampling(mode='subsample')


        self.p.setClipToView(True)
        self.p2.setClipToView(True)
        # self.p3.setClipToView(True)
        self.p.setLabel("left","value",units='V')
        self.p.setLabel("bottom","Timestamp",units='s')
        self.p.setTitle('Latest 1W Data')

        self.p2.setLabel("left","value",units='V')
        self.p2.setLabel("bottom","Timestamp",units='s')
        self.p2.setTitle("Accumulate Data")
        # self.p3.setLabel("left","valuess",units='us')
        # self.p3.setLabel("bottom","Timestamp",units='us')
        self.p.setBackground('w')
        self.p2.setBackground('w')
        # self.p2.setBackground('r')


        self.curve = self.p.plot(pen=(0,0,0))
        self.curve2 = self.p2.plot(pen=(0,0,0))
        self.curve2sub= self.p2.plot()




        # self.data3=self.triy
        self.trix, self.triy = self.triangle_wave(0, 1, 0.01, 2, 2)
        self.scatter = self.p3.plot(pen=(0,0,0), symbol='o')
        # self.scatter = self.p3.addItem(self.scatter1)
        # self.scatter=self.p3.plot()
        # self.scatter =pg.ScatterPlotWidget.scatterPlot()
        # self.scatter.setData()
        # self.
        # self.scatter = self.p3.scatterPlot(x=self.trix,y=self.triy,pen=None)
        # self.scattar=self.p3.plot()
        # self.scatter = self.p2.plot(pen=None)
    def testfunc(self):
        print('we aretestting ethe df ad')
        print(self.curve)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update2)
        self.timer.start(10)





    def triangle_wave(self,start, zhouqi, midu, xdecimals, ydecimals):
        '''

        :param start: the fist value of the wave
        :param end:  the end value of the wave
        :param zhouqi:  the zhouqi range of the wave
        :param midu:  every zhouqi, there are how many points in this zhouqi
        :return: the x array and the y array
        '''

        xout = []
        yout = []
        x = np.around(np.arange(start, start + zhouqi, midu), decimals=xdecimals)
        # y = np.where(x<start+0.5, x-start, 0)
        y = np.around(np.where(x >= start + zhouqi / 2, start + zhouqi - x, x - start), decimals=ydecimals) - 1

        return x, y

    def update(self):
        # global data3, ptr3, ptrtmp
        # data3[ptr3] = np.random.normal()
        self.data3[self.ptr3] = self.triy[self.ptrtmp]
        # self.p3.clear()
        if self.ptr3>1000:
            datatmp1=self.data3[self.ptr3-1000:self.ptr3-1] # 显示最新的10000个数据

        self.ptrtmp += 1
        if self.ptrtmp == 99:
            self.ptrtmp = 0
        self.ptr3 += 1
        if self.ptr3 >= self.data3.shape[0]:
            tmp = self.data3
            self.data3 = np.empty(self.data3.shape[0] * 2)
            self.data3[:tmp.shape[0]] = tmp
        if self.ptr3>1001:
            self.curve.setData(datatmp1)
        else:
            self.curve.setData(self.data3[:self.ptr3])
        # self.p.setRange(xRange=[self.ptr3-50, self.ptr3+50])

        # self.curve.setPos(self.ptr3-1000,0)
        # print('can we in here  after 他和cureset')
        listx = []
        for i in range(self.ptr3):
            listx.append(i+10)
        self.curve2.setData(x=listx,y=self.data3[:self.ptr3])
        # self.curve2sub.setData(self.data3[:self.ptr3]+1)
        # self.scatter.setData(y=self.data3[:self.ptr3],)

    def update2(self):
        global  data_pgpowerx,data_pgpowery
        datatmp1x=data_pgpowerx[len(data_pgpowerx)-10000:len(data_pgpowerx)-1] # 显示最新的10000个数据
        datatmp1y = data_pgpowery[len(data_pgpowerx) - 10000:len(data_pgpowerx) - 1]
        app.processEvents()
        # print('we are in update2')
        self.curve.setData(x=datatmp1x,y=datatmp1y)
        self.curve.setPos(len(data_pgpowerx)-10000,0)
        app.processEvents() #这句话的意思是将界面的控制权短暂的交给ui界面进行显示
        # 另外一种告诉的方案，就是额外的启动两个线程， 干脆就不在当前的线程上进行数据展示，就单独额外的线程进行绘图就好了


        self.curve2.setData(data_pgpowery)
        app.processEvents() #这句话的意思是将界面的控制权短暂的交给ui界面进行显示

        # self.curve2.setData(data_pgpowery)


    def stopupdate(self):
        print('we haive kill the timer')
        self.timer.stop()
        print('we have stopped the timer')

    def startRecving(self):
        # the zmqrecv thread
        print('we are start receiving zmqpackage')

        self.zmqrecv.start()
    def stopRecving(self):
        print('we are start receiving zmqpackage')

        self.zmqrecv.stop()
        # del self.zmqrecv

    def zmqrecvcallback(self):
        print('we have call the recvback once ')
        # self.update2()

        # print(theint)
        # Use this function to update our figure
    def clearData(self):
        global data_pgpowerx,data_pgpowery
        # data_pgpowerx=[0]
        # data_pgpowery=[0]
        print('we have cleared the data')
        # print(data_pgpower)
        # self.curve.setData(data_pgpower)
        # self.curve2.setData(data_pgpowery)
        # self.curve.setData(data_pgpowery)
        # self.p.clear()
        # self.p2.clear()


    def exportdataup(self):
        output = open('datadown.xls', 'w', encoding='gbk')
        output.write('id\tdata\n')
        for i in range(len(data_pgpower)):
            output.write(str(i))
            output.write('\t')
            output.write(str(data_pgpower[i]))
            output.write('\n')
        output.close()

    def exportdatadown(self):
        output = open('datadown.xls','w',encoding='gbk')
        output.write('id\tdata\n')
        for i in range(len(data_pgpower)):

            output.write(str(i))
            output.write('\t')
            output.write(str(data_pgpower[i]))
            output.write('\n')
        output.close()

        pass
    def exportfig(self):
        print('we are in exporr fi g')
        exporter = pg.exporters.ImageExporter(self.p.sceneObj)
        print('aaa')
        exporter.export(fileName='figure1.png')

        exporter1 = pg.exporters.ImageExporter(self.p2.sceneObj)
        exporter1.export('figure2.png')

        exporter2 = pg.exporters.ImageExporter(self.p2.sceneObj)
        exporter2.export('figure3.png')


import process_manager
class ChildDialogWin2(QDialog,process_manager.Ui_Dialog):
    def __init__(self):
        super(ChildDialogWin2,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("Process Monitor GUI")


        print('we are in init')
        self.pushButton_3.clicked.connect(self.start_udp_process_monitor)
        self.pushButton_4.clicked.connect(self.stop_udp_process_monitor)

        self.pushButton_5.clicked.connect(self.start_udp_receive)
        self.pushButton_6.clicked.connect(self.stop_udp_receive)

        self.pushButton_8.clicked.connect(self.run_udp_thread)
        self.pushButton_9.clicked.connect(self.stop_udp_thread)


        self.pushButton_12.clicked.connect(self.start_level_3_11)
        self.pushButton_13.clicked.connect(self.stop_level_3_11)

        self.pushButton_10.clicked.connect(self.start_saving_11)
        self.pushButton_11.clicked.connect(self.stop_saving_11)


        self.pushButton_15.clicked.connect(self.set_exp_id)

        self.pushButton_17.clicked.connect(self.run_pararead_thread)
        self.pushButton_19.clicked.connect(self.stop_pararead_thread)


        self.pushButton_20.clicked.connect(self.start_epics)
        self.pushButton_21.clicked.connect(self.stop_epics)

        self.initilization()


    def initilization(self):
        self.context = zmq.Context()
        self.level_2_req_11 = self.context.socket(zmq.REQ)
        self.level_2_req_11addr = 'tcp://192.168.127.200:8011'
        self.level_2_req_11.bind(self.level_2_req_11addr)
        self.level_2_req_11.setsockopt(zmq.RCVTIMEO,100) #  设定超时时间为5s
        self.level_2_req_11.setsockopt(zmq.SNDTIMEO,100) #  设定超时时间为5s

        self.timerudpprocess = QtCore.QTimer()
        self.timerudpprocess.timeout.connect(self.level_2_3_monitor)

        # self.context = zmq.Context()
        self.level_3_req_11 = self.context.socket(zmq.REQ)
        self.level_3_req_11addr = 'tcp://192.168.127.200:9011'
        self.level_3_req_11.bind(self.level_3_req_11addr)
        self.level_3_req_11.setsockopt(zmq.RCVTIMEO,100)
        self.level_3_req_11.setsockopt(zmq.SNDTIMEO,100)



        # pararead
        self.level_3_req_pararead = self.context.socket(zmq.REQ)
        self.level_3_req_parareadaddr = 'tcp://192.168.127.200:11011'
        self.level_3_req_pararead.bind(self.level_3_req_parareadaddr)
        self.level_3_req_pararead.setsockopt(zmq.RCVTIMEO,100)
        self.level_3_req_pararead.setsockopt(zmq.SNDTIMEO,100)



        self.timersaving11 = QtCore.QTimer()
        self.timersaving11.timeout.connect(self.saving_progressbar_update)
        self.Saving11thread=Savingrecvthread()

        ## Start epics tcp server thread
        self.tcp_epics_thread = tcp_receiving_thread()
        self.tcp_epics_thread.trigger.connect(self.epics_autoprocess)


    def styleinitialization(self):
        # self.pushButton.setStyleSheet("QPushButton{background:red;border-radius:8px;padding:2px 4px;}")

        pass

    def start_udp_process_monitor(self):
        print('we have start udp update process')


        self.timerudpprocess.start(1000)
        print('after start timer')
    def level_2_3_monitor(self):
        print('already in the updating procsee')
        # time.sleep(10)
        ##################################################################################
        try:
            print('try to send process 11 alive')
            self.level_3_req_11.send(b'process alive?')
        except:
            print('send time out')
        try:
            print('after send')
            x=self.level_3_req_11.recv()
            print('can we receive',x)
            if x==b'process yes':
                self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")

                print('Received Msg:',x)
            else:
                self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

        except:
            self.pushButton_2.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

            print('process 11 not online')
        ################################################################################
        try:
            # self.level_2_req_11.send_multipart([b'alive?',])
            self.level_2_req_11.send(b'udp alive?')
        except:
            print('send time out')


        try:
            x=self.level_2_req_11.recv()
            print('x',x)
            if x==b'udp yes':
                self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:green}")

                print('Received Msg:',x)
            else:
                self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

        except:
            self.pushButton_7.setStyleSheet("QPushButton{border-radius:15px;background-color:grey}")

            print('udp not online')



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

    def stop_udp_process_monitor(self):
        print('we have stoppend update udp process ')
        self.timerudpprocess.stop()

    def run_udp_thread(self):
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


    def stop_udp_thread(self):
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


    def start_udp_receive(self):
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
    def stop_udp_receive(self):

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


class MainDialogWin(QDialog,ManagerPanel.Ui_Dialog):
    def __init__(self):
        super(MainDialogWin,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("ManagerPanel GUI")


        print('we are in init')
        self.pushButton_7.clicked.connect(self.displaypanel)
        self.pushButton_8.clicked.connect(self.process_panel)

        self.pushButton_6.clicked.connect(self.testuithread)
        self.pushButton_9.clicked.connect(self.stopuithread)

        self.dispanel = ChildDialogWin()
        self.process_Monitor_panel=ChildDialogWin2()


        self.initilization()



    def initilization(self):
        pass

    def testuithread(self):
        print('In testuithread')
        # self.uithread.start()
        # self.uithread.startsub()

    def stopuithread(self):
        # self.uithread.stop()
        pass




    def displaypanel(self):
        self.dispanel.show()
    def process_panel(self):
        self.process_Monitor_panel.show()






if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # main = MainDialogImgBW()
    # main.show()
    # #app.installEventFilter(main)
    # sys.exit(app.exec_())
    import sys

    ui = MainDialogWin()
    # ui.setupUi(win)
    ui.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

