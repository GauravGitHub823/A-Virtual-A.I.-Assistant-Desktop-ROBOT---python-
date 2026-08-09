
from IronMan import Ui_IronManUI

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUiType
import sys

import MainJarvisMachine


MainJarvisMachine.start()

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        MainJarvisMachine.Task_Gui()


startExe = MainThread()


class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_IronManUI()
        self.gui.setupUi(self)

        self.gui.Start.clicked.connect(self.startTask)
        self.gui.Stop.clicked.connect(self.close)
        self.gui.Search.clicked.connect(self.chrome_app)


    def chrome_app(self):
        from Searching import seach
        seach()


    def startTask(self):

        self.gui.label1 = QtGui.QMovie("GUI-Gif//FullBodyScan.gif")
        self.gui.Gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("GUI-Gif//Scan.gif")
        self.gui.Gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("GUI-Gif//World.gif")
        self.gui.Gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("GUI-Gif//Face.gif")
        self.gui.Gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("GUI-Gif//Search.gif")
        self.gui.Gif_5.setMovie(self.gui.label5)
        self.gui.label5.start()

        self.gui.label6 = QtGui.QMovie("GUI-Gif//Health.gif")
        self.gui.Gif_6.setMovie(self.gui.label6)
        self.gui.label6.start()

        self.gui.label7 = QtGui.QMovie("GUI-Gif//Code.gif")
        self.gui.Gif_7.setMovie(self.gui.label7)
        self.gui.label7.start()

        self.gui.label8 = QtGui.QMovie("GUI-Gif//Jarvis.gif")
        self.gui.Gif_8.setMovie(self.gui.label8)
        self.gui.label8.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)

        startExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        label_time = "Time : " + time
        self.gui.Text_Time.setText(label_time)

        d_ate = QDate.currentDate()
        date = d_ate.toString(Qt.ISODate)
        label_date = "Date : " + date
        self.gui.Text_Date.setText(label_date)

        import datetime
        days = datetime.datetime.now().strftime("%A")
        label_day = "  Day : " + days
        self.gui.Text_Day.setText(label_day)

        self.gui.Text_Temp.setText("  Location : Varanasi")




GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())

