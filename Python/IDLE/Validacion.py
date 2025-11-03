def val_num(mini,maxi,texto):
    aux=True
    while aux:
            try:
                num=int(input(f"Ingrese {texto}: "))
                if num<mini or num>maxi:
                    print(f"Error en el rango {mini}{maxi}")
                else:
                    return num
            except:
                print(f"Error fuera de rango: {mini}{maxi}")
