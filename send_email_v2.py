#! /bin/python

import os
import sys
import smtplib
import string
import socket
import getpass

mesaj_alerta = "ok"

def send_email(mesaj):
    SMSBody=mesaj
    SUBJECT = "Alerta docker web2sms"
    #TO = "name.surname@domain.com";"name.surname@gmail.com"
    TO = "name.surname@domain.com"
    HOSTUSER = getpass.getuser()
    HOSTNAME = socket.gethostname()
    FROM = HOSTUSER + "@" + HOSTNAME
    text = " \r\n" + SMSBody
    HOST = "localhost"
    BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
    try:
        server = smtplib.SMTP(HOST)
        server.sendmail(FROM, [TO], BODY)
        server.quit()
    except SMTPException:
        print "Error: unable to send email"


send_email(mesaj_alerta)
