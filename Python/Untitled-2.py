def division(a,b):
 aux=True
 while aux == True:
    try:
        if a == 0 or b == 0:
           print("no se puede dividir por 0")
           a=float(input("ingrese 1er num"))
           b=float(input("ingrese 2do num"))
        else:
           resultado=a/b
           return resultado
    except ValueError:
       print ("error con los tipos de datos")

num1=float(input("ingrese 1er num"))
num2=float(input("ingrese 2do num"))


ejercicio=division(num1,num2)
print(ejercicio)

