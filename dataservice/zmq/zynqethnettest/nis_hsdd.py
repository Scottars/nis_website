# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nis_hsdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1291, 717)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(950, 810, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 1291, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_17.setGeometry(QtCore.QRect(520, 10, 81, 21))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(840, 10, 91, 21))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 10, 81, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_15.setGeometry(QtCore.QRect(720, 10, 91, 21))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 10, 81, 21))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_13.setGeometry(QtCore.QRect(280, 10, 91, 21))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 1251, 531))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsView_7 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout_3.addWidget(self.graphicsView_7, 1, 0, 1, 1)
        self.graphicsView_8 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout_3.addWidget(self.graphicsView_8, 2, 0, 1, 1)
        self.graphicsView_9 = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout_3.addWidget(self.graphicsView_9, 0, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(140, 10, 111, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 10, 81, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 10, 81, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 10, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 10, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 10, 91, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 10, 81, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(740, 10, 91, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 1251, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_2 = PlotWidget(self.gridLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 1, 0, 1, 1)
        self.graphicsView_3 = PlotWidget(self.gridLayoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 2, 0, 1, 1)
        self.graphicsView = PlotWidget(self.gridLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(860, 10, 91, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_18.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_20.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.graphicsView_10 = PlotWidget(self.gridLayoutWidget_3)
        self.graphicsView_10.setObjectName("graphicsView_10")
        self.gridLayout_4.addWidget(self.graphicsView_10, 1, 0, 1, 1)
        self.graphicsView_11 = PlotWidget(self.gridLayoutWidget_3)
        self.graphicsView_11.setObjectName("graphicsView_11")
        self.gridLayout_4.addWidget(self.graphicsView_11, 2, 0, 1, 1)
        self.graphicsView_12 = PlotWidget(self.gridLayoutWidget_3)
        self.graphicsView_12.setObjectName("graphicsView_12")
        self.gridLayout_4.addWidget(self.graphicsView_12, 0, 0, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_21.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_22.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_23.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_24.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_25.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_25.setObjectName("pushButton_25")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_26.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_27.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_28.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.graphicsView_13 = PlotWidget(self.gridLayoutWidget_4)
        self.graphicsView_13.setObjectName("graphicsView_13")
        self.gridLayout_5.addWidget(self.graphicsView_13, 1, 0, 1, 1)
        self.graphicsView_14 = PlotWidget(self.gridLayoutWidget_4)
        self.graphicsView_14.setObjectName("graphicsView_14")
        self.gridLayout_5.addWidget(self.graphicsView_14, 2, 0, 1, 1)
        self.graphicsView_15 = PlotWidget(self.gridLayoutWidget_4)
        self.graphicsView_15.setObjectName("graphicsView_15")
        self.gridLayout_5.addWidget(self.graphicsView_15, 0, 0, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_29.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_30.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_31.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_32.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_33.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_33.setObjectName("pushButton_33")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_34.setGeometry(QtCore.QRect(410, 10, 81, 21))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_35.setGeometry(QtCore.QRect(140, 10, 111, 23))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_36.setGeometry(QtCore.QRect(620, 10, 81, 21))
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 40, 1251, 531))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.graphicsView_16 = PlotWidget(self.gridLayoutWidget_5)
        self.graphicsView_16.setObjectName("graphicsView_16")
        self.gridLayout_6.addWidget(self.graphicsView_16, 1, 0, 1, 1)
        self.graphicsView_17 = PlotWidget(self.gridLayoutWidget_5)
        self.graphicsView_17.setObjectName("graphicsView_17")
        self.gridLayout_6.addWidget(self.graphicsView_17, 2, 0, 1, 1)
        self.graphicsView_18 = PlotWidget(self.gridLayoutWidget_5)
        self.graphicsView_18.setObjectName("graphicsView_18")
        self.gridLayout_6.addWidget(self.graphicsView_18, 0, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_37.setGeometry(QtCore.QRect(280, 10, 91, 21))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_38.setGeometry(QtCore.QRect(840, 10, 91, 21))
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_39.setGeometry(QtCore.QRect(720, 10, 91, 21))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 10, 101, 23))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_41.setGeometry(QtCore.QRect(520, 10, 81, 21))
        self.pushButton_41.setObjectName("pushButton_41")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_42 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_42.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_43.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_44.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphicsView_19 = PlotWidget(self.gridLayoutWidget_6)
        self.graphicsView_19.setObjectName("graphicsView_19")
        self.gridLayout_7.addWidget(self.graphicsView_19, 1, 0, 1, 1)
        self.graphicsView_20 = PlotWidget(self.gridLayoutWidget_6)
        self.graphicsView_20.setObjectName("graphicsView_20")
        self.gridLayout_7.addWidget(self.graphicsView_20, 2, 0, 1, 1)
        self.graphicsView_21 = PlotWidget(self.gridLayoutWidget_6)
        self.graphicsView_21.setObjectName("graphicsView_21")
        self.gridLayout_7.addWidget(self.graphicsView_21, 0, 0, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_45.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_46.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_47.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_48.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_49.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_49.setObjectName("pushButton_49")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.pushButton_50 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_50.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_51.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_52.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab_7)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphicsView_25 = PlotWidget(self.gridLayoutWidget_7)
        self.graphicsView_25.setObjectName("graphicsView_25")
        self.gridLayout_9.addWidget(self.graphicsView_25, 1, 0, 1, 1)
        self.graphicsView_26 = PlotWidget(self.gridLayoutWidget_7)
        self.graphicsView_26.setObjectName("graphicsView_26")
        self.gridLayout_9.addWidget(self.graphicsView_26, 2, 0, 1, 1)
        self.graphicsView_27 = PlotWidget(self.gridLayoutWidget_7)
        self.graphicsView_27.setObjectName("graphicsView_27")
        self.gridLayout_9.addWidget(self.graphicsView_27, 0, 0, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_53.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_54.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_55.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_56.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_57.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_57.setObjectName("pushButton_57")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.pushButton_65 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_65.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_61 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_61.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_60 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_60.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_58 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_58.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_8)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.graphicsView_31 = PlotWidget(self.gridLayoutWidget_8)
        self.graphicsView_31.setObjectName("graphicsView_31")
        self.gridLayout_11.addWidget(self.graphicsView_31, 1, 0, 1, 1)
        self.graphicsView_32 = PlotWidget(self.gridLayoutWidget_8)
        self.graphicsView_32.setObjectName("graphicsView_32")
        self.gridLayout_11.addWidget(self.graphicsView_32, 2, 0, 1, 1)
        self.graphicsView_33 = PlotWidget(self.gridLayoutWidget_8)
        self.graphicsView_33.setObjectName("graphicsView_33")
        self.gridLayout_11.addWidget(self.graphicsView_33, 0, 0, 1, 1)
        self.pushButton_62 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_62.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_59 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_59.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_63 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_63.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_64.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_64.setObjectName("pushButton_64")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.pushButton_66 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_66.setGeometry(QtCore.QRect(420, 10, 81, 21))
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_67.setGeometry(QtCore.QRect(150, 10, 111, 23))
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_68.setGeometry(QtCore.QRect(630, 10, 81, 21))
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.tab_9)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(10, 40, 1251, 531))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.graphicsView_34 = PlotWidget(self.gridLayoutWidget_9)
        self.graphicsView_34.setObjectName("graphicsView_34")
        self.gridLayout_12.addWidget(self.graphicsView_34, 1, 0, 1, 1)
        self.graphicsView_35 = PlotWidget(self.gridLayoutWidget_9)
        self.graphicsView_35.setObjectName("graphicsView_35")
        self.gridLayout_12.addWidget(self.graphicsView_35, 2, 0, 1, 1)
        self.graphicsView_36 = PlotWidget(self.gridLayoutWidget_9)
        self.graphicsView_36.setObjectName("graphicsView_36")
        self.gridLayout_12.addWidget(self.graphicsView_36, 0, 0, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_69.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_70.setGeometry(QtCore.QRect(850, 10, 91, 21))
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_71.setGeometry(QtCore.QRect(730, 10, 91, 21))
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_72.setGeometry(QtCore.QRect(20, 10, 101, 23))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_73.setGeometry(QtCore.QRect(530, 10, 81, 21))
        self.pushButton_73.setObjectName("pushButton_73")
        self.tabWidget.addTab(self.tab_9, "")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(100, 40, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 40, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(8)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_17.setText(_translate("Dialog", "ClearUpdate"))
        self.pushButton_14.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_10.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_15.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_16.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_12.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_13.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_11.setText(_translate("Dialog", "StopUpdating"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "WaterCool"))
        self.pushButton_5.setText(_translate("Dialog", "ClearUpdate"))
        self.pushButton_4.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_2.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_3.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_6.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_7.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_9.setText(_translate("Dialog", "Export Figure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "PGPower"))
        self.pushButton_18.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_19.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_20.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_21.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_22.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_23.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_24.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_25.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Ce_furnace"))
        self.pushButton_26.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_27.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_28.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_29.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_30.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_31.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_32.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_33.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Gas_Supply"))
        self.pushButton_34.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_35.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_36.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_37.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_38.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_39.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_40.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_41.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Filament_Power"))
        self.pushButton_42.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_43.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_44.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_45.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_46.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_47.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_48.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_49.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "RF_Power"))
        self.pushButton_50.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_51.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_52.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_53.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_54.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_55.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_56.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_57.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Pg_Magnicant_poower"))
        self.pushButton_65.setText(_translate("Dialog", "ClearUpdate"))
        self.pushButton_61.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_60.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_58.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_62.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_59.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_63.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_64.setText(_translate("Dialog", "StartUpdating"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Dialog", "EG_GG_Power"))
        self.pushButton_66.setText(_translate("Dialog", "StopRcving"))
        self.pushButton_67.setText(_translate("Dialog", "StopUpdating"))
        self.pushButton_68.setText(_translate("Dialog", "ExportDataUp"))
        self.pushButton_69.setText(_translate("Dialog", "StartRcving"))
        self.pushButton_70.setText(_translate("Dialog", "Export Figure"))
        self.pushButton_71.setText(_translate("Dialog", "ExportDataDown"))
        self.pushButton_72.setText(_translate("Dialog", "StartUpdating"))
        self.pushButton_73.setText(_translate("Dialog", "ClearUpdate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Dialog", "Heat_Meter"))
        self.pushButton_8.setText(_translate("Dialog", "Mode："))
        self.radioButton.setText(_translate("Dialog", "Auto Mode"))
        self.radioButton_2.setText(_translate("Dialog", "Menu Mode"))
from pyqtgraph import PlotWidget
