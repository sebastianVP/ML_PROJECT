# ESTE PROGRAMA PERMITE INTERACTUAR CON DATASET DE KAGGLE
#--------------------------------------------------
'''
Developer : Alexander Valdez P.
Ing. Electronico UNI
'''
import os
import json
# DEBEMOS IR A SETTING PARA OBTENER NUESTRA CLAVE
api_token= {"username":"alexandervp","key":"aquivatukeydoctor"}

cmd = 'mkdir /c/Users/soporte/.kaggle'
os.system(cmd)

with open("C:/Users/soporte/.kaggle/kaggle.json",'w') as file:
     json.dump(api_token,file)


cmd = 'chmod 600 /c/Users/soporte/.kaggle/kaggle.json'
os.system(cmd)
print("Well Done!")
