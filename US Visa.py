from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
from playsound import playsound
driver = webdriver.Chrome(executable_path='c.exe')
driver.get('https://cgifederal.secure.force.com/')
time.sleep(40)
d={}
d["January"]=1
d["February"]=2
d["March"]=3
d["April"]=4
d["May"]=5
d["June"]=6
d["July"]=7
d["August"]=8
d["September"]=9
d["October"]=10
d["November"]=11
d["December"]=12




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 70, 181, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 70, 171, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 320, 181, 91))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "US VISA EARLY DATE CHECKER"))
        self.label_11.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "RUN SCRIPT"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))

    def stop(self):
        print("stopped")

    def run(self):
        try:
            box = driver.find_element_by_xpath('//div[@class="leftPanelText"]')
            txt = box.get_attribute('innerHTML').strip()
            arr = txt.split(" ")
            date = arr[6].replace(",", "")
            for x in range(100):
                driver.refresh()
                time.sleep(5)
                box = driver.find_element_by_xpath('//div[@class="leftPanelText"]')
                time.sleep(5)
                txt1 = box.get_attribute('innerHTML').strip()
                arr1 = txt1.split(" ")
                date1 = arr1[6].replace(",", "")
                driver.delete_cookie('__utma')
                driver.delete_cookie('__utmb')
                driver.delete_cookie('__utmc')
                if (d[arr[5]] > d[arr1[5]] or date > date1):
                        print("changed")
                        playsound('sound.mp3')
        except:
            print("error, did you login correctly? are you on the homepage where the earliest date is showed at the left")
            playsound('sound.mp3')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())










