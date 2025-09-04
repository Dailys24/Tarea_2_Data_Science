#Problema6.py

import pandas as pd
from Datos import datos

def problema6():
    # Realiza un análisis completo de las notas y muestra los resultados.
    df_alumnos = pd.DataFrame(datos)

    # Calcular el promedio de cada alumno
    df_alumnos['promedio'] = df_alumnos['notas'].apply(lambda notas: sum(notas) / len(notas))

    # Calcular el promedio general
    promedio_general = df_alumnos['promedio'].mean()

    print("------------- Promedio general del curso -------------")
    print(f"Promedio general del curso: {promedio_general:.1f}")
