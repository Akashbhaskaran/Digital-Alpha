# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:30:00 2018

@author: user
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

data = pd.read_csv('adult.csv', header = 0)
data = data.dropna()
data = data.drop(data[data.occupation ==' ?'].index)
data = data.drop(data[data['native-country'] ==' ?'].index)

data = data.drop(data[data.workclass ==' ?'].index)
print(data.shape)
print(list(data.columns))

data.head()

data['education'].unique()

data['y'].value_counts()
data['relationship'].value_counts()
data['marital-status'].value_counts()

sns.countplot(x = 'y', data = data)

data['marital-status'].unique()

data.groupby('y').mean()
data.groupby('marital-status').mean()
data.groupby('race').mean()
data.groupby('sex').mean()

pd.crosstab(data.occupation,data.y).plot(kind='bar')
plt.title(' Frequency for Salary ')
plt.xlabel('Occupation')
plt.ylabel('Frequency of Salary')
plt.savefig('purchase_fre_job')
plt.show()

pd.crosstab(data.age,data.y).plot(kind='bar')
plt.title('Frequency for Salary')
plt.xlabel('Age')
plt.ylabel('Frequency of Salary')
plt.show()


pd.crosstab(data.education,data.y).plot(kind='bar')
plt.title(' Frequency for Salary')
plt.xlabel('Education')
plt.ylabel('Frequency of Salary')
plt.show()

pd.crosstab(data.relationship,data.y).plot(kind='bar')
plt.title(' Frequency for Salary')
plt.xlabel('relationship')
plt.ylabel('Frequency of Salary')
plt.show()

pd.crosstab(data.race,data.y).plot(kind='bar')
plt.title(' Frequency for Salary')
plt.xlabel('Race')
plt.ylabel('Frequency of Salary')
plt.show()

pd.crosstab(data['marital-status'],data.y).plot(kind='bar')
plt.title(' Frequency for Job Title')
plt.xlabel('Marital-Status')
plt.ylabel('Frequency of Salary')
plt.show()

pd.crosstab(data['native-country'],data.y).plot(kind='bar')
plt.title(' Frequency for Job Title')
plt.xlabel('Country')
plt.ylabel('Frequency of Salary')
plt.show()


cat_vars=['occupation','marital-status','native-country','sex','race','workclass']

for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1
    
cat_vars=['occupation','marital-status','native-country','sex','race','workclass','education','relationship']    
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

data_final=data[to_keep]
data_final.columns.values

data_final_vars=data_final.columns.values.tolist()
y=['y']
X=[i for i in data_final_vars if i not in y]

from sklearn import datasets
from sklearn.feature_selection import RFE

logreg = LogisticRegression()

rfe = RFE(logreg, 20)
rfe = rfe.fit(data_final[X], data_final[y] )

print(rfe.support_)
print(rfe.ranking_)

cols=["occupation_ Craft-repair", "occupation_ Farming-fishing", "occupation_ Machine-op-inspct","occupation_ Other-service","occupation_ Priv-house-serv","occupation_ Prof-specialty","occupation_ Protective-serv",
      "occupation_ Sales", "marital-status_ Divorced","marital-status_ Married-AF-spouse","native-country_ China","native-country_ Cuba","native-country_ Laos","native-country_ Mexico","native-country_ Nicaragua","native-country_ Outlying-US(Guam-USVI-etc)",
      "native-country_ United-States","sex_ Male","race_ Black","workclass_ Without-pay"] 

X=data_final[cols]
y=data_final['y']

from sklearn.preprocessing import LabelEncoder

obj = LabelEncoder()
y = obj.fit_transform(y)

from scipy import stats
stats.chisqprob = lambda chisq, df : stats.chi2.sf(chisq,df)

import statsmodels.api as sm
logit_model=sm.Logit(y,X)
result=logit_model.fit()
print(result.summary())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

from sklearn import model_selection
from sklearn.model_selection import cross_val_score
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()