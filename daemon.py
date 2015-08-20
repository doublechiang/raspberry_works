#!/usr/bin/env python

# Todo
# 1. event callback
# 2. initialize music list, press power button to start/stop replay music
# 3. volume up/down control


import RPi.GPIO as GPIO
import time
import os
import logging

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

# light it up
GPIO.output(powerled, 1)

while True:
    if GPIO.input(powerbutton) ==False:
        # power butten pressed
        logging.debug("power button down!")
        powercnt +=1
    else:
        logging.debug ("power button up!")
        powercnt = 0

    if (powercnt >3):
        logging.debug( "Power button pressed for over 3 seconds, shutdown now!")
        os.system("init 0")
    time.sleep(1)
    

#clean it up
GPIO.cleanup()
