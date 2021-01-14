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
