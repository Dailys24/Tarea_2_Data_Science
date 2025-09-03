#Problema 4: Porcentaje de estudiantes con al menos una nota bajo 4.0 (Uso de Pandas).

import pandas as pd
from Datos import datos

def problema4():
    df_alumnos = pd.DataFrame(datos)

    # Marcar si cada alumno tiene al menos un rojo
    df_alumnos['tiene_rojo'] = df_alumnos['notas'].apply(lambda notas: any(nota < 4.0 for nota in notas))

    # Calcular porcentaje de alumnos con rojos
    porcentaje_rojos = (df_alumnos['tiene_rojo'].sum() / len(df_alumnos)) * 100

    print("------------- Estudiantes con al menos un rojo -------------")
    print(f"El {porcentaje_rojos:.1f}% de los estudiantes tiene al menos una nota bajo 4.0.")
