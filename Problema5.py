#[5] Listado ordenado (de mayor a menor) de los estudiantes según su promedio.")

import pandas as pd 

from Datos import datos #importa lista de diccionarios 

def problema5(): 
    df_alumnos=pd.DataFrame(datos)
    df_alumnos['promedio'] = df_alumnos['notas'].apply(lambda notas : sum(notas) / len (notas) )
    def_ordenado = df_alumno[['nombre', 'promedio']].sort_values(by='promedio', ascending=False )

    print("------------- Listado de estudiantes según promedio ----------------")
    print(df_ordenado.round(1).to_string(index=False))


