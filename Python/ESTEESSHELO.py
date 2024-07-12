import random
import csv
import math
trabajadores=[ 

    {"nombre": "Juan Pérez", "cargo": "Consultor TI"}, 

    {"nombre": "María García", "cargo": "Analista"}, 

    {"nombre": "Carlos López", "cargo": "Programador"}, 

    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"}, 

    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"}, 

    {"nombre": "Laura Hernández", "cargo": "Analista"}, 

    {"nombre": "Miguel Sánchez", "cargo": "Programador"}, 

    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"}, 

    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"}, 

    {"nombre": "Elena Fernández", "cargo": "Analista"} 

]

men=[]
entre=[]
sup=[]
sueldos=[]

aux=True
while aux == True:
    opc=int(input("Ingresar opción\n1-Asignar sueldos aleatorios.\n2-Clasificar sueldos.\n3-Ver estadísticas.\n4-Generar reporte de sueldos.\n--->"))
    if opc == 1:
        for i in trabajadores:
            i["sueldo"] = random.randint(300000,2500000)

    elif opc == 2:
        print()
        for i in trabajadores:
            if i["sueldo"]<800000:
                men.append(i)
            elif i["sueldo"]>=800000 or i["sueldo"]<=2000000:
                entre.append(i)
            else:
                sup.append(i)

        cont=0
        for a in trabajadores:
            cont+=a["sueldo"]

            
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
        
    elif opc == 3:
        sueldos=[]
        for j in trabajadores:
            sueldos.append(i["sueldo"])
        print(f"El mayor sueldo es {max(sueldos)}")
        print(f"El menor sueldo es {min(sueldos)}")
        print(f"el promedio de sueldos es:{sum(sueldos)/len(sueldos)}")
        sueldo_geom=math.exp(sum(math.log(sueldo)for sueldo in sueldos)/len(sueldos))
        print(f"La media geometrica es {sueldo_geom}")
        
    elif opc == 4:
        print("Nombres           Cargo       Sueldo            Dcto salud            Dcto afp            Sueldo liquido")
        for j in range(len(trabajadores)):
                print(f"{trabajadores[j]["nombre"]}",end="   ")
                print(f"{trabajadores[j]["cargo"]}",end="    ")
                print(f"${trabajadores[j]["sueldo"]}",end="    ")
                print(f"Dcto salud: ${round(trabajadores[j]["sueldo"]*0.07)}",end="        ")
                print(f"Dcto afp: ${round(trabajadores[j]["sueldo"]*0.12)}",end="        ")
                afp=round(trabajadores[j]["sueldo"]*0.12)
                salud=round(trabajadores[j]["sueldo"]*0.07)
                sueldo_liquido=round(trabajadores[j]["sueldo"]-afp-salud)
                print(f"Sueldo liquido: ${sueldo_liquido}",end="\n")
        try:
            open("examenfalso.csv","x")
        except:
            print("Ya hecho!")

        with open("examenfalso.csv","w",newline="") as archivo_csv:
            escritor_csv=csv.writer(archivo_csv)
            for i in range(10):
                escritor_csv.writerows([i["nombre"],i["cargo"],i["sueldo"],afp,salud,sueldo_liquido])
    
