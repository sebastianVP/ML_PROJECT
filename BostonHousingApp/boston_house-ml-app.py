import streamlit as st
import pandas as pd

from sklearn import datasets
import  matplotlib.pyplot as plt

st.write("""
# Aplicacion Web Precio de Casas de Boston

Esta aplicacion predice el precio de una **Casa de Boston**!
""")

st.write('---')
## CARGAR LA DATA
#boston = datasets.load_boston()
boston =pd.read_csv("BostonHousing.csv") 
print(boston.columns)
features=['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax','ptratio', 'b', 'lstat']
#X = boston.loc[:,features].values
#Y = boston.loc[:,['medv']].values
X=boston
## SIDEBAR
# HEADER PARA ESPECIFICAR PARAMETROS DE ENTRADA
st.sidebar.header("Especifica los Parametros de Entrada")

def user_input_features():
    CRIM    = st.sidebar.slider('CRIM',X.crim.min(),X.crim.max(),X.crim.mean())
    ZN      = st.sidebar.slider('ZN',X.zn.min(),X.zn.max(),X.zn.mean())
    INDUS   = st.sidebar.slider('INDUS',X.indus.min(),X.indus.max(),X.indus.mean())
    CHAS    = st.sidebar.slider('CHAS',float(X.chas.min()),float(X.chas.max()),X.chas.mean())
    NOX     = st.sidebar.slider('NOX',X.nox.min(),X.nox.max(), X.nox.mean())
    RM      = st.sidebar.slider('RM',X.rm.min(),X.rm.max(),X.rm.mean())
    AGE     = st.sidebar.slider('AGE',X.age.min(),X.age.max(),X.age.mean())
    DIS     = st.sidebar.slider('DIS',X.dis.min(),X.dis.max(),X.dis.mean())
    RAD     = st.sidebar.slider('RAD',float(X.rad.min()),float(X.rad.max()),X.rad.mean())
    TAX     = st.sidebar.slider('TAX',float(X.tax.min()),float(X.tax.max()),X.tax.mean())
    PTRATIO = st.sidebar.slider('PTRATIO',X.ptratio.min(),X.ptratio.max(),X.ptratio.mean())
    B       = st.sidebar.slider('B',X.b.min(),X.b.max(),X.b.mean())
    LSTAT   = st.sidebar.slider('LSTAT',X.lstat.min(),X.lstat.max(),X.lstat.mean())
    data    = {'CRIM':CRIM,
                'ZN':ZN,
                 'INDUS':INDUS,
                  'CHAS':CHAS,
                    'NOX':NOX,
                      'RM':RM,
                       'AGE':AGE,
                        'DIS':DIS,
                         'RAD':RAD,
                          'TAX':TAX,
                           'PTRATIO':PTRATIO,
                            'B':B,
                              'LSTAT':LSTAT}
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input_features()
# MAIN PANEL
# IMPRIMIR PARAMETROS DE ENTRADA ESPECIFICO
st.header('Specified Inputa Parameters')
st.write(df)
st.write('---')

# BUILD REGRESSION MODEL
