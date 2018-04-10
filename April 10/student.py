# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:47:52 2018

@author: user
"""

import numpy as np

t= {}
l1 = []

for i in range(0,4):
    name = input("Name : ")
    sub1 = int(input("Sub 1 marks : "))
    sub2 = int(input("Sub 2 marks : "))
    sub3 = int(input("Sub 3 marks : "))
    sub4 = int(input("Sub 4 marks : "))
    
    total = sub1+sub2+sub3+sub4
    
    t = {'name':name,'sub1':sub1 ,'sub2':sub2 ,'sub3':sub3 ,'sub4':sub4 ,'total':total }

    l1.append(t)

print("Name \t Sub1 \t Sub2 \t Sub3 \tSub4")

for i in range(0,len(l1)):
    print(l1[i]['name'],"\t",l1[i]['sub1'],"\t",l1[i]['sub2'],"\t",l1[i]['sub3'],"\t",l1[i]['sub4'])

#first two roll nos
 for i in range(0,2):
    print(l1[i]['name'],"\t",l1[i]['sub1'],"\t",l1[i]['sub2'],"\t",l1[i]['sub3'],"\t",l1[i]['sub4'])
   
#All students ascending order
  l1 = sorted(l1,key = itemgetter('total'))  
for i in range(0,len(l1)):
    print(l1[i]['name'],"\t",l1[i]['sub1'],"\t",l1[i]['sub2'],"\t",l1[i]['sub3'],"\t",l1[i]['sub4'])


#topper
from operator import itemgetter
l = sorted(l1,key = itemgetter('total'))
print(l[::-1][0])

#Highest mark
for i in range(0,len(l1)):
    
    print(l1[i]['name'],"\t",max(l1[i]['sub1'],l1[i]['sub2'],l1[i]['sub3'],l1[i]['sub4']))


#Add two more
for i in range(0,2):
    name = input("Name : ")
    sub1 = int(input("Sub 1 marks : "))
    sub2 = int(input("Sub 2 marks : "))
    sub3 = int(input("Sub 3 marks : "))
    sub4 = int(input("Sub 4 marks : "))
    
    total = sub1+sub2+sub3+sub4
    
    t = {'name':name,'sub1':sub1 ,'sub2':sub2 ,'sub3':sub3 ,'sub4':sub4 ,'total':total }

    l1.append(t)

