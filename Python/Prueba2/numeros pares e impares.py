from os import system
system ("cls")

cantpares=0
cantimpares=0


num=int(input("Bienvenido, por favor ingrese un número entero positivo:\n"))
rango = int (input("Desea contar su numero en el rango?\n1-Si\n2-No\n"))

if rango == 1:

    for i in range (1,(num+1)) :
     
     if i % 2 == 0 :
        cantpares=cantpares+1
     else:
        cantimpares=cantimpares+1

if rango == 2 :

    for i in range (1,num):
    
     if i % 2 == 0 :
        cantpares=cantpares+1
     else:
        cantimpares=cantimpares+1
    
print (f"La cantidad de numeros pares en el rango de 1 hasta su numero es de: {cantpares} y la cantidad de impares es: {cantimpares}")