
"""
Project :SWE-CSE2020
Created by : Razzk
C-Date : 12/7/2020 , 11:14Pm
Des: main funcation for user modifing and validation
Last-M : Razzk
M-date 12/8/2020 01:25pm
"""


from data_rw import user
from tinydb import TinyDB, Query
from sechashuli import make_pw_hash, check_pw_hash
from random import randint
from mreset import mail_code

db = TinyDB('usrdb.json')
users = Query()


class user_auth:                    #user login authintication

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        error = ""
        status=False
        data = db.get(self.username == Query()['username'])
        if data == None:
            error = "User Not Found"
        elif check_pw_hash(self.password, data.get('password')):
            error=("Right Password")
            status = True
        else:
            error = "Wrong Password"

        return status, error                                                 #that funcation return error casue and status

    def reset(self):
        data = db.get(self.username == Query()['username'])
        mail = data.get('email')
        reset_code = randint(100000, 999999)
        mail_code(mail, reset_code)
        mail_reset_code = int(input())

        if mail_reset_code == reset_code:
            new_password=str(input("please Enter new Password\n"))
            db.update({"password": make_pw_hash(new_password)}, users.username == self.username)
            print("password had changed ")
        else:
            print("worng mail Code")



"""
#print(user_auth("mohamedrazzk", "pass@word").login())
user_auth("mohamedrazzk","").reset()                             //give function just user name 

"""