# -*- coding: utf-8 -*-
"""House_price_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jLqBEF-hXihyJAR8RhpjX5HpZPYdMHuU

Import & Load data
"""

import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import train_test_split
df=pd.read_csv("/content/drive/MyDrive/cognorise tasks/data (1).csv")
df

df.isna().sum()

df.describe()

df.nunique()

le= LabelEncoder()
df['street']=le.fit_transform(df['street'])
df['city']=le.fit_transform(df['city'])
df['country']=le.fit_transform(df['country'])
df

df.drop('date',inplace=True,axis=1)
df

"""Visualisation"""

plt.figure(figsize=(8,5))
sns.countplot(x='country',data=df,width=0.2,
    order=df["country"].value_counts().index,)
plt.show()

sns.jointplot(x='city',y='yr_built',data=df)

sns.countplot(x='condition',data=df,hue='country')

plt.figure(figsize=(10,7))
sns.boxplot(data=df,x='condition',y='yr_built',palette='hot',width=0.5)
plt.show()

"""Splitting"""

x=df.loc[:,['bedrooms','sqft_above','sqft_living','sqft_lot','sqft_basement','street','city','country']]
x

y=df.iloc[:,:1]
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

lr=LinearRegression()
dec=DecisionTreeRegressor()
gbr=GradientBoostingRegressor()
rfr=RandomForestRegressor()
models=[lr,dec,gbr,rfr]
for model in models:
  print('**',model,'**')
  model.fit(x_train,y_train)
  y_pred= model.predict(x_test)
  y_pred
  print('r2_score:',r2_score(y_test,y_pred)*100)
  print('mae:',mean_absolute_error(y_test,y_pred))
  print('mse:',mean_squared_error(y_test,y_pred))
  print('rmse:',np.sqrt(mean_squared_error(y_test,y_pred)))

new = {'bedrooms': 3.0, 'sqft_above': 1340, 'sqft_living': 1340, 'sqft_lot': 7912, 'sqft_basement': 0, 'street': 1522, 'city': 36, 'country': 0}

new_data = np.array([[new['bedrooms'], new['sqft_above'], new['sqft_living'], new['sqft_lot'], new['sqft_basement'], new['street'], new['city'], new['country']]])

predicted_price = model.predict(new_data)
print("Predicted price:", predicted_price)