def numInt (min,max,texto):
    aux=True
    while aux == True:
        try:
            a=int(input(f"Ingrese {texto}: "))
            if  a < min or a > max:
                print("Fuera de rango!")
            else:
                return a
        except ValueError:
            print("datos erroneos")
            a=int(input(f"Ingrese {texto}: "))
    

def texto (min,max,texto):
    while True:
        a=input(f"Ingrese {texto}: ")
        if len(a) < min or len(a) > max:
            print("Fuera de rango!")
        else:
            return a

def registrar (lista):
    nom=texto(3,15,"Nombre").capitalize() 
    ape=texto(3,15,"Apellido").capitalize()
    t_cargo=numInt(1,3,"su cargo:\n1-Ceo\n2-Analista\n3-Desarrollador\n")
    cargo=""
    if t_cargo == 1:
        cargo="Ceo"
    if t_cargo == 2:
        cargo="Analista"
    if t_cargo == 3:
        cargo="Desarrollador"
    sueldo=numInt(100000,3000000,"Sueldo")
    aux=[nom,ape,cargo,sueldo]
    lista.append(aux)
    return "se ingreso correctamente!"


def mostrar(lista):
    cont=1
    for i in lista:
        print(cont,"-",i[0],"",i[1],"",i[2],"",i[3])
        cont+=1

def tablilla(lista):
    print("     Nombre     Apellido     Cargo            Sueldo")
    for i in lista:
        print(f"     {i[0]}      {i[1]}        {i[2]}        {i[3]}")                 

def guardar (lista):
    string=""
    for i in lista:
        string += i[0]+"  "+i[1]+"  "+i[2]+"  "+str(i[3])+"\n"
    try:
        open("Trabajadores.txt","x")
    except:
        print("En proceso")

    w=open("Trabajadores.txt","w")
    w.write(string)
    w.close()
