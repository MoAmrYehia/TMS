"""
Project :SWE-CSE2020
Created by : Razzk
C-Date : 12/8/2020 , 12:15am
Des: this class is main used for mail server to send recovery code to user
Last-M : Razzk
M-date 01/10/2021 5:26am
"""

import smtplib
def mail_code(mail, code):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login("recovery.swcse2020@gmail.com", "asd$#@asdfas788")
        message = 'Subject: {}\n\n Your Recovery Code is : {}'.format("SW_CSE-ReocveryCode", code)
        server.sendmail("recovery.swcse2020@gmail.com", mail, message)
        server.quit()
        print("Code had been sent")
    except:
        print("Email Faild to send ")
