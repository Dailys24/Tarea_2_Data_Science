#Problema 3: Nota más frecuente (moda) considerando todas las notas de todos los estudiantes (Uso de Pandas).

import pandas as pd
from Datos import datos

def problema3():
    df_alumnos = pd.DataFrame(datos)

    # Convertir todas las listas de notas en una sola columna
    todas_notas = df_alumnos['notas'].explode()

    # Calcular moda (nota más frecuente) y su frecuencia
    moda = todas_notas.mode().iloc[0]
    frecuencia = (todas_notas == moda).sum()

    print("------------- Nota más frecuente (moda) -------------")
    print(f"La nota más frecuente es {moda:.1f}, apareciendo {frecuencia} veces.")
