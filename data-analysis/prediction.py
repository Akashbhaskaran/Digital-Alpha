import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel("Book1.xlsx")
Xi = np.array(dataset['Week']).reshape(-1,1)
Yp1 = np.array(dataset['PRICE 12PK']).reshape(-1,1)
Yp2 = np.array(dataset['PRICE 18PK']).reshape(-1,1)
Yp3 = np.array(dataset['PRICE 30PK']).reshape(-1,1)

yp4 = np.array(dataset['CASES 12PK']).reshape(-1,1)
yp5 = np.array(dataset['CASES 18PK']).reshape(-1,1)
yp6 = np.array(dataset['CASES 30PK']).reshape(-1,1)

print(dataset.corr())

# fitting datas to linear_model
from sklearn.linear_model import LinearRegression
regress1 = LinearRegression()
regress2 = LinearRegression()
regress3 = LinearRegression()
regress4 = LinearRegression()
regress5 = LinearRegression()
regress6 = LinearRegression()

# week vs price12
regress1.fit(Xi,Yp1)
regress1.coef_
plt.figure(1)
plt.scatter(Xi,Yp1)
plt.plot(Xi,regress1.predict(Xi))
plt.title("Week vs Price 12PK")
plt.xlabel("Weeks")
plt.ylabel("Price 12PK")

# week vs price18
regress2.fit(Xi,Yp2)
regress2.coef_
plt.figure(2)
plt.scatter(Xi,Yp2)
plt.plot(Xi,regress2.predict(Xi))
plt.title("Week vs Price 18PK")
plt.xlabel("Weeks")
plt.ylabel("Price 18PK")

# week vs price30
regress3.fit(Xi,Yp3)
regress3.coef_
plt.figure(3)
plt.scatter(Xi,Yp3)
plt.plot(Xi,regress3.predict(Xi))
plt.title("Week vs Price 30PK")
plt.xlabel("Weeks")
plt.ylabel("Price 30PK")

# Price12 vs case12
regress4.fit(Yp1,yp4)
regress4.coef_
plt.figure(4)
plt.scatter(Yp1,yp4)
plt.plot(Yp1,regress4.predict(Yp1))
plt.title("Price 12PK vs Case 12PK")
plt.xlabel("Price 12Pk")
plt.ylabel("Case 12PK")

# Price18 vs case18
regress5.fit(Yp2,yp5)
regress5.coef_
plt.figure(5)
plt.scatter(Yp2,yp5)
plt.plot(Yp2,regress5.predict(Yp2))
plt.title("Price 18PK vs Case 18PK")
plt.xlabel("Price 18Pk")
plt.ylabel("Case 18PK")

# Price30 vs case30
regress6.fit(Yp3,yp6)
regress6.coef_
plt.figure(6)
plt.scatter(Yp3,yp6)
plt.plot(Yp3,regress6.predict(Yp3))
plt.title("Price 30PK vs Case 30PK")
plt.xlabel("Price 30Pk")
plt.ylabel("Case 30PK")

# forecasting 
y_pred12 = regress1.predict(np.array([53,54,55,56,57,58,59,60]).reshape(-1,1))
y_pred18 = regress2.predict(np.array([53,54,55,56,57,58,59,60]).reshape(-1,1))
y_pred30 = regress3.predict(np.array([53,54,55,56,57,58,59,60]).reshape(-1,1))

y_case12 = regress4.predict(y_pred12)
y_case18 = regress5.predict(y_pred18)
y_case30 = regress6.predict(y_pred30)
