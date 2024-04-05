# -*- coding: utf-8 -*-
"""Breast _cancer_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zwrXdm3mqcrIeIcXRdnJ2RDDtYl9r9f4
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, mean_squared_error, classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
warnings.filterwarnings('ignore')

"""Load data"""

df=pd.read_csv("/content/drive/MyDrive/cognorise tasks/data.csv")
df

df.isna().sum()

df.dtypes

df.drop(columns=['Unnamed: 32','id'],inplace=True)
df

df['diagnosis'].value_counts()

sns.countplot(x='diagnosis',data=df)
plt.title('diagnosis count')

df['diagnosis']=df['diagnosis'].map({'M':1,'B':0})
df

df['diagnosis'].value_counts()

x=df.iloc[:,1:]
x

y=df.iloc[:,:1]
y

"""Balancing Dataset"""

from imblearn.over_sampling import SMOTE
sm=SMOTE()
x_resambled,y_resambled=sm.fit_resample(x,y)

y_resambled.value_counts()

"""Scailing method"""

scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(x_resambled)
x_scaled

x_train,x_test,y_train,y_test=train_test_split(x_resambled,y_resambled,random_state=1,test_size=0.3)

x_train_classification, x_train_regression, y_train_classification, y_train_regression = train_test_split(x_train, y_train, test_size=0.5)
x_test_classification, x_test_regression, y_test_classification, y_test_regression = train_test_split(x_test, y_test, test_size=0.5)

"""Model preparation"""

knn = KNeighborsClassifier()
rf = RandomForestClassifier()
dec = DecisionTreeClassifier()
li = LinearRegression()
lo = LogisticRegression()
classification_models = [knn, rf, dec]
regression_models = [li,lo]
# Classification task
for model in classification_models:
    print("**", model, "**")
    model.fit(x_train_classification, y_train_classification)
    y_pred_classification = model.predict(x_test_classification)
    print("Classification Report:")
    print(classification_report(y_test_classification, y_pred_classification))
    print("Accuracy:", accuracy_score(y_test_classification, y_pred_classification))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test_classification, y_pred_classification))
    print()

# Regression task
for model in regression_models:
    print("**", model, "**")
    model.fit(x_train_regression, y_train_regression)
    y_pred_regression = model.predict(x_test_regression)
    mse = mean_squared_error(y_test_regression, y_pred_regression)
    print("Mean Squared Error (Regression):", mse)
    print()

"""Hyperparameter Tuning On Randomforest classifier"""

from sklearn.model_selection import GridSearchCV
param={'n_estimators':[500],'criterion':['gini','entropy','log_loss'],'max_features':['auto','sqrt','log2']}  #splitting
clf=GridSearchCV(RandomForestClassifier(),param,cv=10,scoring='accuracy')
clf.fit(x_train,y_train)

print(clf.best_params_)

rf=RandomForestClassifier(max_features='sqrt',criterion='entropy',n_estimators=500)
rf.fit(x_train,y_train)
y_pred_1=rf.predict(x_test)
y_pred_1
print(classification_report(y_test,y_pred_1))

"""Got the highest accuracy in RandomForestClassifier than other classifiers and by using best parameters method then i was able to improve the accuracy of the model"""