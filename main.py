import uvicorn #for ASGI
from fastapi import FastAPI
from banknote import BankNote
import numpy as np
import pickle
import pandas as pd 

app=FastAPI()

pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get("/")
def index():
    return "Hello! This is running"

#Expose prediction functionality, make prediction from the passed JSON data and return 
#the predicted bank note with confidence.

@app.post("/predict")
def predict_banknote(data:BankNote):   #data is temp variable which will capture the the post data
    data= data.model_dump()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if (prediction[0]>0.5):
        prediction='Fake Note'
    else:
        prediction='Its a bank note'
    return {'prediction':prediction} 

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000) 
