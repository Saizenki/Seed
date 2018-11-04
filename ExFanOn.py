#!/usr/bin/python
# Author: Saizenki
# Date: 14.08.2018
import RPi.GPIO as GPIO
from AllPin import Pin 

pin_ob=Pin()
pin=pin_ob.number("ExFan")
print(pin)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def FanOn():
	GPIO.output(pin, GPIO.LOW)
	print("Exhaust Fan On")
	
FanOn()