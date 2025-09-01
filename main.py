#Tarea 2 Data Science

import pandas as pd

#Calcular promedio de notas de cada alumno y promedio general del curso
datos = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofia", "notas": [3.9, 4.0, 4.5]},
    {"nombre": "Francisca", "notas": [6.9, 6.8, 7.0]},
    {"nombre": "Maria", "notas": [5.5, 6.0, 5.9]},
    {"nombre": "Carlos", "notas": [4.0, 4.5, 3.8]},
    {"nombre": "Laura", "notas": [6.2, 6.5, 6.8]},
    {"nombre": "Javier", "notas": [5.0, 5.2, 5.4]},
    {"nombre": "Elena", "notas": [3.5, 4.0, 4.1]},
    {"nombre": "Diego", "notas": [2.0, 2.5, 3.2]},
    {"nombre": "Angelo", "notas": [7.0, 6.1, 6.3]},
    {"nombre": "Andres", "notas": [4.5, 4.2, 3.9]},
    {"nombre": "Valeria", "notas": [1.8, 4.7, 2.0]},
    {"nombre": "Juan", "notas": [5.1, 5.3, 5.0]},
    {"nombre": "Gabriela", "notas": [4.0, 4.3, 3.7]},
    {"nombre": "Nicolas Rosale", "notas": [5.0, 3.0, 4.0]},
    {"nombre": "Paula", "notas": [6.0, 6.5, 6.2]},
    {"nombre": "Ricardo", "notas": [4.8, 4.9, 5.1]},
    {"nombre": "Fernanda", "notas": [5.8, 2.3, 4.2]},
    {"nombre": "Jorge", "notas": [5.6, 5.5, 5.8]},
    {"nombre": "Natalia", "notas": [3.6, 4.0, 3.5]},
    {"nombre": "Hugo", "notas": [6.1, 3.2, 6.0]},
    {"nombre": "Camila", "notas": [6.4, 6.0, 6.5]},
    {"nombre": "Roberto", "notas": [5.2, 5.0, 5.3]},
    {"nombre": "Matia Lope", "notas": [4.1, 4.2, 4.0]},
    {"nombre": "Manuel", "notas": [5.8, 2.3, 4.2]}, 
    {"nombre": "Silvia", "notas": [6.7, 6.9, 7.0]},
    {"nombre": "Felipe", "notas": [5.3, 5.5, 5.2]},
    {"nombre": "Adriana", "notas": [3.8, 4.1, 3.9]},
    {"nombre": "Benjamin", "notas": [6.1, 3.2, 6.0]},
    {"nombre": "Lucia", "notas": [6.1, 6.3, 6.0]},
    {"nombre": "Victor", "notas": [4.9, 5.0, 4.8]},
    {"nombre": "Carolina", "notas": [4.9, 5.0, 4.8]}, 
]

df_alumnos = pd.DataFrame(datos)

promedio_notas=sum(notas)/len(notas)

print(df_alumnos ["nombre"])
print("----------------------------------------------")
