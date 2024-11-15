import pickle

with open('model_pickel2",'rb') as f:
    model=pickel.load(f)

def predict_house_price(area,bedrooms,age):
    input_data=[[area,bedrooms,age]]
    predicted_price=model.predict(input_data)
    return predicted_price[0]
  
