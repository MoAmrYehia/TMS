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
    return hashlib.sha256(str.encode(passwod)).hexdigest()  # returning hashed password for validating


def check_pw_hash(password, hash):  # hashing function
    if make_pw_hash(password) == hash:
        return True
    return False
