import time

def time_call():
    current_time = time.time()

    days_since_epoch = int(current_time // 86400)
    remaining_sec = current_time % 86400

    hours = int(remaining_sec // 3600)
    remaining_sec = remaining_sec % 3600

    minutes = int(remaining_sec // 60)
    seconds = int(remaining_sec % 60)

#The number of days since the epoch.
    print("The number of days since epoch is:", days_since_epoch)

#Reads the current time and converts it to a time of day in hours, minutes, and seconds, 
    print("Current time of day (GMT+0) is:", f"{hours:02d}:{minutes:02d}:{seconds:02d}")

time_call()