#Problema7.py

import pandas as pd
from Datos import datos

def problema7():
    # Realiza un análisis completo de las notas y muestra los resultados.
    df_alumnos = pd.DataFrame(datos)

    # Calcular el promedio de cada alumno
    df_alumnos['promedio'] = df_alumnos['notas'].apply(lambda notas: sum(notas) / len(notas))

    # Promedio más alto y más bajo
    alumno_nota_max = df_alumnos.loc[df_alumnos['promedio'].idxmax()]
    alumno_nota_min = df_alumnos.loc[df_alumnos['promedio'].idxmin()]

    print("------------- Promedio mas alto y bajo -------------")
    print("------------------------------------------------------------------------------------")
    print(f"El alumno con el promedio más alto es {alumno_nota_max['nombre']} con un promedio de: {alumno_nota_max['promedio']:.1f}")
    print("------------------------------------------------------------------------------------")
    print(f"El alumno con el promedio más bajo es {alumno_nota_min['nombre']} con un promedio de: {alumno_nota_min['promedio']:.1f}")
