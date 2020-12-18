import notify2
notify2.init('Task Manager')

def push_notification(message):

    n = notify2.Notification("SWE CSE Task Manager ",
                             message,
                             "notification-message-im"   # Icon name
                            )
    n.show()

push_notification("You have task now ")