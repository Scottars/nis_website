#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os,signal,sys
import  pymysql
import  multiprocessing
# from dataservice.zmq.UPcomputer_part.TCP_receive_0mq_PUB.guifile import Ui_Dialog  # 同级目录下引用报错,但是可以运行
from guifile import Ui_Dialog
# import matplotlib,time
# matplotlib.use("Qt5Agg")  # 声明使用QT5
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plteee
import socket
import  os
global flagthreadstop
flagthreadstop=False
global msg
msg=b'\x00\x03'
class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()
    def run(self):
        #这一部分就可以写入你想要执行的代码就好
        # print('开始执行了run')
        # self.ip_port = ('192.168.0.3', 32768)
        #
        self.ip_port = ('127.0.0.1', 44233)
        BUFSIZE = 1024
        self.udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.udp_server_client.bind(self.ip_port)
        print('we have bind this ip')

        while True:
            if flagthreadstop:
                self.udp_server_client.close()
                break


            else:
                global msg
                print('BEFORE')
                msg, addr =self.udp_server_client.recvfrom(BUFSIZE)
                print("recv", msg, addr)
                # self.trigger.emit()



            # self.udp_server_client.sendto(msg.upper(), addr)#我们得到了这个socket 然后通过socket发送到原来接收得到的地址

            # 循环完毕后发出信号


class MainDialogImgBW(QDialog,Ui_Dialog):
    def __init__(self):
        super(MainDialogImgBW,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("HSDD Manager GUI")
        self.setMinimumSize(0,0)




        self.D_02_Run.clicked.connect(self.D_02_Run_func)
        self.T_02_Run.clicked.connect(self.T_02_Run_func)
        self.D_02_Run.clicked.connect(self.P_02_Run_func)
        # self.D_02_Stop.clicked.connect(self.receivestop)
        self.databasecheck.clicked.connect(self.databasechehckresult)

    def databasechehckresult(self):
        print('database -----')
        db = pymysql.connect(host='localhost', user='scottar', password='123456', db='nis_hsdd', port=3306, charset='utf8')
        cur = db.cursor()
        msgResult=''


        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =2"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='02:  '+ str(numinbase) + '\n'

        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =3"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='03:  '+ str(numinbase) + '\n'


        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =4"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='04:  '+ str(numinbase) + '\n'


        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =5"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='05:  '+ str(numinbase) + '\n'


        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =6"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='06:  '+ str(numinbase) + '\n'

        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =7"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='07:  '+ str(numinbase) + '\n'

        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =8"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='08:  '+ str(numinbase) + '\n'

        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =16"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='16:  '+ str(numinbase) + '\n'


        sql = "SELECT * FROM v_data_monitor WHERE  subsys_id =17"
        cur.execute(sql)
        numinbase=0
        for col in (cur):
            numinbase+=1
        msgResult +='17:  '+ str(numinbase) + '\n'

        # self.textBrower
        self.textBrowser.setText(msgResult)


        print(msgResult)


    def D_02_Run_func(self):
        print('we have run  D02')
        os.system("python3 D_02_watercooldown_num10.py")
    def kill(self,pid):
        print('pid',pid)
        # pgid=os.getpgid(pid)
        # print(pgid)
        # a = os.killpg(pgid,signal.SIGKILL)
        a = os.kill(pid,signal.SIGKILL)
        print('已杀死pid为%s的进程,　返回值是:%s' % (pid, a))


    def kill_target(self,target):
        cmd_run="ps aux | grep {}".format(target)
        out=os.popen(cmd_run).read()
        for line in out.splitlines():
            print(line)
            if '另外判断杀死进行所在的路径' in line:
                pid = int(line.split()[1])
                self.kill(pid)


    def T_02_Run_func(self):
        print('we have run  T02')
        os.system("python3 TCP_02_watercooldown_num10.py")


    def P_02_Run_func(self):
        print('we have run  P02')

        os.system("python3 process_02_watercooldown_num10.py")


    def D_02_Stop_func(self):
        # os.system("python3 D_02_watercooldown_num10.py")
        self.kill_target("D_02_watercooldown_num10.py")
        print('we have stopped  D02')

    def T_02_Stop_func(self):
        # os.system("python3 TCP_02_watercooldown_num10.py")
        self.kill_target("TCP_02_watercooldown_num10.py")
        print('we have stopped  T02')


    def P_02_Stop_func(self):
        # os.system("python3 process_02_watercooldown_num10.py")
        self.kill_target("process_02_watercooldown_num10.py")
        print('we have stopped  P02')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainDialogImgBW()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())
