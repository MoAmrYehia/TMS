# -*- coding: utf-8 -*-
"""
login mechanism 
made by ehab ebrahim 
"""

# signals use connect


#from tinydb import TinyDB
from auth import *
from PyQt5 import QtWidgets
#from PyQt5 import QPixmap
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys
from PyQt5.uic import loadUi
import socket


class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi("mainwindow.ui",self)
        self.loginbutton.clicked.connect(self.loginfunc)
        self.email.setPlaceholderText("Email")
        self.pasS.setPlaceholderText("password")
        self.pasS.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.gotosignup)
        self.admin.clicked.connect(self.gotoadmin)
        self.forGet.clicked.connect(self.gotoforget)
        self.stay_in.toggled.connect(self.gotostayin)
        
    def loginfunc(self):
        email=self.email.text()
        password=self.pasS.text()
        print(email,password)
        use=user_auth(email,password)
        print(use.login())
        
        
    def gotosignup(self):
        signUp=signup()
        widget.addWidget(signUp)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def gotoadmin(self):
        Admin=admin()
        widget.addWidget(Admin)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoforget(self):
        Forget=forgetpass()
        widget.addWidget(Forget)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotostayin(self):
        print("stay")
        
            
class admin(QMainWindow):
    def __init__(self):
        super(admin,self).__init__()
        loadUi("admin.ui",self)
        self.login.clicked.connect(self.loginfunc)
        self.email.setPlaceholderText("Email Address")
        self.password.setPlaceholderText("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def loginfunc(self):
        email=self.email.text()
        password=self.password.text()
        print(email,password)
        
        
        
        
class forgetpass(QMainWindow):
    def __init__(self):
        super(forgetpass,self).__init__()
        loadUi("forget.ui",self)
        self.email.setPlaceholderText("Email Address")
        self.sendmail.clicked.connect(self.sendEmail)
        
    def sendEmail(self):
        #check validation email syntax
        
        Email=self.email.text()
        print("send email to",Email)
        lo =writecode()
        widget.addWidget(lo)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
    
    
class writecode(QMainWindow):
    def __init__(self):
        super(writecode,self).__init__()
        loadUi("write_code.ui",self)
        self.code.setPlaceholderText("Enter code")
        self.code.setEchoMode(QtWidgets.QLineEdit.Password)
        self.send.clicked.connect(self.gotosend)
        
    def gotosend(self):
        #make checking code
        
        #if ok goto change pass
        make=makepass()
        widget.addWidget(make)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #else 
        #forget=forgetpass()
       # widget.addWidget(forget)
       # widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
class makepass(QMainWindow):
    def __init__(self):
        super(makepass,self).__init__()
        loadUi("changepass.ui",self)
        self.passw.setPlaceholderText("password")
        self.confpass.setPlaceholderText("confirm password")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reset.clicked.connect(self.gotoreset)
    
    def gotoreset(self):
        if self.passw.text()==self.confpass.text():
            password=self.passw.text()
            print("password changed",password)
            logiin=login()
            widget.addWidget(logiin)
            widget.setCurrentIndex(widget.currentIndex()+1)
    
    
    
    
    
class signup(QMainWindow):
    def __init__(self):
        super(signup,self).__init__()
        loadUi("sign_up.ui",self)
        self.submit.clicked.connect(self.creatfunc)
        self.firstname.setPlaceholderText("first name")
        self.lastname.setPlaceholderText("last name")
        self.email.setPlaceholderText("Email")
        self.username.setPlaceholderText("username")
        self.phone.setPlaceholderText("phone number")
        self.role.setPlaceholderText("role")
        self.password.setPlaceholderText("password")
        self.conf.setPlaceholderText("confirm password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conf.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
    def creatfunc(self):
        first_Name=self.firstname.text()
        second_Name=self.lastname.text()
        email=self.email.text()
        username=self.username.text()
        phone=self.phone.text()
        role=self.role.text()
        password=self.password.text()
        conf=self.conf.text()
        if password==conf:
            print("matched")
            User=user(first_Name,second_Name,email,phone,username,role,password)
            if User.adduser():
                logiin=login()
                widget.addWidget(logiin)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print("in label error check your data")
                
        else:
            print("Not matched")
        
        
        
            
        


app=QApplication(sys.argv)
mainwindow=login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(600)
widget.setFixedHeight(620)
widget.show()
app.exec_()

        


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         #win=QMainWindow()
#         self.setGeometry(1000,1000,800,600)
#         self.setWindowTitle("first")
#         self.initUi()
        
#     def initUi(self):
        
#         self.b=QtWidgets.QPushButton(self)
#         self.b.setText("Admin")
#         self.b.move(20,20)
         
#         self.b1=QtWidgets.QPushButton(self)
#         self.b1.setText("User")
#         self.b1.move(120,20)
         
        
#         self.label=QtWidgets.QLabel(self)
#         self.label.setText("email")
#         self.label.move(50,50)
#         self.line=QtWidgets.QLineEdit(self)
#         self.line.move(100,50)
       
#         self.label1=QtWidgets.QLabel(self)
#         self.label1.setText("password")
#         self.label1.move(50,100)
#         self.line1=QtWidgets.QLineEdit(self)
#         self.line1.move(100,100)
        
#     def 
        
#         # self.b1=QtWidgets.QPushButton(self)
#         # self.b1.setText("Click me")
#         # self.b1.clicked.connect(self.clicked)
        
#     def clicked_admin(self):
#         self.label.setText("preesed")
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #TCP connection

# def window():
#     app=QApplication(sys.argv)
#     win=MyWindow()
#    # xpos=0,ypos=0,width=5,hight=5
#     #win.setGeometry(1020,1020,300,300)
#     #win.setWindowTitle("first")
#     # label=QtWidgets.QLabel(win)
#     # label.setText("ehab dfddf")
#     # label.move(50,50)
#     win.show()
#     sys.exit(app.exec_())
    
# window()
