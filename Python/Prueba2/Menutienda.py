from os import system
system ("cls")

aux=0
totalapagar = 0
totalconiva = 0

while aux == 0 :
    opc=int(input("Bienvenido al menú de tienda!! ¿Que producto desea?\n1-Arroz:$3150\n2-Aceite:$1990\n3-Queso:$2150\n4-Leche:$1190\n5-Salir y pagar\n"))
 
    if opc == 1 :
        print("Se agregó arroz al carrito!")
        totalapagar=totalapagar+3150
    
    if opc == 2 :
        print("Se agregó aceite al carrito!")
        totalapagar=totalapagar+1990
    
    if opc == 3 :
        print ("Se agregó queso al carrito!")
        totalapagar=totalapagar+2150
    
    if opc == 4 :
        print ("Se agregó leche al carrito!")
        totalapagar=totalapagar+1190
    
    if opc == 5 :
        totalconiva = totalapagar*1.19
        print("El total de su compra es : $",round(totalconiva))
        aux = 1