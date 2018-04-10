# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:37:59 2018

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

df = pd.read_excel("Book1.xlsx")

print(df.describe())

unit_price = df['Unit price']

print('Mean unit price : ',np.mean(unit_price))
print('Median unit price : ',np.median(unit_price))

print('Mode unit price : ',Counter(unit_price).most_common()[0])

print(df.dtypes)

customers = df.iloc[:,[2,6]]
print(customers)