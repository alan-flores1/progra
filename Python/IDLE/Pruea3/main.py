from os import system
from csv import writer,reader
from func import *

cont=0
asientos=[
    [],
    [],
    [],
    [],
    [],
    []
    ]

for i in asientos:
    for j in range(12):
        i.append(cont)


for i in asientos:
    print(i)

aux=True
while aux == True:
    print("1-Mostrar lista.\n2-Reservar.\n3-Anular reserva.\n4-Calcular ganancias.\n5-Salir")
    opc=validarnum(1,5,"Ingrese opción")
    if opc==1:
        print()
        mostrar(asientos)
        print()
    elif opc == 2:
        reserva(asientos)
        print()
    elif opc == 3:
        anular(asientos)
        print()
    elif opc == 4:
        print(f"Las ganancias de hoy son de: {calcular(asientos)}")
    elif opc == 5:
        aux=False


try:
    open("Estacionamientos.csv","x")
except:
    print("Existe ya!!")

ingresos=calcular(asientos)
escritura=open("Estacionamientos.csv","w",newline="")
escritura2=writer(escritura)
escritura2.writerow(["Lista de asientos:"])
escritura2.writerows(asientos)
escritura2.writerow([f"\nLos ingresos de hoy son: {ingresos}"])



