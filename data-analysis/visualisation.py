import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel("Book1.xlsx")
Xi = dataset['Week']
Yp1 = dataset['PRICE 12PK']
Yp2 = dataset['PRICE 18PK']
Yp3 = dataset['PRICE 30PK']

yp4 = dataset['CASES 12PK']
yp5 = dataset['CASES 18PK']
yp6 = dataset['CASES 30PK']

plt.plot(Xi,Yp1,color='blue')
plt.title("Week vs Price12_PK")
plt.xlabel("Week")
plt.ylabel("Price12_PK")
plt.show()

plt.plot(Xi,Yp2,color='red')
plt.title("Week vs Price18_PK")
plt.xlabel("Week")
plt.ylabel("Price18_PK")
plt.show()

plt.plot(Xi,Yp3,color='green')
plt.title("Week vs Price30_PK")
plt.xlabel("Week")
plt.ylabel("Price30_PK")
plt.show()

plt.plot(Xi,yp4,color='blue')
plt.title("Week vs Case12_PK")
plt.xlabel("Week")
plt.ylabel("Case12_PK")
plt.show()

plt.plot(Xi,yp5,color='red')
plt.title("Week vs Case18_PK")
plt.xlabel("Week")
plt.ylabel("Case18_PK")
plt.show()

plt.plot(Xi,yp6,color='green')
plt.title("Week vs Case30_PK")
plt.xlabel("Week")
plt.ylabel("Case30_PK")
plt.show()