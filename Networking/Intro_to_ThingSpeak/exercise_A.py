#!/usr/bin/env python
#Import proper libraries
import urllib, urllib.parse, time, http.client
from random import randint
import random
import time
import os
import subprocess
import psutil #this is for the cpu usage

apikey = "****************" #API key from ThinkSpeak

while True:
        #Use linux commands to get cpu temp
        output_cpuTemp = subprocess.Popen(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE)
        cpuTemp = str(output_cpuTemp.stdout.readlines())

        #Parse string to extract just the temp value
        eqIndex = cpuTemp.index("=")
        unitIndex = cpuTemp.index("'")
        cpuTempParsed = cpuTemp[(eqIndex+1):(unitIndex)].strip()
        print (cpuTempParsed) #Prints out the CPU temp to the terminal
        cpuTempNum = float(cpuTempParsed) #Turn temp string into float

        cpu_usage = psutil.cpu_percent(interval=1)
        print (cpu_usage) #Prints out the CPU usage to the terminal

        params = urllib.parse.urlencode({'field1': cpuTempNum, 'field2': cpu_usage, 'key': apikey})
        headers = {"Cotent-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        time.sleep(20)
