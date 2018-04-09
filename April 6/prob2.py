import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_excel('ca_result.xlsx')
X = dataset.iloc[1:, 0]
y1 = dataset.iloc[1:, 3]
y2 = dataset.iloc[1:, 6]
y3 = dataset.iloc[1:, 9]


plt.plot(X, y1, color = 'red')
plt.show()
plt.plot(X, y2, color = 'blue')
plt.show()
plt.plot(X, y3, color = 'green')
plt.show()
