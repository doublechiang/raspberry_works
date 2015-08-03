#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os

# initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pin setting
powerled=4
powerbutton = 18
volumeup=14
volumedown=15

GPIO.setup(powerled, GPIO.OUT)
GPIO.setup(powerbutton, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(volumeup, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(volumedown, GPIO.IN, GPIO.PUD_UP)

powercnt=0

# light it up
GPIO.output(powerled, 1)

while True:
    if GPIO.input(powerbutton) ==False:
        # power butten pressed
        print "power button down!"
        powercnt +=1
    else:
        print "power button up!"
        powercnt = 0

    if (powercnt >3):
        print "Power button pressed for over 3 seconds, shutdown now!"
        # os.system("init 0")
    time.sleep(1)
    print "sleep 1 second"
    

#clean it up
GPIO.cleanup()
