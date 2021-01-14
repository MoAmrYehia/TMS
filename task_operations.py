# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:47:41 2020

@author: dinaa

Hall of Fame coordinator : @ahmed Gnina
Testing Code Review : @ahmed Gnina

"""
from push_notification_sc import push_notification
import datetime
import threading
import time
from tinydb import TinyDB, Query
import re

Notifer=30
db_tasks = TinyDB('taskdb.json')
tasks = Query()
db_scoring = TinyDB('scoringdb.json')
scores = Query()


class Manage():
    """Class that manages operations on the user's tasks."""

    def __init__(self, username):
        self.username = username

    def show_tasks(self):
        """Shows the user's tasks."""
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        unsorted_tasks = db_tasks.search(tasks.username == self.username)
        x = len(unsorted_tasks)  # Total number of tasks
        task_list = []
        for i in range(x):
            task_list.append({'task name' : unsorted_tasks[i]['task'], 'score': unsorted_tasks[i]['score'],
                                   'end_date': unsorted_tasks[i]['end_date'], 
                                   'start_date': unsorted_tasks[i]['start_date'],
                                   'partners': unsorted_tasks[i]['partners'],
                                   'place': unsorted_tasks[i]['place'],
                                   'status':  unsorted_tasks[i]['status'],
                                   'description': unsorted_tasks[i]['description'],
                                   'id': unsorted_tasks[i].doc_id
                                  })
        return task_list

    def sort_by_name(self):
        """Sorts the user's tasks alphabetically."""
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        unsorted_tasks = db_tasks.search((tasks['status'] == "New") & (tasks.username == self.username))
        x = len(unsorted_tasks)  # Total number of tasks
        unsorted_tasks.sort(key=lambda x: x['task'])  # Sorting by name
        task_list = []
        for i in range(x):
            task_list.append({'task name' : unsorted_tasks[i]['task'], 'score': unsorted_tasks[i]['score'],
                                   'end_date': unsorted_tasks[i]['end_date'], 
                                   'start_date': unsorted_tasks[i]['start_date'],
                                   'partners': unsorted_tasks[i]['partners'],
                                   'place': unsorted_tasks[i]['place'],
                                   'status':  unsorted_tasks[i]['status'],
                                   'description': unsorted_tasks[i]['description'],
                                   'id': unsorted_tasks[i].doc_id
                                  })
        return task_list

    def sort_by_end_date(self):
        """Sorts the user's tasks based on end-date"""
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        unsorted_tasks = db_tasks.search((tasks['status'] == "New") & (tasks.username == self.username))
        x = len(unsorted_tasks)  # Total number of tasks
        try:
            unsorted_tasks.sort(key=lambda x: datetime.datetime.strptime(x['end_date'], '%d/%m/%Y %H:%M'))
        except:
            pass

        task_list = []
        for i in range(x):
            task_list.append({'task name' : unsorted_tasks[i]['task'], 'score': unsorted_tasks[i]['score'],
                                   'end_date': unsorted_tasks[i]['end_date'], 
                                   'start_date': unsorted_tasks[i]['start_date'],
                                   'partners': unsorted_tasks[i]['partners'],
                                   'place': unsorted_tasks[i]['place'],
                                   'status':  unsorted_tasks[i]['status'],
                                   'description': unsorted_tasks[i]['description'],
                                   'id': unsorted_tasks[i].doc_id
                                  })
        return task_list
    
    
    def show_ongoing_tasks(self):
        """Shows on-going tasks."""
        ongoing_list = []  # List of on-going tasks
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        on_going_tasks = db_tasks.search((tasks.status == "New") & (tasks.username == self.username))
        
        for i in range(len(on_going_tasks)):
            ongoing_list.append({'task name' : on_going_tasks[i]['task'], 'score': on_going_tasks[i]['score'],
                                   'end_date': on_going_tasks[i]['end_date'], 
                                   'start_date': on_going_tasks[i]['start_date'],
                                   'partners': on_going_tasks[i]['partners'],
                                   'place': on_going_tasks[i]['place'],
                                   'status':  on_going_tasks[i]['status'],
                                   'description': on_going_tasks[i]['description'],
                                   'id': on_going_tasks[i].doc_id
                                  })
        return ongoing_list
 

    def show_finished_tasks(self):
        """Shows finished tasks."""
        finished_list = []  # List of on-going tasks
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        finished_tasks = db_tasks.search((tasks['status'] == "Done") & (tasks.username == self.username))
        
        for i in range(len(finished_tasks)):
            finished_list.append({'task name' : finished_tasks[i]['task'], 'score': finished_tasks[i]['score'],
                                   'end_date': finished_tasks[i]['end_date'], 
                                   'start_date':finished_tasks[i]['start_date'],
                                   'partners': finished_tasks[i]['partners'],
                                   'place': finished_tasks[i]['place'],
                                   'status':  finished_tasks[i]['status'],
                                   'description': finished_tasks[i]['description'],
                                   'id': finished_tasks[i].doc_id
                                  })
        return finished_list
        
    def show_weekly_report(self):
        """Produces a weekly report every Friday that shows (un)/finished tasks."""
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        unsorted_tasks = db_tasks.search(tasks.username == self.username)
        x = len(unsorted_tasks)
        total_score = 0  # Total score of the week
        today = datetime.datetime.today().replace(second=0, minute=0, hour=0, microsecond=0)  # Return today's date
        finished_before_deadline = []
        not_finished_before_deadline = []
        flag=0

        # Getting all days of the current week to see which tasks have been finished on this week

        day_1 = today - datetime.timedelta(days=1)
        day_2 = today - datetime.timedelta(days=2)
        day_3 = today - datetime.timedelta(days=3)
        day_4 = today - datetime.timedelta(days=4)
        day_5 = today - datetime.timedelta(days=5)
        day_6 = today - datetime.timedelta(days=6)

        if today.weekday() == 4:  # 4 means Friday
            flag=1
            for i in range(0, x):

                # Making sure all end_dates are datetime objects not str
                try:
                    unsorted_tasks[i]['end_date'] = datetime.datetime.strptime(unsorted_tasks[i]['end_date'],
                                                                                    '%d/%m/%Y %H:%M')
                    (unsorted_tasks[i]["end_date"]) = (unsorted_tasks[i]["end_date"]).replace(second=0,
                                                                                                        minute=0,
                                                                                                        hour=0,
                                                                                                        microsecond=0)
                except:
                    pass

                # Finding out which tasks were finished this week and which weren't
                if (unsorted_tasks[i]['end_date']) == today or day_1 or day_2  or day_3 or day_4 or day_5 or day_6:

                    if unsorted_tasks[i]['status'] == "Done":
                        finished_before_deadline.append(unsorted_tasks[i]["task"])
                        total_score = unsorted_tasks[i]["score"] + total_score

                    if unsorted_tasks[i]['status'] == "New":
                        not_finished_before_deadline.append(unsorted_tasks[i]["task"])

        return flag, finished_before_deadline, not_finished_before_deadline, total_score
        # Returns list of finished tasks, list of not finished tasks & total score of the week

    def push_notifications(self):
        """Pushes a notification at the task's end date."""
        task_dates = [] 
        task_names = []
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()

        # Getting the On-going tasks only and excluding the finished tasks
        on_going_tasks = db_tasks.search((tasks['status'] == "New") & (tasks.username == self.username))
        on_going_tasks.sort(key=lambda x: datetime.datetime.strptime(x['end_date'], '%d/%m/%Y %H:%M'))
        number_on_going = len(on_going_tasks)

        # Making sure that all end_dates are in datetime format not str
        for i in range(0, number_on_going):  # number_on_going is the no. of on-going tasks
            try:
                on_going_tasks[i]['end_date'] = datetime.datetime.strptime(on_going_tasks[i]['end_date'],
                                                                                '%d/%m/%Y %H:%M')
            except:
                pass
            task_dates.append(on_going_tasks[i]['end_date'])  # Adding the tasks to the list
            task_names.append(on_going_tasks[i]['task'])

        # Measuring the time now and calculating the difference between it and the end_date of the task
        while task_dates:

            now = datetime.datetime.now().replace(microsecond=0).replace(second=0)
            diff = (task_dates[0] - now).total_seconds()  # Time difference in seconds


            if diff <= Notifer:  # Print the notification is the time difference is Notifer seconds or less assuming that will be variable
                push_notification(task_names[0])
                try:
                    task_dates.pop(0)  # Removing the task from the list after notification's done
                    task_dates.pop(0)
                except IndexError:
                    pass

            #print(self.task_list[0])
            # Sleeping until the next task
            try:
                now = datetime.datetime.now().replace(microsecond=0).replace(second=0)
                diff = (task_dates[0] - now).total_seconds()  # Time difference
            except IndexError:
                time.sleep(600) #If there are no on-going tasks for now then sleep for 5 minutes

            if diff-Notifer >= 5:
                time.sleep(diff-Notifer)
                
    def start_notification(self):
        threading.Thread(target= self.push_notifications).start()


    def set_level(self):
        """Determines silver/gold/bronze"""
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        db = TinyDB('usrdb.json')  
        users = Query() 
        unsorted_tasks = db_tasks.search(tasks.username == self.username)
        x = len(unsorted_tasks)
        total_score = 0
        finished_tasks = db_tasks.search((tasks['status'] == "Done") & (tasks.username == self.username))
        number_finished=len(finished_tasks)
        
        ongoing_tasks = db_tasks.search((tasks['status'] == "New") & (tasks.username == self.username))
        number_on_going=len(ongoing_tasks)
        
        now = datetime.datetime.now().replace(microsecond=0)
        use = db.get(users.username == self.username)
        date = use['rdate']
        creation_date = datetime.datetime.strptime(date, '%Y-%m-%d  %H:%M:%S')
        creation_date = creation_date.replace(microsecond=0)
        month_diff = (now.year - creation_date.year) * 12 + (now.month - creation_date.month)

        # Score Calculation
        for i in range(x):
            if unsorted_tasks[i]['status'] == "Done":
                total_score = unsorted_tasks[i]["score"] + total_score
        db.update({"score": total_score}, users.username == self.username)
        try:
            if (number_finished / x) >= 0.5 and (number_finished / x) < 0.7 and (month_diff >= 1):
                db.update({"level": "Bronze"}, users.username == self.username)

            if (number_finished / x) >= 0.7 and (number_finished / x) < 0.8 and (month_diff >= 2):  # Silver Level
                db.update({"level": "Silver"}, users.username == self.username)

            if (number_finished / x) >= 0.8 and (month_diff >= 3):  # Gold Level
                db.update({"level": "Gold"}, users.username == self.username)

            if number_on_going == 0 and number_finished and (month_diff >= 3):  # Gold Level
                db.update({"level": "Gold"}, users.username == self.username)

        except ZeroDivisionError:  # Happens if user has zero tasks
            pass

    def search(self, s_key):
        """Function that does both recommendations and search for tasks."""
        # that can both work as search and recommendation with task name Query send for both you can slice it as you wanna
        db_tasks = TinyDB('taskdb.json')
        tasks = Query()
        task = db_tasks.search(
            tasks.task.matches(s_key + '.*', flags=re.IGNORECASE) & (tasks.username == self.username))

        if task:
            text=task[0]["task"]
            return 1, text
        else:
            return 0, None
        #print(db_tasks.search(where('task').matches(s_key + '.*') & (tasks.username == self.username)))  # case sensitve


#print(Manage("mohamezdrazzk").sort_by_end_date())
