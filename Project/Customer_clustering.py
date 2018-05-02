# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:04:37 2018

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May  2 09:36:29 2018

@author: user
"""

import pandas as pd
import numpy as np

import time, warnings
import datetime as dt

#modules for predictive models
import sklearn.cluster as cluster
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.mixture import GMM

from sklearn.metrics import silhouette_samples, silhouette_score

#visualizations
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

import seaborn as sns

warnings.filterwarnings("ignore")

retail_df = pd.read_excel("C:\\Users\\user\\Desktop\\store-dataset.xlsx")
retail_df.head()

print("Summary..")
#exploring the unique values of each attribute
print("Number of transactions: ", retail_df['Order ID'].nunique())

print("Number of customers:", retail_df['Customer ID'].nunique() )
print("Percentage of customers NA: ", round(retail_df['Customer ID'].isnull().sum() * 100 / len(retail_df),2),"%" )


retail_df['Order Date'].max()


now = dt.date(2017,12,30)
print(now)

retail_df['date'] = retail_df['Order Date'].dt.date

recency_df = retail_df.groupby(by='Customer ID', as_index=False)['date'].max()
recency_df.columns = ['Customer ID','LastPurshaceDate']
recency_df.head()

recency_df['Recency'] = recency_df['LastPurshaceDate'].apply(lambda x: (now - x).days)
recency_df.head()
recency_df.drop('LastPurshaceDate',axis=1,inplace=True)

retail_df_copy = retail_df
retail_df_copy.drop_duplicates(subset=['Order Date', 'Customer ID'], keep="first", inplace=True)
#calculate frequency of purchases
frequency_df = retail_df_copy.groupby(by=['Customer ID'], as_index=False)['Order Date'].count()
frequency_df.columns = ['Customer ID','Frequency']
frequency_df.head()

retail_df['TotalCost'] = retail_df['Quantity'] * retail_df['Sales']
monetary_df = retail_df.groupby(by='Customer ID',as_index=False).agg({'TotalCost': 'sum'})
monetary_df.columns = ['Customer ID','Monetary']
monetary_df.head()

temp_df = recency_df.merge(frequency_df,on='Customer ID')
temp_df.head()

#merge with monetary dataframe to get a table with the 3 columns
rfm_df = temp_df.merge(monetary_df,on='Customer ID')
#use CustomerID as index
rfm_df.set_index('Customer ID',inplace=True)
#check the head
rfm_df.head()

#get the 80% of the revenue
pareto_cutoff = rfm_df['Monetary'].sum() * 0.8
print("The 80% of total revenue is: ",round(pareto_cutoff,2))

customers_rank = rfm_df
# Create a new column that is the rank of the value of coverage in ascending order
customers_rank['Rank'] = customers_rank['Monetary'].rank(ascending=0)
#customers_rank.drop('RevenueRank',axis=1,inplace=True)
customers_rank.head()

customers_rank.sort_values('Rank',ascending=True)
#get top 20% of the customers
top_20_cutoff = 793 *20 /100
top_20_cutoff

revenueByTop20 = customers_rank[customers_rank['Rank'] <= 158]['Monetary'].sum()
revenueByTop20

quantiles = rfm_df.quantile(q=[0.25,0.5,0.75])
quantiles
quantiles.to_dict()

def RScore(x,p,d):
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1
# Arguments (x = value, p = recency, monetary_value, frequency, k = quartiles dict)
def FMScore(x,p,d):
    if x <= d[p][0.25]:
        return 1
    elif x <= d[p][0.50]:
        return 2
    elif x <= d[p][0.75]: 
        return 3
    else:
        return 4

rfm_segmentation = rfm_df
rfm_segmentation['R_Quartile'] = rfm_segmentation['Recency'].apply(RScore, args=('Recency',quantiles,))
rfm_segmentation['F_Quartile'] = rfm_segmentation['Frequency'].apply(FMScore, args=('Frequency',quantiles,))
rfm_segmentation['M_Quartile'] = rfm_segmentation['Monetary'].apply(FMScore, args=('Monetary',quantiles,))

rfm_segmentation.head()
rfm_segmentation['RFMScore'] = rfm_segmentation.R_Quartile.map(str) \
                            + rfm_segmentation.F_Quartile.map(str) \
                            + rfm_segmentation.M_Quartile.map(str)
rfm_segmentation.head()

rfm_segmentation[rfm_segmentation['RFMScore']=='444'].sort_values('Monetary', ascending=False).head(10)

print("Best Customers: ",len(rfm_segmentation[rfm_segmentation['RFMScore']=='444']))
print('Loyal Customers: ',len(rfm_segmentation[rfm_segmentation['F_Quartile']==4]))
print("Big Spenders: ",len(rfm_segmentation[rfm_segmentation['M_Quartile']==4]))
print('Almost Lost: ', len(rfm_segmentation[rfm_segmentation['RFMScore']=='244']))
print('Lost Customers: ',len(rfm_segmentation[rfm_segmentation['RFMScore']=='144']))
print('Lost Cheap Customers: ',len(rfm_segmentation[rfm_segmentation['RFMScore']=='111']))

rfm_data = rfm_df.drop(['R_Quartile','F_Quartile','M_Quartile','RFMScore'],axis=1)
rfm_data.head()

rfm_data.corr()

sns.heatmap(rfm_data.corr())
scatter_matrix(rfm_data, alpha = 0.3, figsize = (11,5), diagonal = 'kde');