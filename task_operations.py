# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:47:41 2020

@author: dinaa
"""
import datetime
import threading 
import continuous_threading
import time
from tinydb import TinyDB, Query 
from operator import itemgetter

db_tasks = TinyDB('taskdb.json')
tasks= Query()
db_scoring = TinyDB('scoringdb.json')
scores = Query()


class Manage():
    """Class that manages operations on the user's tasks"""
    def __init__(self,username):
        self.username = username
        self.unsorted_tasks = db_tasks.search(tasks.username == self.username)
        self.x = len(self.unsorted_tasks) #Total number of tasks
        
        self.on_going_tasks = db_tasks.search((tasks['status'] == "On-going") & (tasks.username == self.username))
        self.number_on_going = len(self.on_going_tasks)
        
        self.finished_tasks = db_tasks.search((tasks.status == "Finished") & (tasks.username == self.username))
        self.number_finished = len(self.finished_tasks)
        
        #Scoring
        db_scoring.insert({"username": self.username , "level": None , "Score": None })
        
    def sort_by_name(self):
        """Sorts the user's tasks alphabetically."""
        self.unsorted_tasks.sort(key=lambda x: x['task'])
        self.result = sorted(self.unsorted_tasks, key=itemgetter('task'))
        for i in self.result:
            print(i['task'])
 

    def sort_by_end_date(self):
        """Sorts the user's tasks based on end-date"""
        self.unsorted_tasks.sort(key=lambda x: datetime.datetime.strptime(x['end_date'], '%d/%m/%Y %H:%M'))
  
        for i in range(self.x):
            self.unsorted_tasks[i]['end_date'] = datetime.datetime.strptime(self.unsorted_tasks[i]['end_date'], '%d/%m/%Y %H:%M')
            print(self.unsorted_tasks[i]['task'])


        
    def show_progress(self):
        """Shows finished and on-going tasks."""
        for i in self.on_going_tasks:
            print("On-going task, " , i['task'])
            
        if self.finished_tasks:
            for i in self.finished_tasks:
                print("Finished task, ", i["task"])
    
          
    def show_weekly_report(self):
        """Produces a weekly report every Friday that shows (un)/finished tasks on 12 PM."""
        self.unsorted_tasks = db_tasks.search(tasks.username == self.username)
        self.total_score = 0 #Total score of the week
        self.today = datetime.datetime.today().replace(second = 0, minute = 0, hour =0, microsecond =0 ) #Return today's date
        self.finished_before_deadline = []
        self.not_finished_before_deadline = []
        
        #Getting all days of the current week to see which tasks have been finished on this week
        
        self.day_1 = self.today - datetime.timedelta(days = 1)
        self.day_2 = self.today - datetime.timedelta(days = 2)
        self.day_3 = self.today - datetime.timedelta(days = 3)
        self.day_4 = self.today - datetime.timedelta(days = 4)
        self.day_5 = self.today - datetime.timedelta(days = 5)
        self.day_6 = self.today - datetime.timedelta(days = 6)

        if self.today.weekday() == 5: #5 means Friday
            for i in range (0,self.x):
                
                #Making sure all end_dates are datetime objects not str
                try:
                    self.unsorted_tasks[i]['end_date'] = datetime.datetime.strptime(self.unsorted_tasks[i]['end_date'], '%d/%m/%Y %H:%M')
                    (self.unsorted_tasks[i]["end_date"]) =  (self.unsorted_tasks[i]["end_date"]).replace(second = 0, minute = 0, hour =0, microsecond =0 )
                except: 
                    pass
                
                #Finding out which tasks were finished this week and which weren't
                if (self.unsorted_tasks[i]['end_date'])== self.today or self.day_1 or self.day_2 or self.day_2 or self.day_3 or self.day_4 or self.day_5  or self.day_6:
                 #       print('Hello')
                            
                    if self.unsorted_tasks[i]['status'] == "Finished":
                        self.finished_before_deadline.append(self.unsorted_tasks[i]["task"])
                        self.total_score = self.unsorted_tasks[i]["score"] + self.total_score
                            
                    if self.unsorted_tasks[i]['status'] == "On-going":
                        self.not_finished_before_deadline.append(self.unsorted_tasks[i]["task"])
 
            if self.finished_before_deadline:
                print("Congratulations your overall score this week is ", self.total_score)
                print("Take a look at the tasks you have finished:")
                for i in self.finished_before_deadline:
                    print(i)
                
            if self.not_finished_before_deadline:
                print("Unfortunately you haven't finished these tasks due this week: ")
                for i in self.not_finished_before_deadline:
                    print(i)

    def push_notifications(self):
        """Pushes a notification at the task's end date."""
        self.count = self.x #The number of tasks for each user which will determine the end conidition of the while loop
        
        #Making sure that all end_dates are in datetime format not str
        for i in range (0,self.x):
            try:
                self.unsorted_tasks[i]['end_date'] = datetime.datetime.strptime(self.unsorted_tasks[i]['end_date'], '%d/%m/%Y %H:%M')  
            except: 
                pass
            
        # Measuring the time now and calculating the difference between it and the end_date of the task
        while self.count:
            for i in range (0,self.x): #Iterating over the tasks where x is the number of tasks
                 self.now = datetime.datetime.now().replace(microsecond=0).replace(second = 0)
           #     print(type(self.now))
           #     print(type(self.unsorted_tasks[i]["end_date"]))
                 self.diff = (self.unsorted_tasks[i]["end_date"] - self.now).total_seconds() #Time difference
                 
                 if int(self.diff) == 0 and self.unsorted_tasks[i]["status"] == "On-going":
                    print("Task deadline reminder for >> ", self.unsorted_tasks[i]["task"])
                    self.count = self.count - 1

            time.sleep(10) # We check for new tasks every 10 seconds
            
    def set_level(self):
        """Determines silver/gold/bronze""" 
        #Hi, Razzk, we need to have a flag that indicates that the user has used our App for a month or 2 or 3
        #Here I assume no flags and I set the level based only on the user's scores
        self.total_score = 0
        
        #Score Calculation
        for i in range(self.x):
            if self.unsorted_tasks[i]['status'] == "Finished":
                self.total_score = self.unsorted_tasks[i]["score"] + self.total_score
                
        if (self.number_finished/self.x) >= 0.5 and (self.number_finished/self.x) < 0.7 and (self.number_on_going!=0): #Bronze Level
            db_scoring.update({"level": "Bronze", "Score":self.total_score }, scores.username == self.username)
            print('Your level is Bronze')

        if (self.number_finished/self.x) >= 0.7 and (self.number_finished/self.x) < 0.8 and (self.number_on_going!=0) : #Silver Level
            db_scoring.update({"level": "Silver", "Score":self.total_score }, scores.username == self.username)
            print('Your level is Silver')
            
        if (self.number_finished/self.x) >= 0.8 and (self.number_on_going!=0): #Gold Level         
            db_scoring.update({"level": "Gold", "Score":self.total_score }, scores.username == self.username)
            print('Your level is Gold')
                
        elif self.number_on_going == 0 and self.number_finished: #Gold Level
            db_scoring.update({"level": "Gold", "Score":self.total_score }, scores.username == self.username)
            print('Your level is Gold')
            



manage_dina = Manage("dinaashraf")
manage_ashraf = Manage("ashraf")

manage_dina.set_level()
manage_ashraf.set_level()

#manage_dina.sort_by_end_date()
#manage_dina.show_weekly_report()
#manage_dina.sort_by_name()
#manage_dina.show_progress()
#manage_dina.push_notifications()
#Running a thread
#th = threading.Thread(target = manage_dina.push_notifications(), ).start()

#db_scoring.truncate()
