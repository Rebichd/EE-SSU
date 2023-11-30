#!/usr/bin/env python
import RPi.GPIO as GPIO
import http.client, urllib, urllib.parse, urllib.request, requests
import string
import json
from time import sleep

my_api_Key = "****************"
my_talkback_key = "********"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set pin 17 as the output
GPIO.setup(17, GPIO.OUT)

while True:
        baseurl = ('https://api.thingspeak.com/talkbacks/*****/commands/execute.json?api_key=****************')
        contents = json.loads(urllib.request.urlopen(baseurl).read())

        if len(contents) > 0:
                if contents["command_string"] == 'OFF':
                        print ('LED1 OFF')
                        GPIO.output (17, GPIO.LOW)
                elif contents["command_string"] == 'ON':
                        print ('LED1 ON')
                        GPIO.output (17, GPIO.HIGH)
                else:
                        print ('NOT Command')
                sleep(20)
