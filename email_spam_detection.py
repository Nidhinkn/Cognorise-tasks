# -*- coding: utf-8 -*-
"""Email spam detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UJMIx7UzqOeYA-atiFQVUKLCRmX6wQqw
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from nltk.stem import SnowballStemmer
from nltk import TweetTokenizer
from nltk.corpus import stopwords
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import warnings
import seaborn as sns
import pandas as pd
df=pd.read_csv('/content/drive/MyDrive/cognorise tasks/spam.csv')
df

df.isna().sum()

df['Category'].value_counts()

sns.countplot(x='Category',data=df)

df['Category']=df['Category'].map({'ham':0,'spam':1})
df

df.describe()

df.head(15)

df.tail()

Message=df.Message
Message

Message=Message.str.replace('[^a-zA-Z0-9]+'," ")
Message

stemmer=SnowballStemmer('english')
tk=TweetTokenizer()

Message=Message.apply(lambda line:[stemmer.stem(token.lower())for token in tk.tokenize(line)]).apply(lambda token:" ".join(token))
Message

nltk.download('stopwords')
sw=stopwords.words('english')
sw

Message = Message.apply(lambda line:[token for token in tk.tokenize(line) if token not in sw ]).apply(lambda token:" ".join(token))
Message

vectorizer=TfidfVectorizer()
x=vectorizer.fit_transform(Message)
print(x)

x.shape

x=x.toarray()
x

df1=pd.DataFrame(x)
df1

x=df1.iloc[:,:]
x

y=df.iloc[:,:1]
y

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

knn=KNeighborsClassifier()
ad=AdaBoostClassifier()
rf=RandomForestClassifier()
lo=LogisticRegression()
models=[knn,ad,rf,lo]
for model in models:
  print("****", model,"****")
  model.fit(x_train,y_train)
  y_pred=model.predict(x_test)
  y_pred
  print(classification_report(y_test,y_pred))

nw=vectorizer.transform(['Will ü b going to esplanade fr home?'])
nw=nw.toarray()
y=model.predict(nw)
if y==0:
  print('ham')
elif y==1:
  print('spam')