"""
Project :SWE-CSE2020
Created by : Razzk
C-Date : 12/7/2020 , 7:15Pm
Des: hasing passwords
Last-M : Razzk
M-date 12/7/2020 10:50pm
"""

import hashlib

def make_pw_hash(passwod):
    return hashlib.sha256(str.encode(passwod)).hexdigest()        #returning hashed password for validating


def check_pw_hash(password,hash):                                 #hashchiching funcatio
     if make_pw_hash(password) == hash:
         return True
     return False



#print(make_pw_hash("pass@word"))
#print(check_pw_hash("pass@word","a0f4f5e99ec8ca18b26b2f9c64d35194ee497a95b907614aadb2c90b93d88626"))