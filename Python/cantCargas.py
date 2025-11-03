from os import system
system ("cls")

cargasliv = 0
cargasmed = 0
total = 0
cantcargas = 0

while cantcargas == 0 :
   try :
      cantcargas =int (input("Bienvenido ¿cuantas cargas desea transportar?"))
      
   except :
    print ("Ingresó un dato inválido")
   
   
for i in range (cantcargas) :
 pesocarga = 0
 while pesocarga == 0 :
    try :
       pesocarga = int (input("Cuanto pesa la carga?"))
       if pesocarga < 1 or pesocarga > 10 :
          print ("El valor debe estar entr 1-5 o 6-10")
    except :
       print ("Ingresó un dato inválido")

 if pesocarga >= 1 and pesocarga <= 5 :
   cargasliv = cargasliv + 1
   total = total + 1000

 if pesocarga >= 6 and pesocarga <= 10 :
   cargasmed = cargasmed + 1
   total = total + 2000

print (f"Cargas livianas: {cargasliv}\nCargas medianas: {cargasmed}\nValor a pagar: ${total}")