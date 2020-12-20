import time
import threading


def T_print():

    [tasks, sleep_time] = 10, 1
    while tasks != 0:
        print(tasks, sleep_time)
        sleep_time, tasks = sleep_time+1, tasks-1
        time.sleep(sleep_time)
    return


notification = threading.Thread(target=T_print)
notification.start()