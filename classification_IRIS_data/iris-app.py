# LIBRERIAS

import streamlit  as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Desarrollo Web y Metodos de ML
#st.title('IRIS ML App -Data Scientis')
st.write("""
# Simple Iris Flower Prediction App

This app predictsthe Iris Flower  Type!
***
""") 
## LA PAGINA WEB TIENE 2 PANELES
## 1. PARAMETROS DE ENTRADA, donde escogemos las variables
## 2. CUERPO DE LA  WEB, DONDE SE MUESTRA LOS RESULTADOS -PREDICCION


## EL ESQUEMA CENTRAL ES DE LA SIGUIENTE FORMA
## 1. PARAMETROS DE ENTRADA 4: length y width de sepal y petal 
## 2. Etiquetas de las clases que podemos obtener como salida
## 3. Prediction
## 4. Probabilidad de Prediccion


st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',4.3,7.9,5.4)
    sepal_width  = st.sidebar.slider('Sepal width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal Length',1.0,6.9,1.3)
    petal_width  = st.sidebar.slider('Petal width',0.1,2.5,0.2)
    data         = {'sepal_length': sepal_length,
                    'sepal_width' : sepal_width,
                    'petal_length': petal_length,
                    'petal_width' : petal_width}
    features     = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()  

st.subheader('User input Parameters')
st.write(df)
## ML
# cargamos la data
iris  = datasets.load_iris()
# train y test
#  x e y
X     = iris.data
Y     = iris.target
# escogemos el modelo
clf   = RandomForestClassifier()
# ajuste del modelo
clf.fit(X,Y)
# ya podemos predecir input x output y
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader("Class Label and their corresponding index number")
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)

