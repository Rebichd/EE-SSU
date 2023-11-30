#!/usr/bin/env python
#Making Web Request

import smtplib

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email server
SMTP_PORT = 587 #Server Port
GMAIL_USERNAME = 'sendingEmail@gmail.com' #Gmail account that I want to send from
GMAIL_PASSWORD = '**** **** **** ****' #code for app usage of Gmail account

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

sender = Emailer()

sendTo = 'recipientEmail@gmail.com' #email address you want to send message to
emailSubject = "Hello World"
emailContent = "This is a test of my Emailer CLass"

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject adn "emailContent" as the email content
sender.sendmail(sendTo, emailSubject, emailContent)

