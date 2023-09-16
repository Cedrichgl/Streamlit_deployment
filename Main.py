import setuptools
import streamlit as st
import pickle
import sklearn 
import pandas as pd
import numpy as np
from PIL import Image

#chargement du fichier model
Model = pickle.load(open('model.sav','rb'))

st.title('Prédiction du prix de la maison')
st.sidebar.header('Date de la maison')
Image = Image.open('Lagos.jpg')


#Les input 
def User_report():
    Bedrooms = st.sidebar.slider('Bedrooms',1,6)
    Bathrooms = st.sidebar.slider('Bathrooms',1,4)
    Stories = st.sidebar.slider('Stoties',1,4)
    Parking = st.sidebar.slider('Parking',1,3)

    Data = {
        'Bedrooms':Bedrooms,
        'Bathrooms':Bathrooms,
        'Stories':Stories,
        'Parking':Parking
    }

    Features = pd.DataFrame(Data,index=[0])
    return Features

User_data = User_report()
st.subheader("Cout de la maison")
st.write(User_data)


Price = model.predict(User_data)
st.subheader('Prix de estimé de la maison')
