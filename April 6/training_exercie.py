import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = [8,2,11,6,5,4,12,9,6,1]
Y = [3,10,3,6,8,12,1,4,9,14]

Xmean = np.mean(X)
Ymean = np.mean(Y)

Xi = []
for i in range(len(X)):
    Xi.append(X[i] - Xmean)
    
Yi = []
for i in range(len(Y)):
    Yi.append(Y[i] - Ymean)
    
Xxy = []
for i in range(len(Xi)):
    Xxy.append(Xi[i]*Yi[i])
    
Xs = []
for i in range(len(Xi)):
    Xs.append((X[i]-Xmean)**2)
    
A = sum(Xxy)
B = sum(Xs)

slope = A/B

inter = Ymean - (slope*Xmean)
regress = []
for i in range(len(X)):
    regress.append(inter+(slope*X[i]))

plt.scatter(X, Y, color = 'red')
plt.plot(X, regress, color = 'blue')
plt.title('Linear regression')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
