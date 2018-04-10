# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:10:29 2018

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df.columns)

b = df.iloc[:10,:10]

itemtype = df['Item Type']
profit = df['Total Profit']

profit = np.array(df['Total Profit']).reshape(-1,1)

plt.plot(profit)
plt.show()

l = []


for i in range(len(profit)):
    if(profit[i]>1000000):
        print(itemtype[i])