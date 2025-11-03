from os import system
from csv import reader
from json import dump
system ("cls")


lectura=open("datos.csv","r")
lectura_csv=reader(lectura)
 
mayores=[]
cont=0
for i in lectura_csv:
    if cont==0:
        print()
    else:
        if int(i[1])>=25:
            mayores.append(i)
    

print(mayores)