#thermostat.py
#controlls the exhaust fan, turns it on when temperature is over the target temperature

import RPi.GPIO as GPIO
from logData import logData
from saveGlobals import setVariable
import variable
from AllPin import Pin
pin_ob=Pin()
pin=pin_ob.number("ExFan")

def adjustThermostat(temp):
    "Turn the fan on or off in relationship to target temperature"
    print ("Adjust Thermostat %s" %str(temp))

    _fanPin = pin #take from Allpin
    currentFanOn = True
    _priorFanOn = "priorFanOn"
    _targetTemp = "targetTemp"
    priorFanOn = variable.env['priorFanOn']
    targetTemp = variable.env['targetTemp']
    print("Target Temp %s" %targetTemp)
    print("Current Temp: %s" %temp)
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
#avoid switching pin state and messing up condition    
#    GPIO.setup(fanPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#    fanOn = GPIO.input(fanPin)
    
    if temp > targetTemp:
        GPIO.setup(_fanPin, GPIO.OUT)
        GPIO.output(_fanPin, GPIO.LOW)
        print("Fan On")
    else:
        GPIO.setup(_fanPin, GPIO.OUT)
        GPIO.output(_fanPin, GPIO.HIGH)
        GPIO.cleanup()    
        currentFanOn = False
        print("Fan Off")

#separate reporting logic for issues during restart where flag not match reality
    print ("CurrentFanOn: " + str(currentFanOn))
    print ("PriorFanOn: " + str(priorFanOn))
    if currentFanOn != priorFanOn:
        print ("Fans not equal")
        if currentFanOn:
            logData("Exhaust Fan", "Success", "state", "On", "Current Temp: " + str(temp))
            print("Fan state - On")
        else:
            logData("Exhaust Fan", "Success", "state", "Off", "Current Temp: " + str(temp))
            print ("Fan state - Off")
# Save out changed fan state
        tmp=variable.env
        tmp[_priorFanOn]=currentFanOn
        setVariable('priorFanOn', currentFanOn)
