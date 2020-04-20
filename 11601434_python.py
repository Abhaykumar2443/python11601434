#!/usr/bin/env python
# coding: utf-8

# CAP776/11601434

# In[30]:


import csv, json
import pandas as pd
import numpy  as np
import matplotlib.pyplot as pt
import requests

json_data_url = requests.get('https://api.covid19india.org/raw_data.json')
json_file = open('D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\rawjson.json','w')
json_file.write(str(json_data_url.text))
json_file.close()

inputFile = open('D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\rawjson.json') 
outputFile = open('D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\covidcsv.csv','w') 
data = json.load(inputFile)
inputFile.close()

# WRITE INTO CSV FILE
output = csv.writer(outputFile)
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
    
#CONVVERT CSV FILE INTO EXCEL
read_file = pd.read_csv (r'D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\covidcsv.csv',encoding="cp1252")
read_file.to_excel (r'D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\covidexcel.xlsx', index = None, header=True)

print('NOVEL COVID 19 DATASET  :')

#READ EXCEL FILE AND SHOWING IT INTO GRAPH VISUALIZATION OUTPUT 
file=pd.read_excel('D:\\MCA LATEST FILES\\CAP776 PROGRAMMING IN PYTHON\\covidexcel.xlsx')
file.fillna("undefined", inplace = True) 

# THERE ARE THE FOLLOWING GRAPHS WITH THE VISUALIZATION OUTPUT :

# 1) PIE CHART

print('VISUALIZATION OF PIE CHART:')

x=0
y=0
z=0
for i in file['typeoftransmission']:

    if(i=='Imported'):x=x+1

    elif(i=='Local'):y=y+1
    elif(i=='TBD'):z=z+1      

print("Imported:",x)
print("Local:",y)
print("TBD :",z)

fig = pt.figure()

ax = fig.add_axes([0,0,1,1])

lab = ['Imported', 'Local','TBD']

coviddata = [x,y,z]

pt.title("COVID_19 DATA")

pt.xlabel("TYPE OF TRANSMISSION")

pt.ylabel("TOTAL PEOPLE")



ax.pie(coviddata, labels = lab,autopct='%1.2f%%')

pt.show()

# LINE GRAPH

print('VISUALIZATION IN LINE GRAPH:')

f=0
m=0
ud=0
for i in file['gender']:
    if(i=='M'):
        m=m+1
    elif(i=='F'):
        f=f+1
    else:
        ud=ud+1
print("MALE:",m)
print("FEMALE:",f)
print("UNDEFINED:",ud)

gender=["MALE","FEMALE","UNDEFINED"]
value=[m,f,ud]
pt.title("COVID_19 DATA")
pt.xlabel("GENDER")
pt.ylabel("TOTAL PEOPLE")
pt.plot(gender,value,color='blue')
pt.show()

# BAR GRAPH
print('VISUALIZATION IN BAR RAPH:')

rec=0
hop=0
dea=0
mig=0
uda=0
for i in file['detecteddistrict']:
    if(i=='Chandigarh'):
        rec=rec+1
    elif(i=='Italians*'):
        hop=hop+1
    elif(i=='Mumbai'):
        dea=dea+1
    elif(i=='Pune'):
        mig=mig+1
    elif(i=='New Delhi'):
        uda=uda+1
print("CHANDIGARH:",rec)
print("ITALIANS*:",hop)
print("MUMBAI:",dea)
print("PUNE:",mig)
print("NEW DELHI:",uda)

pt.title("COVID_19 DATA")
ob=("CHANDIGARH","ITALIANS*","MUMBAI ","PUNE","NEW DELHI")
z=np.arange(len(ob))
val=[rec,hop,dea,mig,uda]
pt.xlabel("Current Status")
pt.ylabel("TOTAL PEOPLE")
toplabel=pt.bar(z,val,color=['yellow', 'pink', 'black', 'red', 'green'])
pt.xticks(z,ob)
for i in toplabel:
    height = i.get_height()
    pt.text(i.get_x() + i.get_width()/2, 1*height,height,ha='center', va='bottom')
pt.show()

