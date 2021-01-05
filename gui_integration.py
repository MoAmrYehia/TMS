# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# signals use connect


#from tinydb import TinyDB

from task import *
from task_operations import*
from auth import *
import speech_recognition as sr
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QListWidget,QListWidgetItem,QDialog,QWidget,QHBoxLayout,QFileDialog, QAction,QTableView,QHeaderView,QVBoxLayout,QMenu
import sys
from PyQt5.QtCore import Qt, QSortFilterProxyModel,QDateTime,QMimeData
from PyQt5.QtGui import QStandardItemModel, QStandardItem,QPixmap,QDrag
from PyQt5.QtGui import *

from PyQt5.uic import loadUi
import socket



#from PyQt5 import QPixmap



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
        
        """ if status == True then go to the main windwo of the app"""
        if status ==True:
            
            widget.addWidget(mainWindowTask(self.email.text()))
            widget.setCurrentIndex(widget.currentIndex()+1)
            print(error)
       
        else:
            print(error)
        
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
        #self.role.setPlaceholderText("role")
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
        
        





class mainWindowTask(QMainWindow):
    def __init__(self,username):
        super(mainWindowTask, self).__init__()
        loadUi("mainwindow_task.ui",self)
       
        self.username=username
        print(Manage(self.username).show_tasks())
        self.center()
        self.menuBar=self.menuBar()
        file_menu=self.menuBar.addMenu("File")
        edit_menu=self.menuBar.addMenu("Edit")
        exit_action =QAction('Exit App',self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(lambda :QApplication.quit())
        file_menu.addAction(exit_action)
        
        file_menu.addAction("New Task").triggered.connect(self.gotoAdd)

        #edit_menu.addAction("Undo").triggered.connect()
        #self.task_view.setForeground(Qt.blak)
        #self.task_view.setAcceptDrops(True)
        #self.task_view.setDropIndicatorShown(True)
        #self.done.setDropIndicatorShown(True)
        #self.done.setAcceptDrops(True)
        #self.task_view.setDragEnabled(True)
        show_tasks(self.task_view,self.username)
        
        #self.Home.clicked.connect(self.gotohome)
        self.notification.activated.connect(self.gotonotification)
        self.comboBox.activated.connect(self.gotopf)
        self.search.clicked.connect(self.gotosearch)
        
        self.Add.clicked.connect(self.gotoAdd)
        self.Add2.clicked.connect(self.gotoAdd)
        self.sortN.clicked.connect(self.gotosort_by_name)
        self.sortA.clicked.connect(self.gotosort_by_appointment)
        self.All.clicked.connect(self.goto_showAll)
        self.task_view.itemDoubleClicked.connect(self.gotopopup)
        #self.task_view.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.task_view.customContextMenuRequested.connect(self.gotomenu)
        #self.task_view.itemClicked.connect(self.gotomenu)
        
    def contextMenuEvent(self, event):
        contextMenu=QMenu(self)
        delete=contextMenu.addAction("Delete")
        openA=contextMenu.addAction("Open")
        edit=contextMenu.addAction("Edit")
        Done=contextMenu.addAction("Done")
        action=contextMenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == openA:
            
            item=self.task_view.currentItem()
            widget.addWidget(show_task(self.username,item.text()))
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        elif action == edit:
           
            item=self.task_view.currentItem()
            i=int(item.text()[4])-1
            widget.addWidget(Edit(self.username,i))
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        elif action == delete:
            
            item=self.task_view.currentItem()
            task_list=Manage(self.username).show_tasks()
            #print(int(item.text()[4])-1)
            #print(task_list[int(item.text()[4])-1]["task name"])
            Task.remove_task(task_list[int(item.text()[4])-1]["id"])
           # Task.remove_task(task_list[int(item.text()[4])-1]["task name"],self.username)
            show_tasks(self.task_view,self.username)
            #widget.addWidget(show_tasks(self.task_view,self.username))
        elif action == Done:
           
            item=self.task_view.currentItem()
            
            widget.addWidget(Edit(self.username,item.text()))
            widget.setCurrentIndex(widget.currentIndex()+1)

    def center(self):
        qr=self.frameGeometry()
        cp =QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def gotopopup(self,item):
        
        widget.addWidget(show_task(self.username,item.text()))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    
    def gotopf(self):
        if self.comboBox.currentIndex()==1:
            #go to profile
            #print("profile")
            print(user.find("username",self.username))
            widget.addWidget(profile(self.username))
            widget.setCurrentIndex(widget.currentIndex()+1)
        #elif self.comboBox.currentIndex()==2:
            #goto favo
           # print("favo")
        elif self.comboBox.currentIndex()==3:
            #goto signout
            #print("signout")
            widget.addWidget(login())
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        else:
            print("nothing")

        
    def gotonotification(self):
        self.notification.currentIndex()
    
        
        
        
    def gotosearch(self):
        #send the search text to database
        widget.addWidget(search(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotoAdd(self):
        widget.addWidget(Ui_Form(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def goto_showAll(self):
        #print("showall")
        show_aLL(self.task_view,self.username)
        #self.task_view.addItem("rhhh")
        #class show all tasks
         
        
    def gotosort_by_name(self):
       # show tasks sorted by name from data base
       self.task_view.clear()
       task_list=Manage(self.username).sort_by_name()
       #print(task_list)
       self.x=len(task_list)
       for i in range(self.x):
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task_view.addItem(l1)
    def gotosort_by_appointment(self):
       # show tasks sorteed by appointment from data base
       self.task_view.clear()
       task_list=Manage(self.username).sort_by_end_date()
       #print(task_list)
       self.x=len(task_list)
       for i in range(self.x):
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task_view.addItem(l1)
       

    
    
    
class show_tasks(QListWidget):
    
    def __init__(self,task,username):

        super(show_tasks,self).__init__()
        #show all tasks in database
        #if addtask true
        self.task=task
        self.username=username
        task_list=Manage(self.username).show_tasks()
        self.task.clear()
        #print(task_list)
        
        self.x=len(task_list)
        for i in range(self.x):
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task.addItem(l1)
            
class show_aLL(QListWidget):
    
    def __init__(self,task,username):

        super(show_aLL,self).__init__()
        #show all tasks in database
        #if addtask true
        self.task=task
        self.task.clear()
        self.username=username
        task_list=Manage(self.username).show_tasks()
        self.x=len(task_list)
        for i in range(self.x):
            
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task.addItem(l1)
        
        
        
        
        
        
#class search(self):
    
#adding task
class Ui_Form(QMainWindow,QListWidget):
    def __init__(self,username):
        super(Ui_Form, self).__init__()
        loadUi("second.ui",self)
        self.username=username
        
        
        self.finish_Button_3.clicked.connect(self.finish1)
    
    
    def finish1(self):
        
        
        Task(self.username,self.partner_Edit.text(),self.comboBox_2.currentIndex()+1,self.dateTimeEdit_3.text(),self.dateTimeEdit_2.text(),self.comboBox.currentText(),self.partner_Edit_2.text(),None,self.partner_Edit_3.text())
        
        #l1=QListWidgetItem(self.partner_Edit.text(),self.partner_Edit3.text())
        
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)






class profile(QMainWindow):
    def __init__(self,username):
        super(profile, self).__init__()
        loadUi("profile.ui",self)
        self.username=username
        p_list=user.find("username",self.username)
        self.f_n.append(p_list[0]["first_name"])
        self.last_name_Browser.append(p_list[0]["last_name"])
        self.email_Browser.append(p_list[0]["email"])
        self.phone_Browser.append(p_list[0]["phone"])
        self.rank_Browser.append(p_list[0]["level"])
        self.upload_photo_bt.clicked.connect(self.uppl)
        self.set_password_bt.clicked.connect(self.change1)
        self.home_bt.clicked.connect(self.home1)
        self.logout_bt.clicked.connect(self.logout)
    def uppl(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label_photo.setPixmap(pixmap)
    def change1(self):
        print("change the pass pls")
    def back1(self):
        exit()   
    def home1(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
    def logout(self):
        widget.addWidget(login())
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class search(QMainWindow):
    def __init__(self,username):
        super(search,self).__init__()
        loadUi("Search.ui",self)
        self.username=username
        ###model =         #add the search list
       # mainLayout=form
        companies=[]
        task_list=Manage(self.username).show_tasks()
        self.x=len(task_list)
        for i in range(self.x):
            companies.append("Task id "+str(task_list[i]["id"])+" "+task_list[i]["task name"])
        #companies = ('Apple', 'Facebook', 'Google', 'Amazon', 'Walmart', 'Dropbox', 'Starbucks', 'eBay', 'Canon')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['Task Name'])

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)
        
        filter_proxy_model=QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterKeyColumn(0)
        
        search_filed=self.search_Edit
        search_filed.textChanged.connect(filter_proxy_model.setFilterRegExp)
        
        #table =QTableView()
        #table.setStyleSheet('font-size: 35px;')
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setModel(filter_proxy_model)
        self.table.doubleClicked.connect(self.gotoshow)
        #form.addWidget(table)
        self.Micro_Button.clicked.connect(self.gotovoice)
        
    def gotovoice(self):
        #print("voice")
        r = sr.Recognizer()
        while 1:
            with sr.Microphone() as source:
                print("Speak Anything :")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                except:
                    print("Sorry could not recognize what you said")
		#if text == 'end':
		#	break
        
    def gotoshow(self,item):
        widget.addWidget(show_spacific_task(self.username,item.data()))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class show_spacific_task(QMainWindow):
    def __init__(self,username,name):
        super(show_spacific_task,self).__init__()
        loadUi("Show_Task_final.ui",self)
        self.username=username
        self.name=name
        i=int(name[8:9])
        #print(i)
        task_list=Task.show_task_details(i)
       # print(task_list)
        #task_list=Manage(self.username).show_tasks()
        self.Task_browser.append(task_list["task"])
        self.description_browser.append(task_list["description"])
        self.partner_browser.append(task_list["partners"])
        self.location_browser.append(task_list["place"])
        self.stutes_browser.append(task_list["status"])
        self.start_browser.append(task_list["start_date"])
        self.end_browser.append(task_list["end_date"])
        
        
        self.back_Button.clicked.connect(self.goback)
        self.delete_Button.clicked.connect(self.gotodel)
        self.Edit_Button.clicked.connect(self.gotoedit)
        
        
    def goback(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotodel(self):
        i=int(self.name[8:9])
        task_list=Manage(self.username).show_tasks()
        Task.remove_task(i)
        #Task.remove_task(task_list[i]["task name"],self.username)
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        #show_tasks(self.task,self.username)
        
    def gotoedit(self):
        i=int(self.name[8:9])
        widget.addWidget(edit(self.username,i))
        widget.setCurrentIndex(widget.currentIndex()+1)

class show_task(QMainWindow):
    def __init__(self,username,name):
        super(show_task,self).__init__()
        loadUi("Show_Task_final.ui",self)
        self.username=username
        
        self.name=name
       
        i=int(name[4:6])-1
       
        
        task_list=Manage(self.username).show_tasks()
        
        self.Task_browser.append(task_list[i]["task name"])
        self.description_browser.append(task_list[i]["description"])
        self.partner_browser.append(task_list[i]["partners"])
        self.location_browser.append(task_list[i]["place"])
        self.stutes_browser.append(task_list[i]["status"])
        self.start_browser.append(task_list[i]["start_date"])
        self.end_browser.append(task_list[i]["end_date"])
        
        
        self.back_Button.clicked.connect(self.goback)
        self.delete_Button.clicked.connect(self.gotodel)
        self.Edit_Button.clicked.connect(self.gotoedit)
        
        
    def goback(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotodel(self):
        i=int(self.name[4:6])-1
        print(i)
        task_list=Manage(self.username).show_tasks()
        Task.remove_task(task_list[i]["id"])
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        #show_tasks(self.task,self.username)
        
    def gotoedit(self):
        i=int(self.name[4:6])-1
        widget.addWidget(Edit(self.username,i))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class Edit(QMainWindow):
    def __init__(self,username,name):
        super(Edit,self).__init__()
        loadUi("Edit_task_final.ui",self)
        self.username=username
        
        task_list=Manage(self.username).show_tasks()
        #print(name)
        #i=int(name[4])-1
        if task_list[name]["status"] =="New":
            j=0
        elif task_list[name]["status"] =="Done":
            j=1
        
        self.partner_Edit.setText(task_list[name]["task name"])
        self.partner_Edit_2.setText(task_list[name]["description"])
        self.partner_Edit_3.setText(task_list[name]["partners"])
        self.partner_Edit_4.setText(task_list[name]["place"])
        self.comboBox.setCurrentIndex(j)
        self.comboBox_2.setCurrentIndex(int(task_list[name]["score"])-1)
        self.start_Time_Edit.setDateTime(QDateTime.fromString(task_list[name]["start_date"], Qt.ISODate))
        self.endTimeE_dit.setDateTime(QDateTime.fromString(task_list[name]["start_date"], Qt.ISODate))
        self.finish_Button_3.clicked.connect(self.gotofinish)
        task_Edit={'task' : self.partner_Edit.text(), 'score': self.comboBox_2.currentIndex()+1,
                                   'end_date': self.endTimeE_dit.text(), 
                                   'start_date': self.start_Time_Edit.text(),
                                   'partners': self.partner_Edit_3.text(),
                                   'place': self.partner_Edit_4.text(),
                                   'status':  self.comboBox.currentText(),
                                   'description': self.partner_Edit_2.text()}
        Task.edit_task(task_list[name]["id"],task_Edit)
        #Task.edit_task(self.partner_Edit.text(),self.username,task_Edit)
        
    def gotofinish(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class edit(QMainWindow):
    def __init__(self,username,name):
        super(edit,self).__init__()
        loadUi("Edit_task_final.ui",self)
        self.username=username
        
        task_list=Task.show_task_details(name)
        print(name)
        #i=int(name[4])-1
        if task_list["status"] =="New":
            j=0
        elif task_list["status"] =="Done":
            j=1
        
        self.partner_Edit.setText(task_list["task"])
        self.partner_Edit_2.setText(task_list["description"])
        self.partner_Edit_3.setText(task_list["partners"])
        self.partner_Edit_4.setText(task_list["place"])
        self.comboBox.setCurrentIndex(j)
        self.comboBox_2.setCurrentIndex(int(task_list["score"])-1)
        self.start_Time_Edit.setDateTime(QDateTime.fromString(task_list["start_date"], Qt.ISODate))
        self.endTimeE_dit.setDateTime(QDateTime.fromString(task_list["start_date"], Qt.ISODate))
        self.finish_Button_3.clicked.connect(self.gotofinish)
        task_Edit={'task' : self.partner_Edit.text(), 'score': self.comboBox_2.currentIndex()+1,
                                   'end_date': self.endTimeE_dit.text(), 
                                   'start_date': self.start_Time_Edit.text(),
                                   'partners': self.partner_Edit_3.text(),
                                   'place': self.partner_Edit_4.text(),
                                   'status':  self.comboBox.currentText(),
                                   'description': self.partner_Edit_2.text()}
        Task.edit_task(name,task_Edit)
        #Task.edit_task(self.partner_Edit.text(),self.username,task_Edit)
        
    def gotofinish(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)


app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget.addWidget(login())
#widget.setGeometry()
#widget.setWindowState(WindowMaximized)
#widget.showFullScreen()
#widget.setFixedWidth(1024)
#widget.setFixedHeight(800)
widget.show()
app.exec_()

        


