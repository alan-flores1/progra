def validarnum(min,max,texto):
    while True:
        try:
            num=int(input(f"{texto} (Entre {min} y {max})\n"))
            if num < min or num > max:
                print("Fuera de rango!")
            else:
                return num
        except ValueError:
            print("Tipo de dato erroneo!")

def mostrar(lista):
    for i in lista:
        try:
            print(i)
        except:
            print(i)

def reserva (lista):
    fila=validarnum(1,6,"Ingrese fila del asiento a reservar")
    columna=validarnum(1,12,"Ingrese columna del asiento a reservar ")
    lista[fila-1][columna-1]="X"

def anular (lista):
    fila=validarnum("Ingrese fila del asiento a anular")
    columna=validarnum("Ingrese columna del asiento a anular")
    if lista[fila-1][columna-1] == "X":
        print("Anulado exitosamente!")
        lista[fila-1][columna-1]=0
    else:
        print("Este asiento no está reservado, intente denuevo")

def calcular (lista):
    cont=0
    fila=1
    for i in lista:
        for j in i:
            if type(j) == type(int()):
                pass
            else:
                if fila > 2:
                    cont+=1500
                else:
                    cont+=6000
        fila += 1
    
    return cont
