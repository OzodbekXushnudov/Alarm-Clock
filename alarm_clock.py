# Ozod Xushnudov
# 11/08/2023
# Alarm Clock with Python

"""
An alarm clock is a clock with a function that can be activated to ring a t atime set in advance

"""

from datetime import datetime
from playsound import playsound
alarm_time = input("Enter the time that you want ot be set: HH:MM:SS\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm ... ")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')

    if(alarm_hour == current_hour):
        if(alarm_minute == current_minute):
            if(alarm_seconds == current_second):
                print("Wake up")
                playsound('ring.wav')
                break
