#Problema1.py

import pandas as pd
from Datos import datos

def problema1():
    #Realiza un análisis completo de las notas y muestra los resultados.
    df_alumnos = pd.DataFrame(datos)

    #Calcular el promedio de cada alumno
    df_alumnos['promedio']=df_alumnos['notas'].apply(lambda notas: sum(notas) / len(notas))

    print("\n------------- Promedios -------------")
    print(df_alumnos[['nombre', 'promedio']].round(1))
