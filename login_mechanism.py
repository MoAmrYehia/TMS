from auth import *
from PyQt5 import QtWidgets
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
        status,error=user_auth(self.email.text(),self.pasS.text()).login()
        print(error)
        """ if status == True then go to the main windwo of the app"""
                    
       
        
        
    def gotosignup(self):
        widget.addWidget(signup())
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def gotoadmin(self):
        widget.addWidget(admin())
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoforget(self):
        widget.addWidget(forgetpass())
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
        status,error=user_auth(self.email.text(),self.password.text()).login()
        print(error)
        
        """if status == True then go to the admin windwo"""
        
        
        
        
class forgetpass(QMainWindow):
    def __init__(self):
        super(forgetpass,self).__init__()
        loadUi("forget.ui",self)
        self.email.setPlaceholderText("Email Address")
        self.sendmail.clicked.connect(self.sendEmail)
        
    def sendEmail(self):
          
        user_auth(self.email.text(),"").reset()
        # want a function take the email only and send the code
        print("send email to",self.email.text())
        lo =writecode(self.email.text())
        widget.addWidget(lo)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
    
    
class writecode(QMainWindow):
    def __init__(self,email):
        super(writecode,self).__init__()
        loadUi("write_code.ui",self)
        self.email=email
        self.code.setPlaceholderText("Enter code")
        self.code.setEchoMode(QtWidgets.QLineEdit.Password)
        self.send.clicked.connect(self.gotosend)
        
    def gotosend(self):
        #make checking code
        status=user_auth(str(self.email),"").code_validaion(self.code.text())
        
        #if ok goto change pass
        if status==True:
            widget.addWidget(makepass(self.email))
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            widget.addWidget(forgetpass())
            widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
class makepass(QMainWindow):
    def __init__(self,email):
        super(makepass,self).__init__()
        loadUi("changepass.ui",self)
        self.email=email
        self.passw.setPlaceholderText("password")
        self.confpass.setPlaceholderText("confirm password")
        self.passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reset.clicked.connect(self.gotoreset)
    
    def gotoreset(self):
        if self.passw.text()==self.confpass.text():
            status=user_auth(str(self.email),"").reset_handler(self.passw.text())
            if status==True:
                widget.addWidget(login())
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print("enter another pass")
            
        else:
            print("notmatched")
    
    
    
    
    
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
        self.password.setPlaceholderText("password")
        self.conf.setPlaceholderText("confirm password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conf.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
    def creatfunc(self):
        if self.password.text()==self.conf.text():
            print("matched")
            User=user(self.firstname.text(),self.lastname.text(),self.email.text(),self.phone.text(),self.username.text(),self.role.currentText(),self.password.text())
            status,error=User.adduser()
            if status==True:
                widget.addWidget(login())
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print(error)
                
        else:
            print("Not matched")
        
        
        
            
        


app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget.addWidget(login())
widget.show()
app.exec_()

        
