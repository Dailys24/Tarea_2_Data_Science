#Main.py

#Tarea 2 Data Science

import pandas as pd
import os
from Datos import datos
from Problema1 import problema1
from Problema2 import problema2
from Problema3 import problema3
from Problema4 import problema4
from Problema5 import problema5

# unción principal que contiene el menú
def main():
    while True:
        #Limpiar la pantalla de la consola
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #Menú del programa
        print("****************************************************************************************")
        print("\n-----Tarea 2 Fundamentos de Data Science-----\n")
        print("------------- MENU -------------")
        print("\n\u27a4 [1] Calcuar el promedio de notas y promedio mas alto y bajo.")
        print("\n\u27a4 [2] Filtrar estudiantes que aprobaron (promedio >= 4.0).")
        print("\n\u27a4 [3] Nota mas frecuente (moda) considerando todas las notas de todos los estudiantes.")
        print("\n\u27a4 [4] Porcentaje de estudiantes con al menos una nota bajo 4.0.")
        print("\n\u27a4 [5] Listado ordenado (de mayor a menor) de los estudiantes según su promedio.")
        print("\n\u27a4 [6] Terminar")
        print("\n****************************************************************************************")

        try:
            op = int(input("\nIngrese una opcion: "))
            
            if op < 1 or op > 6:
                print("\n*** Opcion invalida. Porfavor digite nuevamente ***\n")
                input("Presione Enter para continuar...")
                continue #Vuelve al inicio del bucle
            
            #Switch-case en Python (usamos un diccionario o if/elif/else)
            if op == 1:
                print("------------------------------------------------------------------------------------")
                problema1() #Llamamos a la función del problema 1
                print("------------------------------------------------------------------------------------")
            
            elif op == 2:
                print("------------------------------------------------------------------------------------")
                problema2() #Llamamos a la función del problema 2
                print("------------------------------------------------------------------------------------")
            elif op == 3:
                print("------------------------------------------------------------------------------------")
                problema3() #Llamamos a la función del problema 3
                print("------------------------------------------------------------------------------------")
            elif op == 4:
                print("------------------------------------------------------------------------------------")
                problema4() #Llamamos a la función del problema 4
                print("------------------------------------------------------------------------------------")
            
            elif op == 5:
                print("------------------------------------------------------------------------------------")
                problema5() #Llamamos a la función del problema 5
                print("------------------------------------------------------------------------------------")
            
            elif op == 6:
                print("\n****Gracias por utilizar****")
                break

            while True:
                opcion = input("\n\u27a4¿Desea Realizar otra operacion? (Y=si/N=no): ").upper()
                if opcion == 'N':
                    print("\n****Gracias por utilizar****")
                    return
                elif opcion == 'Y':
                    break
                else:
                    print("Operacion invalida.")

        except ValueError:
            print("\n*** Opcion invalida. Porfavor digite un numero ***\n")
            input("Presione Enter para continuar...")

#Ejecutamos la función principal
if __name__ == "__main__":
    main()
