# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nis_Ui.py'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!



class MainDialogWin(QDialog,ManagerPanel.Ui_Dialog):
    def __init__(self):
        super(MainDialogWin,self).__init__()
        #
        self.setupUi(self)
        self.setWindowTitle("ManagerPanel GUI")


        print('we are in init')
        self.pushButton_7.clicked.connect(self.displaypanel)

        self.dispanel = ChildDialogWin()


    def displaypanel(self):
        self.dispanel.show()




        # self.zmqrecv.__init__()
        # self.zmqrecv.trigger.connect(self.zmqrecvcallback)