# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:50:36 2018

@author: user
"""
import pandas as pd
d = {}
l=[]

for i in range(0,2):
    name = input("Name")
    score = int(input("Score : "))
    num_attempts = int(input("Number of Attempts : "))
    qualified = input("Qualified : ")
    
    d = {'name':name,'score':score,'num_attempts':num_attempts,'qual':qualified}
    l.append(d)

df = pd.DataFrame(l)

#Name and Qual
print(df.iloc[:,[0,2]])

#First 4 rows
print(df.iloc[0:4,:])

count =0
#number of scrore between 25-30

score = df['score']

for i in range(len(score)):
    if(score[i]>25 and score[i]<30):
        count = count+1
        
print(count)

    

    