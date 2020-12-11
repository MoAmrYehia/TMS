
"""
Project:SWE-CSE2020
Created by: Dina Ashraf
C-Date: 12/10/2020 
"""
from datetime import datetime 
#import datetime as dt
from tinydb import TinyDB, Query 
from operator import itemgetter
db = TinyDB('usrdb.json')                           
users = Query()  

db_tasks=TinyDB('taskdb.json')
tasks=Query()

class Tasks():
    """Class that handles all functions related to tasks"""
    def __init__(self):
        #An empty list that will contain the user tasks
        self.tasks=[]
        self.status = "On-going" #Status: state of the task: finished or on-going
        
    def add_task(self, user, task, score, deadline, place="", partner=""):
        """Method that creates the tasks and adds them to lists"""
        self.user=user
        self.task=task
        self.score=score
        self.deadline=deadline  #Please define the deadline in the following format: %d/%m/%Y %H:%M:%S
        self.place=place
        self.partner=partner
        
        self.now = datetime.now()
        self.start_date= self.now.strftime("%d/%m/%Y %H:%M:%S")
        
        self.tasks.append(self.task)
      
        db_tasks.insert({"username": self.user, "task":self.task, "score":self.score ,
                         "start_date": self.start_date, "deadline": self.deadline,
                         "place": self.place, "partners": self.partner, "status" : self.status})
     
        db.update({'tasks': self.tasks}, self.user== users.username ) #assigning the tasks to the user's database
        
    def show_tasks(self):
        for task in self.tasks:
            print(task)
        
    def sort_by_name(self):
        print("Tasks ordered alphabetically by name: ")
        for task in sorted(self.tasks):
            print(task)
            
    def sort_by_end_date(self):
        
        tasks.deadline =datetime.strptime(str(tasks.deadline), '%d/%m/%y %H:%M')
        self.undecorated = db_tasks.search(tasks.username==self.user) #All tasks associated with the user
        self.result = sorted(self.undecorated, key=itemgetter('deadline'))
        for i in self.result:
            print(i['task'] , i['deadline'])
        
            
    def mark_as_finished(self,name):
        self.finished_task_name = name
        db_tasks.update({"status" : "Finished" } , self.finished_task_name== tasks.task)    
    def show_tasks_in_progress(self):
        self.on_going_tasks = db_tasks.search(tasks.status == "On-going")
        for i in self.on_going_tasks:
            print(i['task'])
            


#Create a user for testing
db.insert(
                    {'first_name': 'Dina', 'last_name': 'Ashraf', 'email': 'ddd1111@gmail.com',
                     'phone': 111111111,
                     'username': 'dinaashraf',
                     'password': 10, 'role': 'user'})


#Create an instance of the list of tasks
to_do_list =  Tasks()
#Add tasks
to_do_list.add_task('dinaashraf', 'Do homework', 10, '15/10/2019 01:02', place="Cairo") #task with place attribute and no partner
to_do_list.add_task('dinaashraf', 'Write code', 10, '12/12/2020 01:01') #task with neither place nor partner attribute
#task with partner and place attributes
to_do_list.add_task('dinaashraf', 'Write the code of thr project', 10, '11/10/2020 02:01' , "cairo", "mohamedrazzk") 

#Testing sort_by_name
to_do_list.sort_by_name()


#Testing the sort_by_end_date()
to_do_list.sort_by_end_date()  ##currently causes a ValueError


#Testing mark_as_finished()
to_do_list.mark_as_finished("Do homework")


#Testing showing tasks in progress
to_do_list.show_tasks_in_progress()



db_tasks.truncate() #-- clearing out the tasks database






# In[ ]:




