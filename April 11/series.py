# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:30:59 2018

@author: user
"""

n = int(input("ENter Number"))
a=[]
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    if(i<n):
        print("+",sep=" ",end=" ")
    a.append(i)
print("=",sum(a))
 
print()

for i in range(0,500):
    if(i%n == 0):
        print(i)
        
print(n+n*n+n*n*n)


a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()

sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))