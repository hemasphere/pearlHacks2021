#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('healthData.csv')
new_data = df[df['Start Date'] == '20-February-2021']
new_data.to_csv(r'/Users/karishmamuni/newHealthData.csv')


# In[2]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = '1helloworld1User@gmail.com'
email_password = 'HelloWorld11!'
email_send = '2goodbyeworld2User@gmail.com'

subject = "Patient Hello World's Health Data"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi, Here is the health data for today!'
msg.attach(MIMEText(body,'plain'))

filename='newHealthData.csv'
attachment=open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()


# In[3]:


import csv
from twilio.rest import Client
from environmentVariables import phone_num1
account_sid = "AC81f00617bd2f6151da4e912d9bb3f732"
auth_token = "8ba9b1a708b25c3ee07c4ff1f41ad8e3"

with open('newHealthData.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

client = Client(account_sid, auth_token)
# steps
if int(data[-1][-1]) <= 20 and int(data[-1][-2]) > 100:
    client.messages.create(from_= "+18623439653",
                       to=phone_num1,
                       body='This is an abnormal heart rate at resting state.')


# In[ ]:





# In[ ]:




