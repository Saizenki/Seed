#!/usr/bin/python
# Author: Saizenki
# Date: 14.08.2018
import RPi.GPIO as GPIO
from AllPin import Pin

name="Led"

pin_ob=Pin()
pin=pin_ob.number(name)
print(pin)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def LedOn():
	GPIO.output(pin, GPIO.LOW)
	print("Led is On")

LedOn()