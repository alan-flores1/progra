from os import system
system ("cls")

auxi = 1
while auxi != 0:
    try :
        opc = int(input("Bienvenido al fakin menu.\n1-Nombre.\n2-Impuestos.\n3-Triangulos.\n4-Signos zodiacales\n0-Salir\n"))
    
        if opc < 0 or opc > 4 :
            print ("Ingreso valor fuera del rango ")
        
        if opc == 0 :
            auxi = 0 

    except: print ("Dato inválido ")

    if opc == 1 :
     cantcarac= 0
     nom= 0
     while nom==0 :
        try :
            nom=input("Ingrese un nombre ")
            for i in nom :
                cantcarac+=1

            if cantcarac < 4 or cantcarac > 20 :
                print ("Nombre fuera de rango ")
        except :
            print ("Dato invalido ")

        nom2=""
        for i in nom :
            if i == "o":
                nom2 +="i"
            else:
                nom2+=i
    
        print (f"{nom2}")
        

    if opc == 2 :
        aux1=0

        while aux1 == 0 :
            try :
              monto=int(input("Ingrese el monto"))
 
              if monto < 9000 or monto > 100000 :
                    print ("Fuera de rango")
              else:
                    aux1 = 1

            except:
                print ("Dato inválido")

        monto = monto * 1.19
        print (f"Su monto con el IVA agregado es de {monto}")
        opc = 0


    if opc == 3 :

        num=int(input("Ingrese un numero para la altur"))

        for i in range (num):
         print (' ' * (num - i - 1) + "*" * (2 * i + 1))
         
        



    if opc == 4 :
        aux2 = 0


        while aux2 == 0 :
            try:
                dia = int(input("Ingrese el dia de nacimiento"))
                if dia < 1 or dia > 31:
                 print ("Dia inválido")
                else :
                    aux2 = 1

            except :
                print ("Se ingresó un dato inválido")


        while aux2 == 1 :
            try:
                mes = int(input("Ingrese el numero del mes del nacimiento"))
                if mes < 1 or mes > 12:
                    print ("Mes invalido")
                else :
                    aux2 = 2

            except :
                print ("dato invalido")


        if mes == 1 and dia >= 20 or mes==2 and dia <= 18 :
            print ("Eres Acuario, hola")

        elif mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
            print ("Eres piscis, hola")

        elif mes == 3 and dia >= 21 or mes == 4 and dia <= 19:
            print ("Eres aries, hola")

        elif mes == 4 and dia >= 20 or mes == 5 and dia <= 20:
            print ("Eres Tauro, UN CRAK")

        elif mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
            print ("Eres Geminis, hola")

        elif mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
            print ("Eres cancer, hola")

        elif mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
            print ("Eres leo,como mi ex, te extraño Anto")

        elif mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
            print ("eres virgo,hola")

        elif mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
            print ("eres libra,hola")

        elif mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
            print ("eres escorpio")

        elif mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
            print("eres sagitario,hola")

        elif mes == 12 and dia >= 22 or mes == 1 and dia <= 19 :
            print("eres capricornio,hola")
        
        
            

