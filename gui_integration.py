# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# signals use connect


#from tinydb import TinyDB
from data_rw import *
import sys
import io
#import gmaps
import googlemaps
#import gmaps.datasets
#gmaps.configure(api_key='AIzaSyBv3H5SMUpoLqqFmoeg1tbJS6UBmoEPVbk')
map_client=googlemaps.Client('AIzaSyBv3H5SMUpoLqqFmoeg1tbJS6UBmoEPVbk')
import folium
from PyQt5 import QtWidgets,QtWebEngineWidgets

from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget,QListWidget,QListWidgetItem,QDialog,QWidget,QHBoxLayout,QFileDialog, QAction,QTableView,QHeaderView,QVBoxLayout,QMenu

from PyQt5.QtCore import Qt, QSortFilterProxyModel,QDateTime,QMimeData
from PyQt5.QtGui import QStandardItemModel, QStandardItem,QPixmap,QDrag
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.uic import loadUi
#import socket

from task import *


from task_operations import*
from auth import *
import speech_recognition as sr

#from PyQt5 import QPixmap



class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi("mainwindow.ui",self)
        self.loginbutton.clicked.connect(self.loginfunc)
        pixmap=QPixmap("Obj/ico/TMS_Logo.png")
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())
        #self.setLayout(QImage("download.jpeg"))
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
            self.label_2.setText(error)
            #print(error)
       
        else:
            self.label_2.setText(error)
            #print(error)
            
        
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
        pixmap=QPixmap("TMS_Logo.png")
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())
        self.login.clicked.connect(self.loginfunc)
        self.email.setPlaceholderText("Email Address")
        self.password.setPlaceholderText("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def loginfunc(self):
        status,error=user_auth(self.email.text(),self.password.text()).login()
        self.label_2.setText(error)
        #print(error)
        
        """if status == True then go to the admin windwo"""
        
        
        
        
class forgetpass(QMainWindow):
    def __init__(self):
        super(forgetpass,self).__init__()
        loadUi("forget.ui",self)
        self.email.setPlaceholderText("Email Address")
        self.sendmail.clicked.connect(self.sendEmail)
        
    def sendEmail(self):
        if self.email.text()==None:
            self.label_2.setText("Enter valid Email")
        else:
            user_auth(self.email.text(),"").reset()
            # want a function take the email only and send the code
            #print("send email to",self.email.text())
            #lo =writecode(self.email.text())
            widget.addWidget(writecode(self.email.text()))
            widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
        
    
    
class writecode(QMainWindow):
    def __init__(self,email):
        super(writecode,self).__init__()
        loadUi("write_code.ui",self)
        self.email=email
        self.code.setPlaceholderText("Enter code")
        self.label.setText("email sent to :"+ email)
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
            user.modify(self.email, "password", self.passw.text())
            if status==True:
                widget.addWidget(login())
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.label_2.setText("Enter another passowrd")
                #print("enter another pass")
            
        else:
            self.label_2.setText("Not matched")
            #print("notmatched")
    
    
    
    
    
class signup(QMainWindow):
    def __init__(self):
        super(signup,self).__init__()
        loadUi("sign_up.ui",self)
        pixmap=QPixmap("107341878-sign-up-button-click-glyph-icon-silhouette-symbol-new-user-registration-membership-hand-pressing-but.jpg")
        self.label.setPixmap(pixmap)
        #self.label.setSize(100,100)
        #self.label.resize(pixmap.width(),pixmap.height())
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
            #print("matched")
            User=user(self.firstname.text(),self.lastname.text(),self.email.text(),self.phone.text(),self.username.text(),self.role.currentText(),self.password.text())
            status,error=User.adduser()
            if status==True:
                widget.addWidget(login())
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.label_2.setText(error)
                #print(error)
                
        else:
            self.label_2.setText("Not matched")
            #print("Not matched")
        
        





class mainWindowTask(QMainWindow):
    def __init__(self,username):
        super(mainWindowTask, self).__init__()
        loadUi("mainwindow_task.ui",self)
        self.Add2.setIcon(QIcon("Obj/ico/images_1.jpeg"))
        self.search.setIcon(QIcon("Ojb/ico/images.png"))
        self.notification.clear()
        self.comboBox.clear()
        self.notification.addItem(QIcon("appointment-reminders.png")," ")
        self.comboBox.addItem(QIcon("download (1).jpeg")," ")
        self.comboBox.addItem("profile")
        self.comboBox.addItem("SignOut")
        #self.notification.setStyleSheet("border-image : (file:///home/ehab/Desktop/download.jpeg)") 
        #self.Add2.setStyleSheet("background-image : url(images (1).jpeg)")
        Manage(username).start_notification()
        self.username=username
        #print(Manage(self.username).show_tasks())
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
        flag,finished_before_deadline,not_finished,total_score=Manage(self.username).show_weekly_report()
        if flag==True:
            self.notification.addItem("weakly report")
            
        show_tasks(self.task_view,self.username)
        show_done_tasks(self.done,self.username)
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
            i=int(item.text()[4:6])-1
            print(i)
            widget.addWidget(Edit(self.username,i))
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        elif action == delete:
            
            item=self.task_view.currentItem()
            task_list=Manage(self.username).show_ongoing_tasks()
            
            Task.remove_task(task_list[int(item.text()[4:6])-1]["id"])
           
            show_tasks(self.task_view,self.username)
            
        elif action == Done:
            task_list=Manage(self.username).show_ongoing_tasks()
            item=self.task_view.currentItem()
            Task.mark_as_finished(task_list[int(item.text()[4:6])-1]["id"])
            widget.addWidget(mainWindowTask(self.username))
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
            
            widget.addWidget(profile(self.username))
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        elif self.comboBox.currentIndex()==2:
    
            widget.addWidget(login())
            widget.setCurrentIndex(widget.currentIndex()+1)
            
        else:
            print("nothing")

        
    def gotonotification(self):
        if self.notification.currentIndex==1:
            widget.addWidget(login())
            widget.setCurrentIndex(widget.currentIndex()+1)
    
        
        
        
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
            if i%2:
                l1.setBackground(Qt.darkGray)
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
            if i%2:
                l1.setBackground(Qt.darkGray)
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task_view.addItem(l1)
       

    
class show_done_tasks(QListWidget):
    
    def __init__(self,task,username):

        super(show_done_tasks,self).__init__()
        
        self.task=task
        self.username=username
        task_list=Manage(self.username).show_finished_tasks()
        
        self.task.clear()
        #print(task_list)
        
        self.x=len(task_list)
        for i in range(self.x):
           
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            if i%2:
                l1.setBackground(Qt.darkGray)
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task.addItem(l1)
    
class show_tasks(QListWidget):
    
    def __init__(self,task,username):

        super(show_tasks,self).__init__()
        
        self.task=task
        self.username=username
        task_list=Manage(self.username).show_ongoing_tasks()
        #task_list=Manage(self.username).show_tasks()
        self.task.clear()
        #print(task_list)
        
        self.x=len(task_list)
        for i in range(self.x):
            task_list=Manage(self.username).show_ongoing_tasks()
        
            l1=QListWidgetItem()
            l1.setFont(QFont("Arial font", 16))
            #l1.setFrameStyle()
            if i%2:
                l1.setBackground(Qt.darkGray)
            #l1.setStyleSheet('QListWidget { background: lightblue; border: solid black;}' )
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
            if i%2:
                l1.setBackground(Qt.darkGray)
            #l1.setStyleSheet('QListWidget { background: lightblue; border: solid black;}' )
            l1.setText("Task"+str(i+1)+"\n"+"name: "+task_list[i]["task name"]+"\n"+"score: "+str(task_list[i]["score"])+"\n"+"partners:"+task_list[i]["partners"]+"\n"+"EndDate: "+task_list[i]["end_date"]+"\n")
            self.task.addItem(l1)
        

    
#adding task
class Ui_Form(QMainWindow,QListWidget):
    def __init__(self,username):
        super(Ui_Form, self).__init__()
        loadUi("Add_Task_final.ui",self)
        pixmap=QPixmap("Obj/ico/task_clip.jpg")
        
        self.labelmg.setPixmap(pixmap)
        
        self.toolButton.setIcon(QIcon("download (2).jpeg"))
        self.username=username
        self.toolButton.clicked.connect(self.gotomap)
        self.partner_Edit.textChanged.connect(self.textchanged)
        self.finish_Button_3.clicked.connect(self.finish1)
        
    def textchanged(self,text):
        #print(text)
        flag,t=Manage(self.username).search(text)
        #print(Manage(self.username).search(text))
        if flag==1:
            self.partner_Edit.setText(t)
    def gotomap(self):
        Maap()
        
    def finish1(self):
    
        Task(self.username,self.partner_Edit.text(),self.comboBox_2.currentIndex()+1,self.start_Time_Edit.text(),self.endTimeE_dit.text(),self.comboBox.currentText(),self.partner_Edit_2.text(),self.partner_Edit_4.text(),self.partner_Edit_3.text())
        
        #l1=QListWidgetItem(self.partner_Edit.text(),self.partner_Edit3.text())
        
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)






class profile(QMainWindow):
    def __init__(self,username):
        super(profile, self).__init__()
        loadUi("Profile_final.ui",self)
        self.username=username
        p_list=user.find("username",self.username)
        self.f_n.append(p_list[0]["first_name"])
        self.last_name_Browser.append(p_list[0]["last_name"])
        self.email_Browser.append(p_list[0]["email"])
        self.phone_Browser.append(p_list[0]["phone"])
        self.rank_Browser.append(p_list[0]["level"])
        #self.upload_photo_bt.clicked.connect(self.uppl)
        self.set_password_bt.clicked.connect(self.change1)
        self.home_bt.clicked.connect(self.home1)
        self.logout_bt.clicked.connect(self.logout)
        self.Edit_bt.clicked.connect(self.gotoeditprofile)
    
    def change1(self):
        widget.addWidget(reset_pass(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
    def back1(self):
        exit()   
    def home1(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
    def logout(self):
        widget.addWidget(login())
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoeditprofile(self):
        widget.addWidget(edit_profile(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)

class edit_profile(QMainWindow):
    def __init__(self,username):
        super(edit_profile, self).__init__()
        loadUi("Edit_Profile2.ui",self)
        self.username=username
        p_list=user.find("username",self.username)
        print(p_list)
        self.f_n.setText(p_list[0]["first_name"])
        self.last_name_Edit.setText(p_list[0]["last_name"])
        self.email_Edit.setText(p_list[0]["email"])
        self.phone_Edit.setText(p_list[0]["phone"])
        #self.rank_Edit.setText(p_list[0]["level"])
        
        
        self.done_bt.clicked.connect(self.home1)
        
    
    
    def home1(self):
        user.modify(self.username, "first_name", self.f_n.text())
        user.modify(self.username, "last_name", self.last_name_Edit.text())
        user.modify(self.username, "email", self.email_Edit.text())
        user.modify(self.username, "phone", self.phone_Edit.text())
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class reset_pass(QMainWindow):
    def __init__(self,username):
        super(reset_pass,self).__init__()
        loadUi("Password_final.ui",self)
        self.username=username
        self.old_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_Edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.finish_Button.clicked.connect(self.gotoreset)
        self.finish_Button_2.clicked.connect(self.gotoback)
        
    def gotoreset(self):
        if self.new_Edit.text()==self.confirm_Edit.text():
            status=user_auth(str(self.username),"").reset_handler(self.new_Edit.text())
            if status==True:
                widget.addWidget(login())
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.label.setText("Enter Another Password")
                print("enter another pass")
            
        else:
            self.label.setText("Not Matched")
            print("notmatched")
    def gotoback(self):
        widget.addWidget(profile(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class search(QMainWindow):
    def __init__(self,username):
        super(search,self).__init__()
        loadUi("Search.ui",self)
        pixmap=QPixmap("images.png")
        pixmap_1=QPixmap("Obj/ico/microphone.png")
        self.label.setPixmap(pixmap)
        #self.Micro_Button.setSize(100,100)
        self.Micro_Button.setIcon(QIcon("Obj/ico/microphone.png"))
        self.username=username
        ###model =         #add the search list
       # mainLayout=form
        companies=[]
        task_list=Manage(self.username).show_tasks()
        self.x=len(task_list)
        for i in range(self.x):
            companies.append("Task id "+str(task_list[i]["id"])+"  "+task_list[i]["task name"])
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
        self.search_Button.clicked.connect(self.gotoback)
        self.table.doubleClicked.connect(self.gotoshow)
        #form.addWidget(table)
        self.Micro_Button.clicked.connect(self.gotovoice)
        
    def gotoback(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotovoice(self):
       
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            self.label_2.setText("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                self.search_Edit.setText(text)
                print("You said : {}".format(text))
            except:
                self.label_2.setText("Sorry could not recognize what you said")
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
        i=int(name[8:10])
        print(i)
        task_list=Task.show_task_details(i)
        print(task_list)
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
        self.toolButton.setIcon(QIcon("download (2).jpeg"))
        self.username=username
        
        self.name=name
       
        i=int(name[4:6])-1
       
        
        task_list=Manage(self.username).show_ongoing_tasks()
        
        self.Task_browser.append(task_list[i]["task name"])
        self.description_browser.append(task_list[i]["description"])
        self.partner_browser.append(task_list[i]["partners"])
        self.location_browser.append(task_list[i]["place"])
        self.stutes_browser.append(task_list[i]["status"])
        self.start_browser.append(task_list[i]["start_date"])
        self.end_browser.append(task_list[i]["end_date"])
        
        self.toolButton.clicked.connect(self.gotomap)
        self.back_Button.clicked.connect(self.goback)
        self.delete_Button.clicked.connect(self.gotodel)
        self.Edit_Button.clicked.connect(self.gotoedit)
        
    def gotomap(self):
        Maap()
    def goback(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotodel(self):
        i=int(self.name[4:6])-1
        #print(i)
        task_list=Manage(self.username).show_ongoing_tasks()
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
        self.name=name
        pixmap=QPixmap("135638555_108817857718563_7138284607891211623_n.jpg")
        self.labelmg.setPixmap(pixmap)
        self.toolButton.setIcon(QIcon("download (2).jpeg"))
        task_list=Manage(self.username).show_ongoing_tasks()
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
        self.toolButton.clicked.connect(self.gotomap)
        
    def gotomap(self):
        Maap()
        #Task.edit_task(self.partner_Edit.text(),self.username,task_Edit)
        
    def gotofinish(self):
        task_list=Manage(self.username).show_ongoing_tasks()
        task_Edit={'task' : self.partner_Edit.text(), 'score': self.comboBox_2.currentIndex()+1,
                                   'end_date': self.endTimeE_dit.text(), 
                                   'start_date': self.start_Time_Edit.text(),
                                   'partners': self.partner_Edit_3.text(),
                                   'place': self.partner_Edit_4.text(),
                                   'status':  self.comboBox.currentText(),
                                   'description': self.partner_Edit_2.text()}
        Task.edit_task(task_list[self.name]["id"],task_Edit)
        print(task_list[self.name]["id"])
        #print(task_Edit)
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class edit(QMainWindow):
    def __init__(self,username,name):
        super(edit,self).__init__()
        loadUi("Edit_task_final.ui",self)
        self.username=username
        pixmap=QPixmap("135638555_108817857718563_7138284607891211623_n.jpg")
        self.labelmg.setPixmap(pixmap)
        self.toolButton.setIcon(QIcon("download (2).jpeg"))
        task_list=Task.show_task_details(name)
        #print(name)
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
        self.toolButton.clicked.connect(self.gotomap)
        
    def gotomap(self):
        Maap()
        #Task.edit_task(self.partner_Edit.text(),self.username,task_Edit)
        
    def gotofinish(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)

class report(QMainWindow):
    def __init(self,username):
        super(report,self).__init__()
        loadUi("Report_final.ui",self)
        flag,finished_before_deadline,not_finished,total_score=Manage(self.username).show_weekly_report()
        
        for row,task in enumerate(finished_before_deadline):
            self.tableView.setItem(row,0,task)
            
        for row,task in enumerate(not_finished):
            self.tableView_2.setItem(row,0,task)
        
        self.textBrowser.append(total_score)
        self.finish_Button.clicked.connect(self.gotoback)
        
    def gotoback(self):
        widget.addWidget(mainWindowTask(self.username))
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Maap(QMainWindow):
    def __init__(self):
        super(Maap,self)
        
        #layout=QVBoxLayout()
        #widget.setLayout(layout)
        #self.window=AnotherWindow()
        coordinate=(30.066211722837554, 31.275636626805426)   
        m=folium.Map(title="Faculty of Engineering",zoom_start=13,location=coordinate)
        data=io.BytesIO()
        m.save(data,close_file=False)
        webView=QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        #layout.addWidget(webView)
        #layout.show()
       # widget2=QtWidgets
        
        widget2.addWidget(webView)
        widget2.setCurrentIndex(widget.currentIndex()+1)
        widget2.show()
        
        
app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
widget2=QtWidgets.QStackedWidget()
widget.addWidget(login())
#widget.setGeometry()
#widget.setWindowState(WindowMaximized)
#widget.showFullScreen()
#widget.setFixedWidth(1024)
#widget.setFixedHeight(800)
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
