import urllib.request
import json
import RPi.GPIO as GPIO
import time      
import threading 

# This file is not checked in. It is a simple KEY = VALUE module that contains the
# secret key needed to post data to my adafruit.io feed. It looks like this:
#
# AIO = 'blahblahblah'
#
import credentials # Not checked in ... simple KEY = VALUE module

import adafruit_io

io = adafruit_io.AdafruitIO('topher_cantrell',credentials.AIO)

# Count of pulses over time interval
current_pulse_count = 0

# Thread lock (the button event is asynchronous)
lock = threading.Lock()    

S_PULSE = 4
GPIO.setmode(GPIO.BCM)

def count_pulse(event):
    global current_pulse_count,lock
    with lock:
        current_pulse_count += 1

GPIO.setup(S_PULSE, GPIO.IN)
GPIO.add_event_detect(S_PULSE, GPIO.RISING, callback=count_pulse,bouncetime=100)

while True:        
    time.sleep(10)
    with lock:
        x = current_pulse_count
        current_pulse_count = 0
    #print('Count '+str(x))
    io.add_data_retry('power-monitor',x)
            
        