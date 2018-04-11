import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('employee_data.csv', sep=',')
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dataset['Department'] = labelencoder.fit_transform(dataset['Department'])

X = np.array(dataset.iloc[:, :-1].values).reshape(-1, 4)
y = np.array(dataset.iloc[:, 4].values).reshape(-1, 1)

# Avoiding the Dummy Variable Trap
#X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
