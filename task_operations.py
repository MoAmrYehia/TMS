# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:47:41 2020

@author: dinaa
"""
from push_notification_sc import push_notification
import datetime
import threading
import time
from tinydb import TinyDB, Query, where
import re
import regex
import platform


Notifer=30
db_tasks = TinyDB('taskdb.json')
tasks = Query()
db_scoring = TinyDB('scoringdb.json')
scores = Query()
db = TinyDB('usrdb.json')  # defind database location as json file
users = Query()  # implementing data as user query


class Manage():
    """Class that manages operations on the user's tasks"""

    def __init__(self, username):
        self.username = username

    def show_tasks(self):
        """Shows the user's tasks."""
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
                                  })
        return task_list

    def sort_by_name(self):
        """Sorts the user's tasks alphabetically."""
        unsorted_tasks = db_tasks.search(tasks.username == self.username)
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
                                  })
        return task_list

    def sort_by_end_date(self):
        """Sorts the user's tasks based on end-date"""
        unsorted_tasks = db_tasks.search(tasks.username == self.username)
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
                                  })
        return task_list
    
    def show_ongoing_tasks(self):
        """Shows on-going tasks."""
        self.ongoing_list = []  # List of on-going tasks
        self.on_going_tasks = db_tasks.search((tasks['status'] == "On-going") & (tasks.username == self.username))
        self.number_on_going = len(self.on_going_tasks)

        for i in self.on_going_tasks:
            self.ongoing_list.append(i["task"])
        if self.ongoing_list:
            return self.ongoing_list
        else:
            return 0  # Means that no tasks are no on-going tasks

    def show_finished_tasks(self):
        """Shows finished tasks."""
        self.finished_list = []  # List of finished tasks
        self.finished_tasks = db_tasks.search((tasks.status == "Finished") & (tasks.username == self.username))
        self.number_finished = len(self.finished_tasks)

        for i in self.finished_tasks:
            self.finished_list.append(i["task"])

        if self.finished_list:
            return self.finished_list
        else:
            return 0  # Means that no tasks are finished

    def show_weekly_report(self):
        """Produces a weekly report every Friday that shows (un)/finished tasks."""
        self.unsorted_tasks = db_tasks.search(tasks.username == self.username)
        self.total_score = 0  # Total score of the week
        self.today = datetime.datetime.today().replace(second=0, minute=0, hour=0, microsecond=0)  # Return today's date

        self.finished_before_deadline = []
        self.not_finished_before_deadline = []

        # Getting all days of the current week to see which tasks have been finished on this week

        self.day_1 = self.today - datetime.timedelta(days=1)
        self.day_2 = self.today - datetime.timedelta(days=2)
        self.day_3 = self.today - datetime.timedelta(days=3)
        self.day_4 = self.today - datetime.timedelta(days=4)
        self.day_5 = self.today - datetime.timedelta(days=5)
        self.day_6 = self.today - datetime.timedelta(days=6)

        if self.today.weekday() == 4:  # 4 means Friday
            print("Saturday")
            for i in range(0, self.x):

                # Making sure all end_dates are datetime objects not str
                try:
                    self.unsorted_tasks[i]['end_date'] = datetime.datetime.strptime(self.unsorted_tasks[i]['end_date'],
                                                                                    '%d/%m/%Y %H:%M')
                    (self.unsorted_tasks[i]["end_date"]) = (self.unsorted_tasks[i]["end_date"]).replace(second=0,
                                                                                                        minute=0,
                                                                                                        hour=0,
                                                                                                        microsecond=0)
                except:
                    pass

                # Finding out which tasks were finished this week and which weren't
                if (self.unsorted_tasks[i][
                    'end_date']) == self.today or self.day_1 or self.day_2 or self.day_2 or self.day_3 or self.day_4 or self.day_5 or self.day_6:

                    if self.unsorted_tasks[i]['status'] == "Finished":
                        self.finished_before_deadline.append(self.unsorted_tasks[i]["task"])
                        self.total_score = self.unsorted_tasks[i]["score"] + self.total_score

                    if self.unsorted_tasks[i]['status'] == "On-going":
                        self.not_finished_before_deadline.append(self.unsorted_tasks[i]["task"])

        return self.finished_before_deadline, self.not_finished_before_deadline, self.total_score
        # Returns list of finished tasks, list of not finished tasks & total score of the week

    def push_notifications(self):
        """Pushes a notification at the task's end date."""
        self.task_list = []  # List that will contain the tasks ordered

        # Getting the On-going tasks only and excluding the finished tasks

        self.on_going_tasks = db_tasks.search((tasks['status'] == "On-going") & (tasks.username == self.username))
        self.on_going_tasks.sort(key=lambda x: datetime.datetime.strptime(x['end_date'], '%d/%m/%Y %H:%M'))
        self.number_on_going = len(self.on_going_tasks)


        # Making sure that all end_dates are in datetime format not str

        for i in range(0, self.number_on_going):  # number_on_going is the no. of on-going tasks
            try:
                self.on_going_tasks[i]['end_date'] = datetime.datetime.strptime(self.on_going_tasks[i]['end_date'],
                                                                                '%d/%m/%Y %H:%M')
            except:
                pass
            self.task_list.append(self.on_going_tasks[i]['end_date'])  # Adding the tasks to the list


        # Measuring the time now and calculating the difference between it and the end_date of the task
        while self.task_list:

            self.now = datetime.datetime.now().replace(microsecond=0).replace(second=0)

            self.diff = (self.task_list[0] - self.now).total_seconds()  # Time difference in seconds


            if int(self.diff) <= Notifer:  # Print the notification is the time difference is Notifer seconds or less assuming that will be variable
                #print( self.task_list[0])  # Task notification
                self.task_list.remove(self.task_list[0])  # Removing the task from the list after notification's done
                push_notification(self.on_going_tasks[0]['task'])

            print(self.task_list[0])
            # Sleeping until the next task
            self.now = datetime.datetime.now().replace(microsecond=0).replace(second=0)
            self.diff = (self.task_list[0] - self.now).total_seconds()  # Time difference

            if self.diff-Notifer >= 5:
                time.sleep(self.diff-Notifer)


    def set_level(self):
        """Determines silver/gold/bronze"""
        self.total_score = 0
        self.now = datetime.datetime.now().replace(microsecond=0)
        self.use = db.get(users.username == self.username)
        self.date = self.use['rdate']
        self.creation_date = datetime.datetime.strptime(self.date, '%Y-%m-%d  %H:%M:%S')
        self.creation_date = self.creation_date.replace(microsecond=0)
        self.month_diff = (self.now.year - self.creation_date.year) * 12 + (self.now.month - self.creation_date.month)

        # Score Calculation
        for i in range(self.x):
            if self.unsorted_tasks[i]['status'] == "Finished":
                self.total_score = self.unsorted_tasks[i]["score"] + self.total_score
        db.update({"score": self.total_score}, users.username == self.username)
        try:
            if (self.number_finished / self.x) >= 0.5 and (self.number_finished / self.x) < 0.7 and (
                    self.month_diff >= 1):
                db.update({"level": "Bronze"}, users.username == self.username)

            if (self.number_finished / self.x) >= 0.7 and (self.number_finished / self.x) < 0.8 and (
                    self.month_diff >= 2):  # Silver Level
                db.update({"level": "Silver"}, users.username == self.username)

            if (self.number_finished / self.x) >= 0.8 and (self.month_diff >= 3):  # Gold Level
                db.update({"level": "Gold"}, users.username == self.username)

            if self.number_on_going == 0 and self.number_finished and (self.month_diff >= 3):  # Gold Level
                db.update({"level": "Gold"}, users.username == self.username)


        except ZeroDivisionError:  # Happens if user has zero tasks
            pass

    def search(self, s_key):
        """Function that does both recommendations and search for tasks."""
        # that can both work as search and recommendation with task name Query send for both you can slice it as you wanna
        return db_tasks.search(
            tasks.task.matches(s_key + '.*', flags=re.IGNORECASE) & (tasks.username == self.username))
        #print(db_tasks.search(where('task').matches(s_key + '.*') & (tasks.username == self.username)))  # case sensitve


#print(Manage("mohamezdrazzk").sort_by_end_date())

# Running a thread
# th = threading.Thread(target = manage_razzk.push_notifications()).start()
#manage_razzk.push_notifications()
threading.Thread(target=Manage("mohamezdrazzk").push_notifications()).start()


