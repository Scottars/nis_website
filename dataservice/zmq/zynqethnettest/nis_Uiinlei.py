#-*-coding:utf-8-*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os,signal,sys
from pyqtgraph.Qt import QtGui,QtCore, USE_PYSIDE, USE_PYQT5,QtWidgets
import  pymysql
import  multiprocessing
import  numpy as np
from nis_hsdd import  Ui_Dialog
import struct
import  pyqtgraph as pg
import nis_hsdd
from pyqtgraph.ptime import time
# 声明一个应用程序
app = QtGui.QApplication([])
import time
import  zmq

global data_pgpower
data_pgpower=[]



class zmqrecvthread(QtCore.QThread):
    trigger=QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.context=zmq.Context()
        self.zmqsub=self.context.socket(zmq.SUB)
        self.zmqsub.setsockopt(zmq.SUBSCRIBE,b'')
        self.subaddr='tcp://192.168.127.200:8011'
        # self.subaddr='inproc://iiii'
        print('in the thread init')
        self.zmqsub.bind(self.subaddr)
        self.flag=0
        # # Initialize poll set
        # self.poller = zmq.Poller()
        # self.poller.register(self.zmqsub,zmq.POLLIN)

    def run(self):
        global  data_pgpower
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
                print(counter)
                for i in range(100):
                    tmpb=b[i*4:(i+1)*4]
                    x = struct.unpack('!f', tmpb)[0]
                    # print('x',x)
                    data_pgpower.append(x)
                # print(data_pgpower)
            except zmq.Again:
                print('TO recv again')
                pass



    def stop(self):
        self.flag=0
        print('we have stop the thread in stop')




class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("HSDD Manager GUI")
        self.setMinimumSize(0,0)
        self.p= self.graphicsView
        self.p2=self.graphicsView_2

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

        self.zmqrecv = zmqrecvthread()
        # self.zmqrecv.__init__()
        # self.zmqrecv.trigger.connect(self.zmqrecvcallback)


    def initlizefig(self):
        self.p.setDownsampling(mode='subsample')
        self.p2.setDownsampling(mode='subsample')
        self.p.setClipToView(True)
        self.p2.setClipToView(True)
        # self.p.setRange(xRange=[-100, 0])
        # self.p.setLimits(xMax=0)
        self.curve = self.p.plot()
        self.curve2 = self.p2.plot()
    def testfunc(self):
        print('we aretestting ethe df ad')
        print(self.curve)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update2)
        self.timer.start(1)

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
        print('we are in here')
        self.data3[self.ptr3] = self.triy[self.ptrtmp]
        print(type(self.data3))
        self.ptrtmp += 1
        if self.ptrtmp == 99:
            self.ptrtmp = 0
        self.ptr3 += 1
        if self.ptr3 >= self.data3.shape[0]:
            tmp = self.data3
            self.data3 = np.empty(self.data3.shape[0] * 2)
            self.data3[:tmp.shape[0]] = tmp

        self.curve.setData(self.data3[:self.ptr3])
        # self.p.setRange(xRange=[self.ptr3-50, self.ptr3+50])

        self.curve.setPos(self.ptr3,0)

        # self.curve2.setData(self.data3[:self.ptr3])
        print('before')
        print('size data3',)
    def update2(self):
        global  data_pgpower
        datatmp1=data_pgpower[len(data_pgpower)-10000:len(data_pgpower)-1] # 显示最新的10000个数据
        # print('we are in update2')
        self.curve.setData(datatmp1)
        self.curve.setPos(len(data_pgpower)-10000,0)
        self.curve2.setData(data_pgpower)

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
        global data_pgpower
        data_pgpower=[0]
        print('we have cleared the data')
        print(data_pgpower)
        # self.curve.setData(data_pgpower)
        self.curve2.setData(data_pgpower)

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

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # main = MainDialogImgBW()
    # main.show()
    # #app.installEventFilter(main)
    # sys.exit(app.exec_())
    import sys

    ui = MainDialogImgBW()
    # ui.setupUi(win)
    ui.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

