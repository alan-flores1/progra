from os import system
system ("cls")

nota=int(input("Ingrese su nota:\n"))

if nota >= 65 :
    print ("Su calificacion es : A, felicidades!")

if nota <= 64 and nota >= 50 :
    print ("Su calificacion es : B, felicidades")

if nota <= 49 and nota >= 40 :
    print ("Su calificacion es: C, la siguiente será mejor!")

if nota <= 39 and nota >= 30 :
    print ("Su calificacion es : D, ánimo a la próxima!")

if nota <= 29 :
    print ("Su calificación es : F")