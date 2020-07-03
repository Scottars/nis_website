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
global data_pgpowerx,data_pgpowey,data_receive_flag_02,data_receive_flag_11
data_receive_flag_02 = False
data_receive_flag_11 = False
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



# 水冷数据接收
class zmqrecvthread_02(QtCore.QThread):
    trigger=QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.context=zmq.Context()
        self.zmqsub=self.context.socket(zmq.SUB)
        self.zmqsub.setsockopt(zmq.SUBSCRIBE,b'')
        # self.subaddr='tcp://192.168.127.200:10011'
        self.subaddr='tcp://192.168.127.201:5002'
        # self.subaddr='inproc://iiii'
        print('in the thread init')
        self.zmqsub.connect(self.subaddr)
        self.flag=0
        # # Initialize poll set
        # self.poller = zmq.Poller()
        # self.poller.register(self.zmqsub,zmq.POLLIN)

    def run(self):
        global  data_pgpower,data_receive_flag_02
        global pic2
        print('we are running ')
        print(self.subaddr)
        self.flag=1
        i=1
        counter=0
        while True:
            if self.flag:
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
                except zmq.Again:
                    print('TO recv again')
                    pass
    def stop(self):
        self.flag=0
        print('we have stop the thread in stop')


# 引出电源数据接收
class zmqrecvthread_11(QtCore.QThread):
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
        global  data_pgpower,data_receive_flag_11
        global pic2
        print('we are running ')
        print(self.subaddr)
        self.flag=1
        i=1
        counter=0
        while True:
            if data_receive_flag_11:
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
                            data_pgpowerx.append(x)
                            data_pgpowery.append(y)
                        except:
                            print('time sample error')
                except zmq.Again:
                    print('TO recv again')
                    pass


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

        self.zmqrecv_11 = zmqrecvthread_11()
        self.zmqrecv_11.start()

        self.zmqrecv_02 = zmqrecvthread_02()
        self.zmqrecv_02.start()


        self.tabWidget.currentChanged.connect(self.tabchange)
        # self.tab_2.changeEvent(self.tabchange2)

    def tabchange(self):
        #ps这个current index  是从左到右依次增加的，默认从0开始
        # 对于这个地方，我们可以实现数据接收的停止，以及对应的ui的定时刷新的停止。


        print('index:',self.tabWidget.currentIndex())
        # if self.tabWidget.currentIndex()==0
        currenttab= self.tabWidget.currentIndex()
        if currenttab==0:
            self.pushButton_8.setDisabled(True)

        elif currenttab == 1:
            self.pushButton_8.setEnabled(True)
        elif currenttab == 2:
            # 切换到那个页面，就只对那个页面实现数据的接收，实时刷新的显示。
            # 对于其他页面的数据接收和实时显示部分

            pass
        elif currenttab == 3:

            pass
        elif currenttab == 4:
            pass
        elif currenttab == 6:
            pass
        elif currenttab == 7:
            pass
        elif currenttab == 8:
            pass
        print('tabchahge111111111111')
    def tabchange2(self):
        print('tabchange22222222222')
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
    def rt_display_intial(self):
        self.timer_02 = QtCore.QTimer()
        self.timer_02.timeout.connect(self.update_02)
        self.timer_02.start(10)

        self.timer_11 = QtCore.QTimer()
        self.timer_11.timeout.connect(self.update_11)
        self.timer_11.start(10)



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

    def update_02(self):
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
    def update_11(self):
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


    def stopupdate_02(self):
        print('we haive kill the timer')
        self.timer_02.stop()
        print('we have stopped the timer')
    def stopupdate_11(self):
        self.timer_11.stop()

    def startRecving_02(self):
        global data_receive_flag_02
        data_receive_flag_02 = True
    def stopRecving_02(self):
        global data_receive_flag_02
        data_receive_flag_02 = False

    def startRecving_11(self):
        global data_receive_flag_11
        data_receive_flag_11 = True
    def stopRecving_11(self):
        global data_receive_flag_11
        data_receive_flag_11 = False

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








if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # main = MainDialogImgBW()
    # main.show()
    # #app.installEventFilter(main)
    # sys.exit(app.exec_())
    import sys

    ui = ChildDialogWin()
    # ui.setupUi(win)
    ui.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

