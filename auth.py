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
ccdenum=0

class user_auth:  # user login authintication

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        error = ""
        status = False
        if "@" in self.username:
            data = db.get(self.username == Query()['email'])
        else:
            data = db.get(self.username == Query()['username'])
        if data == None:
            error = "User Or Emal  Not Found"
            return status, error
        elif check_pw_hash(self.password, data.get('password')):
            error = ("Right Password")
            status = True
        else:
            error = "Wrong Password"

        return status, error  # that funcation return error casue and status


    def reset(self):
        if "@" in self.username:
            if db.get(self.username == Query()['email']) is not None:
                mail = db.get(self.username == Query()['email']).get('email')
            else:
                return False , "Mail Not Found"

        else:
            if db.get(self.username == Query()['username']) is not None:
                mail = db.get(self.username == Query()['username']).get('email')
            else:
                return False, "User Not Found"

        global ccdenum
        ccdenum = randint(100000, 999999)
        mail_code(mail, ccdenum)
        return True, "Code had been Sent"


    def code_validaion(self,code):
        mail_reset_code = int(code)
        if mail_reset_code == ccdenum:
            return True
        else:
            return "Wrong Reset Code "

    def reset_handler(self,password):
        new_password = str(password)
        db.update({"password": make_pw_hash(new_password)}, users.username == self.username)
        return True


"""
print(user_auth("mohamedrazzk","").reset())
x=input()
print(user_auth("","").code_validaion(x))
print(user_auth("mohamedrazzk",None).reset_handler("pass@word"))

#print(user_auth("mohamedrazzk", "pass@word").login())
user_auth("mohamedrazzk","").reset()                             //give function just user name 

"""
