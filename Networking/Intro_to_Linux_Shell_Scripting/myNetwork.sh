#!/bin/bash
#Author: Daniel Rebich
#Sept. 14, 2023 - Version 1
#--------------------------

#IP
ifconfig | grep broadcast > temp1.txt
echo -n "IP Address: " > myNetwork.txt | cut -f10 -d" " temp1.txt >> myNetwork.txt

#MAC
ifconfig | grep -m1 ether > temp1.txt
echo -n "MAC Address: " >> myNetwork.txt | cut -f10 -d" " temp1.txt >> myNetwork.txt

#Hostname
echo -n "Hostname: " >> myNetwork.txt | hostname >> myNetwork.txt

#Username
echo -n "Username: " >> myNetwork.txt | whoami >> myNetwork.txt

#OS
echo -n "OS: " >> myNetwork.txt | uname -o >> myNetwork.txt

#Distribution
cat /etc/os-release | grep PRETTY > temp1.txt
echo -n "Distribution: " >> myNetwork.txt | cut -d'"' -f2 temp1.txt >> myNetwork.txt

#delete temp files
rm temp1.txt
