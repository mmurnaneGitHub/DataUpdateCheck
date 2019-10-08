# Send Email if RPZ Vote Data has changed on AGO
# Script Last Updated: 2019-4-10
# Author: mmurnane
# Works in 3.6.6
# https://www.tutorialspoint.com/python3/python_sending_email.htm

import urllib.request
import json  
import time
from datetime import datetime, timedelta

import smtplib

sender = 'mmurnane@cityoftacoma.org'
receivers = ['mmurnane@cityoftacoma.org, RPP@cityoftacoma.org']

message = """From: Mike Murnane <mmurnane@cityoftacoma.org>
To: RPP@cityoftacoma.org <RPP@cityoftacoma.org>
Subject: RPZ Vote Was Updated Last 24 Hours
"""

# Feature layer url - RPZ Vote Data 
fsURL = "https://services3.arcgis.com/SCwJH1pD8WSn5T5y/ArcGIS/rest/services/Vote_RPZ/FeatureServer/0?f=pjson"  

# Request the json data for the feature layer 
jsonResponse = urllib.request.urlopen(fsURL)

# Extract the data required - lastEditDate value in editingInfo section of json response  
jsonOutput = json.loads(jsonResponse.read())[u'editingInfo']  
  
# Compare dates  
editTime = int(jsonOutput['lastEditDate'])/1000
print("Current Time: " + time.strftime('%c'))
print("Data Last Edited: " + time.strftime('%c', time.localtime(editTime)))
message+= "Current Time: " + time.strftime('%c')
message+= "\nData Last Edited: " + time.strftime('%c', time.localtime(editTime)) + "\n"

a = editTime #last edit in epoch recorded time
b = time.time() #current epoch time
#print(a)
#print(b)
c = b - a #returns seconds
#days = c // 86400
#hours = c // 3600 % 24
hours = int(c // 3600 % 24)
minutes = int(c // 60 % 60)
seconds = c % 60
print ("Data changed " + str(hours) + " hours and " + str(minutes) + " minutes ago.")

if hours < 24:
    message+= "\n"
    message+= "Data changed " + str(hours) + " hours and " + str(minutes) + " minutes ago."
    try:
        smtpObj = smtplib.SMTP('smtp001.tacoma.lcl')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")

