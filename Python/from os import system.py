from os import system
from csv import reader
from json import dump
system("cls")

lectura=open("documento.csv","r")
lectura_csv = reader(lectura)
pequenas = []
medianas = []
grandes= []

for i in lectura_csv: 
    print (i[2])