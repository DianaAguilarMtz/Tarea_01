#Autor: Diana Patricia Aguilar Martínez
#Descripción: este programa pregunta al usuario su edad en años y meses enteros e imprime el número aproximado de días que ha vivido.

años=int(input("¿cuantos años enteros has vivido?"))
mes=int(input("contando desde tu ultimo cumpleaños ¿cuantos meses enteros has vivido? "))
ab= int(input("¿cuantos años bisiestos has presenciado?"))

dias= (años*365) + (mes*30)

DV= dias + 5 + ab

print("usted ha vivido  un aproximado de", DV , "dias")