# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:51:41 2018

@author: user
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
d = {}
l=[]
#input data
for i in range(0,2):
    name = input("Name")
    age = int(input("age : "))
    weight = int(input("Weight : "))
    height = int(input("Height : "))
    gender = input("Gender : ")
    
    d = {'name':name,'age':age,'height':height,'weight':weight,'gender':gender}
    l.append(d)

df = pd.DataFrame(l)

#Save data to file
writer = ExcelWriter('Student-data.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

#Retrieve data
df = pd.read_excel("Student-data.xlsx")

#Sort based on height

print(df.sort_values(['height']))

#Caluclate BMI
df['bmi'] = df['weight']/df['height']**2
print(df)

#grouping bmi
df_group = df.groupby(['bmi']).mean()
print(df_group)


#grouping weights
df.ix[(df.weight >= 80) & (df.weight < 100) , 'weightGrp'] = 'OverWeight'
df.ix[(df.weight >= 100) , 'weightGrp'] = 'Obese'
df.ix[(df.weight >= 50) & (df.weight < 80) , 'weightGrp'] = 'Healthy'
df.ix[(df.weight < 50) , 'weightGrp'] = 'Under Weight'

print(df)




