#!/usr/bin/env python
#Import porper libraries
import time
import os
import subprocess

#Version 2: 
#Changes:
#	- Changed the timeout loop to correctly enter the if statement based on whether or not there was an IP
#	address seen or not
#	- Added note about the possibility of the need to modify /etc/dhcpcd.conf file depending on how local
#	network is configured

#A program that uploads the IP Address and MAC address to the php website in the "curl" command below
#This script will run on boot up with the use of laucher.sh 
#This script may require the need to set the /etc/resolv.conf file using the command 'sudo nano /etc/dhcpcd.conf' 
#then at the bottom change the "static domain_name_server=8.8.8.8" and make sure to un-comment it which will 
#force the curl command to use Google as the DNS. You can then restart the service 'sudo service dhcpcd restart'

counter = 0
timeLimit = 120

while True:
	#Use linux commands to get line containing active IP Address(skips loopback address using "broadcast grep")
	output_ifconfig = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
	output_grep1 = subprocess.Popen(["grep", "inet"], stdin=output_ifconfig.stdout, stdout=subprocess.PIPE)
	output_grep2 = subprocess.Popen(["grep", "broadcast"], stdin=output_grep1.stdout, stdout=subprocess.PIPE)

	#Use linux commands to get line containing MAC Address
	output_ifconfig2 = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
	output_grep3 = subprocess.Popen(["grep", "ether"], stdin=output_ifconfig2.stdout, stdout=subprocess.PIPE)

	lineIP = str(output_grep2.stdout.readlines())
	lineMAC = str(output_grep3.stdout.readlines())

	if "inet" not in lineIP:
	#if not lineIP:
		counter += 1
		if counter == timeLimit:
			print ("Time Limit Reached...")
			print ("Terminating IP and MAC Finder...")
			break
		time.sleep(1)
	else:
		lineIndex = lineIP.index("inet")
		lineIndex2 = lineIP.index("netmask")
		myIPAddress = lineIP[(lineIndex+4):lineIndex2].strip()

		lineMACIndex = lineMAC.index("ether")
		lineMACIndex2 = lineMAC.index("txque")
		myMACAddress = lineMAC[(lineMACIndex+5):lineMACIndex2].strip()

		os.system("curl https://faridfarahmand.000webhostapp.com/message.php?message="+ myIPAddress +"--" + myMACAddress)
		break

