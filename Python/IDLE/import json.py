import json
import csv
from aaa import *




personas={
    "nombre":[],
    "edad":[],
    "comuna":[]
    }
nombre=[]
edad=[]
comuna=[]
mayores=[]


aux=True
while aux:
    nombre.append(input("ingrese nombre: "))
    edad.append(val_num(0,100,"edad"))
    comuna.append(input("ingrese comuna: "))
    r=input("quieres agregar otra persona: ").lower()
    if r=="no":
        aux=False
        personas["nombre"].append(nombre)
        personas["edad"].append(edad)
        personas["comuna"].append(comuna)
        mayores.append(nombre)
        for i in edad:
            if i>=25:
                mayores.append(i)
            else:
                print()
    else:
        print()

try:
    open("datos.csv","x")

except:
    print("ya existe")

escritura=open("datos.csv","w",newline="")
escrituranueva=csv.writer(escritura)
escrituranueva.writerow(personas)

