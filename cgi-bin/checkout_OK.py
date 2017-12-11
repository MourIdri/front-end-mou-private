#!/usr/bin/python




# Import modules for CGI handling 
import cgi, cgitb 

import sys
import os
import sys
import logging
import time
import datetime
import json 
import uuid
import requests


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

#debug enabled
cgitb.enable()

# Get data from fields
FirstName = form.getvalue('FirstName')
LastName  = form.getvalue('LastName')
CurrentCompany  = form.getvalue('CurrentCompany')
JobRole = form.getvalue('JobRole')
CurrentMail = form.getvalue('CurrentMail')

# Generate random string for User UUID
ConnexionUserUUID1 = uuid.uuid1()
STRUserUUID1=str(ConnexionUserUUID1)

#writing to json file
data = {u"imgPath":"../IMAGES/",
	u"GargbagePath":"../IMAGEBIN/",
	u"ImagesToS3":"../IMAGESTOS3/",
	u"CurrentMail":CurrentMail,
	u"STRUserUUID1": STRUserUUID1,
	u"User":{u"FirstName": FirstName, u"LastName": LastName, }, 
	u"UserInfos": {u"CurrentCompany": CurrentCompany, u"JobRole": JobRole }
	}
datas = {'CurrentMail': CurrentMail, 'STRUserUUID1': STRUserUUID1, 'FirstName': FirstName, 'LastName': LastName,  'CurrentCompany': CurrentCompany, 'JobRole': JobRole  }

tempfolder="sessions_log"
tempjonfilename="%s/%stempuser.json"%(tempfolder,STRUserUUID1)
with open(tempjonfilename, 'w') as outfile:
  json.dump(data, outfile, indent=4)
outfile.close()

# Posting data using Python's requests to Backen App Server
url = "http://10.100.2.6:80/customerupdate"
#url = "http://10.100.2.4:80/customerupdate"
#datas = {"cardno":"6248889874650987","systemIdentify":"s08","sourceChannel": 12}
headers = {'Content-type': 'application/json'}
rsp = requests.post(url, json=datas, headers=headers)

#url = "http://10.100.2.5:80/customerupdate"
#headers = {'Content-type': 'application/json'}
#rsp = requests.post(url, json=datas, headers=headers)

#httpequiv="refresh" 
#content="5; url =http://google.com/"
#content="1; url =http://google.com/"
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Customers Checkout</title>"
#print ("<meta http-equiv="refresh" content="1; url=http://example.com/"/>")
#print "<meta http-equiv=%s content=%s/>" %(httpequiv,content)
print "</head>"
print "<body>"
print ""
print "<p>your data is written. </p>" 
print ""
print ""
print "<p> </p>"
print ("<div id='button'><a href='/index.php'> BACK ...</a></div>")

print "</body>"
print "</html>"




