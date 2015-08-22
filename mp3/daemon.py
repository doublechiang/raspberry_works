#!/usr/bin/env python

# Reference:
# callback button event refer to http://makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/
# Python dbus control play back.

# Todo
# 2. initialize music list, press power button to start/stop replay music
# 3. volume up/down control


import RPi.GPIO as GPIO
import time
import os
import logging

logging.basicConfig(level=logging.INFO)

# initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pin setting
powerled=4
powerbutton = 18
volumeup=14
volumedown=15

GPIO.setup(powerled, GPIO.OUT)
GPIO.setup(powerbutton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(volumeup, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(volumedown, GPIO.IN, GPIO.PUD_UP)

powercnt=0
powerDownTime=0.0

# light it up
GPIO.output(powerled, 1)

# callback function for volumn down
def volDown(channel):
    pass
    print "VolDown"

def volUp(channel):
    pass
    print "VolUp"


def start_stop():
    print "start/stop action"
    pass



def powerButtonEvent(channel):
    global powerDownTime
    if GPIO.input(powerbutton) == False:
        powerDownTime = time.time()
    else:
        pressTime = time.time() - powerDownTime
        print "Power button down time %f" % (time.time() - powerDownTime)
        if pressTime > 3.0 :
            print "PowerDown"
            os.system("init 0")
        else:
            start_stop
        
    pass


# detect RISING  

GPIO.add_event_detect(powerbutton, GPIO.BOTH, callback=powerButtonEvent)
GPIO.add_event_detect(volumeup, GPIO.RISING, callback=volUp)
GPIO.add_event_detect(volumedown, GPIO.RISING, callback=volDown)
while True:
    time.sleep(1)

    

#clean it up
GPIO.cleanup()
