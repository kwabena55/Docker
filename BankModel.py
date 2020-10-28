#!/usr/bin/env python
# coding: utf-8

# ### Bank Note Authentication
# Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

# In[2]:


import pandas as pd
import numpy as np


# In[5]:


# Import Data
data= pd.read_csv("BankNote_Authentication.csv")


# In[6]:


data.head()


# In[8]:


# Extract X and Y values  i.e Independent and Dependent Features
X= data.iloc[:,:-1]
y=data.iloc[:,-1]


# In[9]:


X.head()


# In[10]:


y.head()


# In[12]:


#Split data into Test and Training Samples
from sklearn.model_selection import train_test_split


# In[14]:


X_train, X_test, y_train, y_test= train_test_split(X,y,test_size= 0.3, random_state=True)


# In[17]:


#Implement random Forest Classifier  for Model training
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)


# In[19]:


#Prediction
y_pred=classifier.predict(X_test)


# In[26]:


#Check Accuracy
from sklearn.metrics import accuracy_score, precision_score
score=accuracy_score(y_test,y_pred)


# In[27]:


score


# In[30]:


score2= precision_score(y_test,y_pred)
score2


# In[31]:


#Create a Pickle file using Serialization
import pickle
pickle_out= open("classifier.pkl","wb")
pickle.dump(classifier, pickle_out)


# In[33]:


#Check some Predictions
classifier.predict([[10,-1,2,3]])


# In[ ]:




