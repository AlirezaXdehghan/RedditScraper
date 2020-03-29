import pandas as pd
import requests
import json
import csv
import os
import time
import datetime

def extractdata(sliceofdata):
    subData = list() #list to store data points
    for i in range (len(sliceofdata)):
        try:
            title = sliceofdata[i]['title']
        except KeyError:
            print(" there is a problem mate :/ \n")
            title=""
        try:
            text = sliceofdata[i]['selftext']
        except KeyError:
            print(" there is a problem mate :/ \n")
            text=""
        try:
            score = sliceofdata[i]['score']
        except KeyError:
            print(" there is a problem mate :/ \n")
            score=""
        try:
            created = pd.to_datetime(sliceofdata[i]['created_utc'], unit='s')
        except KeyError:
            print(" there is a problem mate :/ \n")
            created="0"
        try:
            numComms = sliceofdata[i]['num_comments']
        except KeyError:
            print(" there is a problem mate :/ \n")
            numComms=0
        subData.append((title,text,score,numComms,created))
    return subData


ArrayofData = list()
days = input("please enter the number of days : ")
subredditname = input("please enter the name of subreddit : ")
for i in range (int(days)):
    bday=i
    aday=i+1
    url = 'https://api.pushshift.io/reddit/search/submission/?after='+str(aday)+'d&before='+str(bday)+'d&subreddit='+str(subreddit)+'&sort_type=num_comments&size=100&sort=desc'
    r = requests.get(url)
    data = json.loads(r.text)
    ArrayofData.append(extractdata(data['data']))
    print(i)



while(len(ArrayofData)>1):
    ArrayofData[0].extend(ArrayofData[1])
    ArrayofData.remove(ArrayofData[1])
df = pd.DataFrame(ArrayofData[0],columns=['Title','Text','Score','Comments','Time'])
df = df.sort_values(by=['Time'], ascending=False)
df.to_csv('Data.csv')
