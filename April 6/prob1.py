import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dat = np.array([425,430,430,435,435,435,435,435,440,440,440,440,440,445,445,445,445,445,450,450,450,450,450,450,450,460,460,460,465,465,465,470,470,472,475,475,475,480,480,480,480,485,490,490,490,500,500,500,500,510,510,515,525,525,525,535,549,550,570,570,575,575,580,590,600,600,600,600,615,615])

from scipy import stats
d = stats.itemfreq(dat)

# scatter graph
plt.scatter(d[:,0], d[:,1], color='blue')

d1mean = np.mean(d[:,0])
d2mean = np.mean(d[:,1])
a = 0
b = 0

for i in range(len(d[:,0])):
    a = a + ((d[i][0]-d1mean)*(d[i][1]-d2mean))
    b = b + (d[i][0]-d1mean)**2

cf = a/b
con = d2mean - cf*d1mean

regress = []
for i in range(len(d[:,0])):
    regress.append(con+(cf*d[i][0]))
    
# regression line
plt.plot(d[:,0], regress, color = 'green')
plt.show()

# histogram
plt.hist(dat)
plt.show()
