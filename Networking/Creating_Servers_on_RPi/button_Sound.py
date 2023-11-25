#!/usr/bin/env python
#Import proper libraries
import RPi.GPIO as GPIO
import time
import os

#Use BCM pin numbering scheem
GPIO.setmode(GPIO.BCM)

#Set pin 17 as the input
GPIO.setup(17, GPIO.IN)

while True:
        if(GPIO.input(17)):
                print("Button Pressed")
                #delay of one second
                time.sleep(1)
                #plays the audio .wav file
                os.system("aplay police_s.wav")
                #traps user in loop while button is pressed
                while GPIO.input(17):
                        time.sleep(1)
                #displayed upon button release
                if(not GPIO.input(17)):
                        print("Button Released")
                        time.sleep(1)
