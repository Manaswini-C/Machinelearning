import warnings
warnings.filterwarnings("ignore")


import pandas as pd
import numpy as np
import requests
import pickle

model_url = 'https://raw.githubusercontent.com/Manaswini-C/Machinelearning/master/model_pickle2'
response = requests.get(model_url, stream = True)
response.raise_for_status()

model = pickle.loads(response.content)

def predict_house_price(area,bedrooms,age):
    input_data =[[area,bedrooms,age]]
    predicted_price = model.predict(input_data)
    return predicted_price[0]
