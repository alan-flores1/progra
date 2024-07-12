import random
import csv
import math
from os import system
system("cls")
from funcionesexamen import *
trabajadores=[ 

    {"nombre": "Juan Perez", "cargo": "Consultor TI"}, 

    {"nombre": "Maria Garcia", "cargo": "Analista"}, 

    {"nombre": "Carlos Lopez", "cargo": "Programador"}, 

    {"nombre": "Ana Martinez", "cargo": "Jefe de Proyecto"}, 

    {"nombre": "Pedro Rodriguez", "cargo": "Consultor TI"}, 

    {"nombre": "Laura Hernandez", "cargo": "Analista"}, 

    {"nombre": "Miguel Sanchez", "cargo": "Programador"}, 

    {"nombre": "Isabel Gomez", "cargo": "Jefe de Proyecto"}, 

    {"nombre": "Francisco Diaz", "cargo": "Consultor TI"}, 

    {"nombre": "Elena Fernandez", "cargo": "Analista"} 

]


sueldos=[]

aux=True
while aux == True:
    opc=int(input("Ingresar opción\n1-Asignar sueldos aleatorios.\n2-Clasificar sueldos.\n3-Ver estadísticas.\n4-Generar reporte de sueldos.\n5-Salir\n--->"))
    if opc == 1:
        print()
        asignar_sueldo(trabajadores)

    elif opc == 2:
        print()
        clasif_sueldo(trabajadores)
        
    elif opc == 3:
        print()
        estadisticas(trabajadores)
        
    elif opc == 4:
        print()
        reporte(trabajadores)
    
    elif opc == 5:
        print("chaooo")
        break