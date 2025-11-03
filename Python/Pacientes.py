import csv
import json
from os import system
system ("cls")

lista=[]
res = ""
ar = []

while res != "no":
    paciente = []
    rut = input("Ingrese el rut del paciente: ")
    nom = input("Ingrese el nombre del paciente: ")
    fecha = input("Ingrese fecha de nacimiento del paciente: ")
    dolencia = input("Ingrese la dolencia del paciente: ")
    paciente.append(rut)
    paciente.append(nom)
    paciente.append(fecha)
    paciente.append(dolencia)
    lista.append(paciente)
    res=input("Desea ingresar otro paciente? (si/no): ")
    if res.lower() == "no" :
        break

for i in lista:
    ar.append({"Rut":i[0],"Nombre":i[1],"Fecha de nacimiento":i[2],"Dolencia":i[3]})

try:
    open("pacientes.json","x")
except:
    print("documento ya creado")

dic={"Pacientes:":ar}
with open("pacientes.json","w") as file:
    json.dump(dic,file,ensure_ascii=False, indent=4)