#Problema2.py

import pandas as pd
from Datos import datos

def problema2():
    #Realiza un análisis completo de las notas y muestra los resultados.
    df_alumnos = pd.DataFrame(datos)

    #Calcular el promedio de cada alumno
    df_alumnos['promedio']=df_alumnos['notas'].apply(lambda x: sum(x) / len(x))

    #Estudiantes con promedio >= 4.0
    aprobados=df_alumnos[df_alumnos['promedio'] >= 4.0]

    print("------------- Estudiantes que Aprobaron -------------")

    #Si no hay estudiantes aprobados, mostrar un mensaje
    if aprobados.empty:
        print("No hay estudiantes que hayan aprobado.")
    else:
        print(aprobados[['nombre', 'promedio']].round(1).to_string(index=False))
