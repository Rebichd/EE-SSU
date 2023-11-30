#!/usr/bin/env python
import urllib, urllib.parse, time, http.client
from random import randint
import random

apikey = "****************"

while True:
        myRandom1 = randint(0,100)
        myRandom2 = random.random()
        print (myRandom1, myRandom2)
        #define three fileds for ThinkSpeak
        params = urllib.parse.urlencode({'field1': myRandom1, 'field2': myRandom2, 'field3': 20, 'key': apikey})
        headers = {"Cotent-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        time.sleep(20)
