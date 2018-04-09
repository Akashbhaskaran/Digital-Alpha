import numpy as np
import matplotlib.pyplot as plt

temp = np.array([14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1])
ice = np.array([215,325,185,332,406,522,412,614])

plt.scatter(temp, ice, color='blue')

tmean = np.mean(temp)
imean = np.mean(ice)
a = 0
b = 0

for i in range(len(temp)):
    a = a + ((temp[i]-tmean)*(ice[i]-imean))
    b = b + (temp[i]-tmean)**2

cf = a/b
con = imean - cf*tmean

regress = []
for i in range(len(temp)):
    regress.append(con+(cf*temp[i]))
    
# regression line
plt.plot(temp, regress, color = 'green')
plt.show()
