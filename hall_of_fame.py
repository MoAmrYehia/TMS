# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 07:26:52 2020

@author: dinaa
"""
from tinydb import TinyDB, Query 

db_scoring = TinyDB('scoringdb.json')
scores = Query()

class Hall_of_Fame():
    """Class that determines the top 10 users."""
    def __init__(self):
        self.score = 0
        self.gold_users = db_scoring.search(scores.level== "Gold") #A top 10 user must be Gold

        self.gold_users.sort(key=lambda x: x['Score'], reverse = True) #Sorting the users based on scores
        self.first_ten = list(self.gold_users)[:10] #Returning 10 users with highest scores

        
        if self.first_ten:
            print("The top users are: ")
            for i in range(len(self.first_ten)):
                print(self.first_ten[i]["username"], "  ", self.first_ten[i]["Score"])



h = Hall_of_Fame()