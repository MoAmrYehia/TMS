"""
Project :SWE-CSE2020
Created by : Razzk
C-Date : 12/28/2020 , 9:18Pm
Des: this class is used for sending notifcation to windows and linux center
Last-M : Razzk
M-date 10/1/2021 5:32pm
"""

#this calss
import platform
def push_notification(message):
    if platform.system() == "Windows":
        from win10toast import ToastNotifier
        toast = ToastNotifier()
        toast.show_toast("Task Manager ", message, duration=20) #ico can be added later

    else:
        import notify2
        notify2.init('Task Manager')
        n = notify2.Notification("Task Manager ",
                                 message,
                                 "notification-message-im"  # Icon name
                                 )
        n.show()