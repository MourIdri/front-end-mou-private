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
#datas = {'CurrentMail': "AA", 'STRUserUUID1': "BB", 'FirstName': "ZZ", 'LastName': "ZZ",  'EE': "RR", 'JobRole': "TT"  }
#writing user infos locally to a session_log directory
tempfolder="sessions_log"
tempjonfilename="%s/%stempuser.json"%(tempfolder,STRUserUUID1)
with open(tempjonfilename, 'w') as outfile:
  json.dump(data, outfile, indent=4)
outfile.close()



#sending user infos to app server using python "requests"

url = "http://10.100.2.6:80/customerupdate"
def send_request():
    #payload = {"param_1": "value_1", "param_2": "value_2"}
    payload = datas
    local_file_to_send = 'user_picture.jpg' 
    files = {
         'json': (None, json.dumps(payload), 'application/json'),
         'file': (os.path.basename(local_file_to_send), open(local_file_to_send, 'rb'), 'application/octet-stream')
    }
    r = requests.post(url, files=files)

send_request()


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Customers Checkout</title>"
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




