"""
Project:SWE-CSE2020
Created by: Razzk
C-Date: 11/12/2020
"""
import datetime
# import datetime as dt
from tinydb import TinyDB, Query

db_tasks = TinyDB('taskdb.json')
tasks = Query()


class Tasks:
    """Class that handles all functions related to tasks"""

    def __init__(self, user, task, score, deadline, place="", partner=""):
        # An empty list that will contain the user tasks
        self.tasks = []
        self.status = "On-going"  # Status: state of the task: finished or on-going
        self.user = user
        self.task = task
        self.score = score
        self.deadline = deadline  # Please define the deadline in the following format: %d/%m/%Y %H:%M:%S
        self.place = place
        self.partner = partner
        self.now = datetime.now()
        self.start_date = self.now.strftime(
            "%d/%m/%Y %H:%M")  # add:%s in your code if you gonna include seconds but for both end line you can
        # defualt it with zero

    def sort_by_name(self):
        print("Tasks ordered alphabetically by name: ")
        for task in sorted(self.tasks):
            print(task)


print(db_tasks.all())
unsorted_tasks = db_tasks.all()

for i in range(1, 4):
    item = db_tasks.get(doc_id=i)
    print(item)

data = db_tasks.get(Query()['place'] == "Cairo").get('deadline')
print(data)
print(type(data))

deadline_date = datetime.datetime.strptime(data, '%d/%m/%Y %H:%M')
print(deadline_date)
print(type(deadline_date))

unsorted_tasks.sort(
    key=lambda x: datetime.datetime.strptime(x['deadline'], '%d/%m/%Y %H:%M'))  # this code will sort list with date
print(unsorted_tasks)  # that update dosn't happen in database man just in list

unsorted_tasks.sort(key=lambda x: x['task'])  # this will sort it with task name
print(unsorted_tasks)
