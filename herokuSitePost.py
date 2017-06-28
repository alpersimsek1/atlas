import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth
import csv

'''
r = requests.get('http://127.0.0.1:8000/emails/api/',auth=HTTPBasicAuth('filika','pikacu330'))
#r = requests.get('http://127.0.0.1:8000/message/api/')

messageList = r.text
json_data = json.loads(messageList)
print(json_data)
'''
path = "C:/openFrameworks/apps/myApps/csvEx/bin/data/mails.csv"
df = pd.read_csv(path, names=['mail','project'])
for i in range(len(df)):
    mail = df.loc[i][0]
    project = df.loc[i][1]
    r = requests.post('https://evening-woodland-75874.herokuapp.com/emails/api/',auth=HTTPBasicAuth('filika','Project1234'), data={"mail": mail, "project":project})
    print(mail + " " + project)
outfile = open(path, 'w')
outfile.write("")
outfile.close()

#r = requests.post('https://evening-woodland-75874.herokuapp.com/emails/api/', data={"mail": "alpersim94gmail.com", "project":"filika"})
