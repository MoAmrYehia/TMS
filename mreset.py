"""
Project :SWE-CSE2020
Created by : Razzk
C-Date : 12/8/2020 , 12:15am
Des: hasing passwords
Last-M : Razzk
M-date 12/8/2020 12:27am
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


#mail_code("mohamedrazzk@gmail.com","55555555")