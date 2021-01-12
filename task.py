from tinydb import TinyDB, Query 
db_tasks=TinyDB('taskdb.json')
tasks=Query()
from task_operations import *

class Task:
    """Class that handles all information related to tasks."""

    def __init__(self, username, task, score, start_date, end_date, status = "New", description = None, place = None, partner= None):
        
        self.status = status  # Status: state of the task: New or Done
        self.username = username
        self.task = task
        self.score = score
        self.end_date = end_date  
        self.start_date = start_date
        self.place = place
        self.partner = partner
        self.description = description
        
        db_tasks.insert({"username": self.username, "task":self.task, "description": self.description, "score":self.score ,
                         "start_date": self.start_date, "end_date": self.end_date,
                         "place": self.place, "partners": self.partner, "status" : self.status})
        Manage(self.username).set_level()
        

    @staticmethod    
    def remove_task(task_id):     
        """Remove a task from database."""
        db_tasks=TinyDB('taskdb.json')
        tasks=Query()
        db_tasks.remove(doc_ids = [task_id])
        
    @staticmethod  
    def edit_task(task_id, edits): # edits is a dict
        """Edit any information of a task that has been created before."""
        db_tasks=TinyDB('taskdb.json')
        tasks=Query()
        #print(task_id)
        for key, value in edits.items():
            db_tasks.update({key:value}, doc_ids = [task_id] )
            
    @staticmethod   
    def mark_as_finished(task_id):
        """Marks the finished tasks."""
        db_tasks=TinyDB('taskdb.json')
        tasks=Query()
        db_tasks.update({"status" : "Done" } , doc_ids = [task_id] ) #by task name
        task = db_tasks.get(doc_id = task_id)
        Manage(task["username"]).set_level()
        
        
    @staticmethod   
    def show_task_details(task_id):
        """Takes the id of the task and returns all of its details as a dictionary."""
        db_tasks=TinyDB('taskdb.json')
        tasks=Query()
        task = db_tasks.get(doc_id = task_id)
        return task


#Task.edit_task(4, {"score":50})
#Task.show_task_details(1)
#Task.mark_as_finished(1)
#Task.remove_task(3)

#db_tasks.truncate()
        
        
    
