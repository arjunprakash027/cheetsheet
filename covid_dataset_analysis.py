# -*- coding: utf-8 -*-
"""covid_dataset_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IMbPNYEo2P_OYj1_P8rjuXj4V_H9OKrg
"""

import pandas as pd

df = pd.read_csv('/content/Covid_Dataset.csv')

df

df.head()

df.info()

df['COVID-19'].value_counts()

df.columns

cat_cols = ['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Running Nose', 'Asthma', 'Chronic Lung Disease', 'Headache',
       'Heart Disease', 'Diabetes', 'Hyper Tension', 'Fatigue ',
       'Gastrointestinal ', 'Abroad travel', 'Contact with COVID Patient',
       'Attended Large Gathering', 'Visited Public Exposed Places',
       'Family working in Public Exposed Places', 'Wearing Masks',
       'Sanitization from Market', 'COVID-19']

"""#FEATURE ENGI"""

from sklearn.preprocessing import LabelEncoder

for cols in cat_cols:
  le = LabelEncoder()
  df[cols] = le.fit_transform(df[cols])

df

df['Wearing Masks'].value_counts()

df['Sanitization from Market'].value_counts()

df.columns



import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 14,12

df.corr()

import seaborn as sb
sb.heatmap(df.corr(),annot=True)

df = df[['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Running Nose', 'Asthma','Heart Disease', 'Diabetes', 'Hyper Tension',
       'Gastrointestinal ', 'Abroad travel', 'Contact with COVID Patient',
       'Attended Large Gathering', 'Visited Public Exposed Places',
       'Family working in Public Exposed Places', 'Wearing Masks', 'COVID-19']]

df.info(
)

df.to_csv('covid_analysed.csv')

sb.pairplot(df,hue='COVID-19')

"""#training

"""

import pandas as pd
df = pd.read_csv('/content/covid_analysed.csv')

x = df[['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Running Nose', 'Asthma','Heart Disease', 'Diabetes', 'Hyper Tension',
       'Gastrointestinal ', 'Abroad travel', 'Contact with COVID Patient',
       'Attended Large Gathering', 'Visited Public Exposed Places',
       'Family working in Public Exposed Places', 'Wearing Masks']].values
y = df[['COVID-19']].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

""" #resize so that our model is not biased

"""

from imblearn.under_sampling import RandomUnderSampler
rus=RandomUnderSampler()

x,y=rus.fit_resample(x,y)

x.shape,y.shape

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

df.info(
    
)

df.columns

lr.predict([[0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1]])

import pickle

Pkl_Filename = "covid_prediction.pkl"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(lr, file)

with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

Pickled_LR_Model.predict(x_test)