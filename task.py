import datetime
from tinydb import TinyDB, Query 
from operator import itemgetter
db = TinyDB('usrdb.json')                           
users = Query()  

db_tasks=TinyDB('taskdb.json')
tasks=Query()
    
class Task:
    """Class that handles all functions related to tasks."""

    def __init__(self, user, task, score, start_date, end_date, place = None, partner= None):
        
        self.status = "On-going"  # Status: state of the task: finished or on-going
        self.user = user
        self.task = task
        self.score = score
        self.end_date = end_date  # Please define the deadline in the following format: %d/%m/%Y %H:%M:%S
        self.start_date = start_date
        #self.end_date =  datetime.datetime.strptime(self.end_date, '%d/%m/%Y %H:%M')
        self.place = place
        self.partner = partner
        
        db_tasks.insert({"username": self.user, "task":self.task, "score":self.score ,
                         "start_date": self.start_date, "end_date": self.end_date,
                         "place": self.place, "partners": self.partner, "status" : self.status})
        
        
    def remove_task(self):     
        db_tasks.remove(tasks.task == self.task)
        
    def mark_as_finished(self):
        """Marks the finished tasks."""
        db_tasks.update({"status" : "Finished" } , tasks.task == self.task)
        

task1 = Task("dinaashraf", "Attend Lecture" , 10, "15/12/2020 07:02:06",  "15/12/2020 13:15:05")
task2 = Task("dinaashraf", "Write Code" , 15, "15/12/2020 07:02:04",  "15/12/2020 13:16:05")
task3 = Task("dinaashraf", "Write PHP" , 15, "15/12/2019 07:02:04",  "15/12/2020 14:02:05")
task3.mark_as_finished()
#db_tasks.truncate()



        
        
    