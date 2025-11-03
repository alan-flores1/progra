from os import system
system ("cls")

edad=0

while edad <10 or edad > 80 :
    try :
        edad=int(input("Por favor,ingrese su edad:\n"))
        if edad < 10 or edad > 80 :
            print ("Esta fuera del rango permitido (10-80), por favor ingrese su edad otra vez\n")
    except:
        print ("Ingresó un dato inválido!\n")


print ("Gracias por ingresar su edad, adiós")