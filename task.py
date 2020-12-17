from tinydb import TinyDB, Query 

db_tasks=TinyDB('taskdb.json')
tasks=Query()
    
class Task:
    """Class that handles all information related to tasks."""

    def __init__(self, user, task, score, start_date, end_date, place = None, partner= None):
        
        self.status = "On-going"  # Status: state of the task: finished or on-going
        self.user = user
        self.task = task
        self.score = score
        self.end_date = end_date  # Please define the deadline in the following format: %d/%m/%Y %H:%M
        self.start_date = start_date
        self.place = place
        self.partner = partner
        
        db_tasks.insert({"username": self.user, "task":self.task, "score":self.score ,
                         "start_date": self.start_date, "end_date": self.end_date,
                         "place": self.place, "partners": self.partner, "status" : self.status})
        
        
    def remove_task(self):     
        """Remove a task from database."""
        db_tasks.remove(tasks.task == self.task)
        
    def edit_task(self, edits): # edits is a dict
        """Edit any information of a task that has been created before."""
        self.edits = edits
        for key, value in edits.items():
            db_tasks.update({key:value}, tasks.username == self.user)
        
    def mark_as_finished(self):
        """Marks the finished tasks."""
        db_tasks.update({"status" : "Finished" } , tasks.task == self.task)
        

#task1 = Task("dinaashraf", "Attend Lecture" , 10, "15/12/2020 07:02:06",  "12/12/2020 15:04")
#task2 = Task("dinaashraf", "Write Code" , 15, "15/12/2020 07:02:04",  "13/12/2020 14:59")
#task3 = Task("dinaashraf", "Write PHP" , 15, "15/12/2019 07:02:04",  "16/12/2020 15:04")
#task4 = Task("dinaashraf", "More freakin Code" , 15, "15/12/2019 07:02:04",  "16/12/2020 15:04")

#task3.mark_as_finished()
#task4.mark_as_finished()
#task1.mark_as_finished()
#task2.mark_as_finished()

#task1.edit_task({"start_date": "6/10/2020 07:05"})


#db_tasks.truncate()
        
        
    