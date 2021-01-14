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
