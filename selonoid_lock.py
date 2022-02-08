from flask import Flask, render_template, request, redirect, url_for, make_response
import time
import RPi.GPIO as GPIO
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setuprelay(GPIO.OUT)
relay = 18;
GPIO.output(relay , 0)

#recieve which pin to change from the button press on selonoid.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors

def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 1:
        print "ON"
                GPIO.output( relay , 1)                
    elif changePin == 0:
        print "OFF"
                GPIO.output(relay, 0)
    
