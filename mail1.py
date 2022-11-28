import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests 
import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=project-ruchita-8f71077b7512 (1)'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
mail_content = 'Hi,Please help me urgently... \n Here I attached mylocation: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)
#The mail addresses and password
sender_address = 'projectandroidengg@gmail.com'
sender_pass = '9689544204'
receiver_address = 'shubhangi.sctcode@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Women Security. Emergency HELP!!!!.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 25) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')