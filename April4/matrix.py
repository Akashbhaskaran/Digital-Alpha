from numpy import *
a = array([['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95]])

print(a[:3,[0,1]])


a= append(a,[['Sam',82,79,88,97,99]],0)
print(a)

a[0][3] = 95
print(a)

a= insert(a,[6],[[73],[80],[85],[100]],axis=1)
print(a)