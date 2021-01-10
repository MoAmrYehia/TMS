from tinydb import TinyDB, Query 
#from tinydb_smartcache import SmartCacheTable #Makes query cache update whenever a change in the database if encountered
#TinyDB.table_class = SmartCacheTable

db_tasks=TinyDB('taskdb.json')
tasks=Query()
    
class Task:
    """Class that handles all information related to tasks."""

    def __init__(self, username, task, score, start_date, end_date, status = "New", description = None, place = None, partner= None):
        
        self.status = status  # Status: state of the task: Finished or On-going
        self.username = username
        self.task = task
        self.score = score
        self.end_date = end_date  # Please define the deadline in the following format: %d/%m/%Y %H:%M
        self.start_date = start_date
        self.place = place
        self.partner = partner
        self.description = description
        
        db_tasks.insert({"username": self.username, "task":self.task, "description": self.description, "score":self.score ,
                         "start_date": self.start_date, "end_date": self.end_date,
                         "place": self.place, "partners": self.partner, "status" : self.status})

    @staticmethod    
    def remove_task(task_id):     
        """Remove a task from database."""
        #db_tasks.remove((tasks.task == task_name) & (tasks.username==user))
        db_tasks.remove(doc_ids = [task_id])
        
    @staticmethod  
    def edit_task(task_id, edits): # edits is a dict
        """Edit any information of a task that has been created before."""
        for key, value in edits.items():
            db_tasks.update({key:value}, doc_ids = [task_id] )
            
    @staticmethod   
    def mark_as_finished(task_id):
        """Marks the finished tasks."""
        #db_tasks.update({"status" : "Done" } ,((tasks.doc_id == task_id) & (tasks.username == user)) ) #by task name
        db_tasks.update({"status" : "New" } , doc_ids = [task_id] ) #by task name
        
        
    @staticmethod   
    def show_task_details(task_id):
        """Takes the id of the task and returns all of its details as a dictionary."""
        task = db_tasks.get(doc_id = task_id)
        return task




        
#Task.edit_task(4, {"score":50})
#Task.show_task_details(1)
#Task.mark_as_finished(1)
#Task.remove_task(3)

#Task("mohamezdrazzk", "Attend Lecturessss" , 10, "15/12/2020 07:02:06",  "12/12/2020 15:04")
#Task.edit_task("Attend Lecturessss", "mohamezdrazzk", {'score':35})
#Task.mark_as_finished("Attend Lecturessss", "mohamezdrazzk")
# = Task("mohamezdrazzk", "Attend Lecture" , 10, "15/12/2020 07:02:06",  "12/12/2020 15:04", description = "bla bla")
#task1 = Task("mohamezdrazzk", "Attend Lecture" , 10, "15/12/2020 07:02:06",  "12/12/2020 15:04")
#task2 = Task("mohamezdrazzk", "Write Code" , 10, "15/12/2020 07:02:04",  "13/12/2020 14:59")
#task3 = Task("mohamezdrazzk", "Write PHP" , 10, "15/12/2019 07:02:04",  "16/12/2020 15:04")
#task4 = Task("mohamezdrazzk", "More freakin Code" , 10, "15/12/2019 07:02:04",  "16/12/2020 15:04")

#task3.mark_as_finished()
#task4.mark_as_finished()
#task1.mark_as_finished()
#task2.mark_as_finished()

#task1.edit_task({"start_date": "6/10/2020 07:05"})


#db_tasks.truncate()
        
        
    
