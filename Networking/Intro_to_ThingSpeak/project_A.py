#!/usr/bin/env python
#Import porper libraries
import time
import os
import subprocess
import smtplib

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'senderEmail@gmail.com' #Gmail account that I want to send from
GMAIL_PASSWORD = '**** **** **** ****' #Password for this email account

#Class that is used to send email using the credential from above
class Emailer:
        def sendmail(self, recipient, subject, content):

                #Creat Headers
                headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
                headers = "\r\n".join(headers)

                #Connecnt to Gmail Server
                session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                session.ehlo()
                session.starttls()
                session.ehlo()

                #Login to Gmail
                session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

                #Send Email & Exit
                session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
                session.quit


#Use linux commands to get cpu temp
output_cpuTemp = subprocess.Popen(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE)
cpuTemp = str(output_cpuTemp.stdout.readlines())

#Parse string to extract just the temp value
eqIndex = cpuTemp.index("=")
unitIndex = cpuTemp.index("'")
cpuTempParsed = cpuTemp[(eqIndex+1):(unitIndex)].strip()

print (cpuTempParsed) #Prints out the CPU temp to the terminal

cpuTempNum = float(cpuTempParsed) #Turn temp string into float

#Check if temp is higher than 40'C, if it is send an email
if cpuTempNum > 40:
        #Create an instance of the Emailer variable class
        sender = Emailer()

        sendTo = 'recipientEmail@gmail.com' #Email address that the email will be sent to
        emailSubject = "CPU TEMP WARNING!!!!" #Subject title of the email to be sent
        emailContent = "The CPU Temp is at: " + cpuTempParsed + "'C"
        #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject adn "emailContent" as the email content
        sender.sendmail(sendTo, emailSubject, emailContent)
