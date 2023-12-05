#!/usr/bin/env python
#Import porper libraries
import time
import os
import sys
import subprocess
from influxdb import InfluxDBClient # for the local DataBase

my_Client = InfluxDBClient(host = 'localhost', port = 8086) #this is a call back to the device that the database and python is written on
my_Client.create_database('packet_monitor')
#print (my_Client.get_list_database()) #prints out a list of all databases on this machine
my_Client.switch_database('packet_monitor') #name of the database

#Ask user for ping watch time
watchTime = str(input("Enter amount of time in seconds for PACKET watch: "))
timer = int(watchTime) #added for counter break
watchTime = "duration:" + str(watchTime)
IPtoWatch = "host 192.168.1.140"   #192.168.1.118" #this is for the phone

print ("Starting Packet Watch...")

output = subprocess.Popen(['sudo', 'tshark', '-l', '-i', 'wlan0', '-f', IPtoWatch, '-T', 'fields', '-e', 'frame.len', '-e', 'frame.protocols', '-a', watchTime]>

#Loop to continue while still reading output from tshrak command above
i = 0
while True:
        if str(output.stdout.readline()):
                if output.stdout.readline() == b'':
                        print (".")#does nothing
                else:
                        OrgString = str(output.stdout.readline()) #gets the original string to parse
                        splitString = OrgString.split('\\')
                        #Get the packet size out
                        packetSize = splitString[0][splitString[0].index('\'')+1:]
                        print (packetSize)

                        if len(splitString) > 1:
                                packetType = splitString[1]
                                print (packetType)

                                json_body = [ #if no tiem is included it will just put a timestamp onto it
                                        {
                                                "measurement": "Packet_Data", #name of the measurements
                                                "fields":{      #name of the different fields
                                                        "Packet_type": packetType,
                                                        "Packet_size": int(packetSize)
                                                }
                                        }
                                ]

                                my_Client.write_points(json_body)

        if (i) > int(timer):
                break
        i += 1

time.sleep(1)

print ("Times Up...Terminating PACKET Watch...")

deleteResponse = str(input("Would you like to delete all data in the database? [y/n]:"))

if deleteResponse == "y":
        my_Client.drop_database('packet_monitor')
