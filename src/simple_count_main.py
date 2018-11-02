import RPi.GPIO as GPIO
import time

S_PULSE = 4
GPIO.setmode(GPIO.BCM)

def count_pulse(event):
    print("Pulse")

GPIO.setup(S_PULSE, GPIO.IN)
GPIO.add_event_detect(S_PULSE, GPIO.RISING, callback=count_pulse,bouncetime=100)

while True:
    time.sleep(10)