#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a flask api for the Model
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger


# In[2]:


app=Flask(__name__)
Swagger(app)


# In[3]:


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)


# In[4]:


#USe of python decorator to generate the root api
@app.route('/')
def welcome():
    return "welcome All"




# In[5]:


# @app.route('/predict')
# def predict_note_authentication():
#     '''
#     create four variables  for the four independent variables
    
#     '''
#     variance=request.args.get('variance')
#     skewness=request.args.get('skewness')
#     curtosis=request.args.get('curtosis')
#     entropy=request.args.get('entropy')
#     prediction= classifier.predict([[variance, skewness,curtosis,entropy]])
#     return 'The predicted value for the loaded bank note is ' + str(prediction)
    


# In[6]:


# #Prediciting a file
# @app.route('/predict_file', methods=["POST"])
# def predict_note():
#     df_test=pd.read_csv(request.files.get("file"))
#     prediction2=classifier.predict(df_test)
#     return "Predicited value for the file uploaded is " + str(list(prediction2))


# In[ ]:





# In[7]:



@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)


# In[8]:


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))


    


# In[ ]:


if __name__=='__main__':
    app.run()


# In[ ]:




