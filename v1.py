from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
QHBoxLayout

class Control(QWidget):
    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.edit = QPushButton("")
        self.remove = QPushButton("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Style.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit.setIcon(icon2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon3)
        self.chk = QtWidgets.QCheckBox("")
        self.chk.setChecked(False)

        layout = QHBoxLayout()
        layout.addStretch(1)
        layout.addWidget(self.chk)
        layout.addWidget(self.remove)
        layout.addWidget(self.edit)

        self.setLayout(layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 567)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 10, 31, 25))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("searchIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 371, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 10, 71, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("addIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 10, 61, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(710, 10, 71, 25))
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(150, 40, 631, 501))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2.clicked.connect(self.addTask)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addTask(self):
        con = Control()
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QtCore.QSize(0,40))
        item.setText("Task   " + str(self.listWidget.count()))
        item.setIcon(QtGui.QIcon("Task.jpeg"))
        #item.setCheckState(0)
        con.edit.setObjectName("edit" + str(self.listWidget.count()))
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item,con)
        con.edit.clicked.connect(self.removeTask)


    def removeTask(self):
        self.listWidget.takeItem(self.listWidget.currentRow())



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", " Sort"))
        self.pushButton_9.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
