from os import system
system("cls")
import json

personas= {
    "nombres":[],
    "comunas":[],
    "edad":[]
}

aux=True
while aux == True:

    for i in personas:
        cosa=input(F"ingrese {i} ")
        personas[i].append(cosa)

    respuesta=(input("¿Quiere agregar a alguien más? "))
    
    if respuesta.lower() == "no":
        aux=False

    



print(personas)
with open("lienzo.json","w") as pico:
    json.dump(personas,pico,indent=4)