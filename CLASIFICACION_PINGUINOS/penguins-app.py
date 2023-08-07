#----- LIBRERIAS UTILIZADAS------
import streamlit as st
import pandas    as pd
import numpy     as np
import pickle
from sklearn.ensemble import RandomForestClassifier
#----------Librerias de desarrollo Web, manejo de dataframe , arrays y el pickle-----
#----------para almacenar el modelo, la libreria de ML es el sklearn.ensemble--------

st.write("""
#  Aplicacion de Prediccion de Pinguinos

Esta aplicacion predice las especies de **Pinguinos Palmer** !
Data obtenida desde  la [Libreria Pinguinos Palmer](https://github.com/allisonhorst/palmerpenguins)
""")
#-------------- SIDEBAR- User Input Features
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Ejemplo CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# COLLECTS USER INPUT FEATURES INTO DATAFRAME

uploaded_file = st.sidebar.file_uploader("Upload your input CSV file",type=["csv"])
if uploaded_file is not None:
   input_df = pd.read_csv(uploaded_file)
else:
   def user_input_features():
       island               = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
       sex                  = st.sidebar.selectbox('Sex',('male','female'))
       pico_longitud_mm     = st.sidebar.slider('Longitud de Pico (mm)'  ,32.1,59.6,43.9)
       pico_profundidad_mm  = st.sidebar.slider('Profundidad de Pico(mm)',13.1,21.5,17.2)
       aleta_longitud_mm    = st.sidebar.slider('Longitud de Aleta(mm)',172.0,231.0,201.0)
       masa_corporal_g      = st.sidebar.slider('Masa de Cuerpo (g)',2700.0,6300.0,4207.0)
       data = { 'island'              : island,
                'bill_length_mm'      : pico_longitud_mm,
                'bill_depth_mm'       : pico_profundidad_mm,
                'flipper_length_mm'   : aleta_longitud_mm,
                'body_mass_g'          : masa_corporal_g,
                'sex'                 : sex}
       features = pd.DataFrame(data,index=[0])
       return features
   input_df = user_input_features()
# Combines user input features with entire penguins dataset
# this will be useful for the encoding phase

penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins     = penguins_raw.drop(columns = ['species'])
df           = pd.concat([input_df,penguins],axis = 0)

## ENCODING OF ORDINAL FEATURES
encode = ['sex','island']
for col in encode:
    dummy = pd.get_dummies(df[col],prefix=col)
    df    = pd.concat([df,dummy],axis=1)
    del df[col]

df = df[:1] # SELECCIONAMOS SOLO LA PRIMERA FILA(DATA DEL USUARIO DE ENTRADA)

# DISPLAYS THE USER INPUT FEATURES
st.subheader("User Input features")

if uploaded_file is not None:
   st.write(df)
else:
   st.write('Awaiting CSV File to ve uploaded. Currently using example input parameters(shown below),')
   st.write(df)

# READS IN SAVE CLASSIFICATION MODEL
# https://github.com/dataprofessor/penguins-heroku/blob/master/penguins_clf.pkl
load_clf = pickle.load(open('penguins_clf.pkl','rb'))
# APPLY MODEL TO MAKE PREDICTIONS
prediction       = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
