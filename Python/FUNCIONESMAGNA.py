import random
import math

def asignar_sueldo(lista):
    for i in lista:
        i["sueldo"] = random.randint(300000,2500000)

def clasif_sueldo(lista):
    men=[]
    entre=[]
    sup=[]

    for i in lista:
            if i["sueldo"]<800000:
                men.append(i)
            elif i["sueldo"]>=800000 and i["sueldo"]<=2000000:
                entre.append(i)
            else:
                sup.append(i)
    cont=0

    try:
        for a in lista:
            cont+=a["sueldo"]
    except:
         print("Aún no se asignan los sueldos!")
            
    if len(men)==0:
        pass
    else:
        print(f"Sueldos menores a $800000 Total:{len(men)}\nNombre empleado     cargo       sueldo")
        for j in range(len(men)):
            print(f"{men[j]["nombre"]}",end="   ")
            print(f"{men[j]["cargo"]}",end="    ")
            print(f"${men[j]["sueldo"]}",end="\n")
        
    print()
    if len(entre)==0:
        pass
    else:
        print(f"Sueldos entre $800000 y $2500000 Total:{len(entre)}\nNombre empleado     cargo       sueldo")
        for j in range(len(entre)):
            print(f"{entre[j]["nombre"]}",end="   ")
            print(f"{entre[j]["cargo"]}",end="    ")
            print(f"${entre[j]["sueldo"]}",end="\n")
        
    print()
    if len(sup)==0:
        pass
    else:
        print(f"Sueldos mayores a $2500000 Total:{len(sup)}\nNombre empleado     cargo       sueldo")
        
        for j in range(len(sup)):
            print(f"{sup[j]["nombre"]}",end="   ")
            print(f"{sup[j]["cargo"]}",end="    ")
            print(f"${sup[j]["sueldo"]}",end="\n")
        
    print(f"Total de sueldos: ${cont}")
    print()

def estadisticas(lista):
    sueldos=[]
    for j in lista:
        sueldos.append(j["sueldo"])

    print(f"El mayor sueldo es {max(sueldos)}")
    print(f"El menor sueldo es {min(sueldos)}")
    print(f"el promedio de sueldos es:{sum(sueldos)/len(sueldos)}")

    sueldo_geom=math.exp(sum(math.log(sueldo)for sueldo in sueldos)/len(sueldos))

    print(f"La media geometrica es {sueldo_geom}")
    print()

def reporte(lista):
    import csv
    for j in range(len(lista)):
                print(f"{lista[j]["nombre"]}",end="   ")
                print(f"{lista[j]["cargo"]}",end="    ")
                print(f"${lista[j]["sueldo"]}",end="    ")
                print(f"Dcto salud: ${round(lista[j]["sueldo"]*0.07)}",end="        ")
                print(f"Dcto afp: ${round(lista[j]["sueldo"]*0.12)}",end="        ")

                afp=round(lista[j]["sueldo"]*0.12)
                salud=round(lista[j]["sueldo"]*0.07)
                sueldo_liquido=round(lista[j]["sueldo"]-afp-salud)

                print(f"Sueldo liquido: ${sueldo_liquido}",end="\n")

    print()
    
    try:
        open("examenfalso.csv","x")
    except:
        print("Ya hecho!")

    

    with open("examenfalso.csv","w",newline="") as archivo_csv:
        escritura=csv.writer(archivo_csv)
        escritura.writerow(["Nombre empleado", "Cargo", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        
        for k in lista:
            nombre=k["nombre"]
            cargo=k["cargo"]
            sueldo_base=k["sueldo"]
            dcto_salud=round(sueldo_base*0.07)
            dcto_afp=round(sueldo_base*0.12)
            liquido=sueldo_base-dcto_afp-dcto_salud

            escritura.writerow([nombre,"    ", cargo,"  ", sueldo_base,"  ", dcto_salud,"   ", dcto_afp,liquido])