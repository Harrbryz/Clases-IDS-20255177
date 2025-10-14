#ENERO FEBRERO Y MARZO
#COSTO EN ENERO 1.25
#FEBRERO 1.38
#MARZO 1.14
#recibir los valores que no conozco de los tres inputs
enerocosto = 1.25
febrerocosto = 1.38
marzocosto = 1.14
enero = int(input("Ingrese la cantidad de enero: "))
febrero = int(input("Ingrese la cantidad de febrero: "))
marzo = int(input("Ingrese la cantidad de marzo: "))
costotal = (enero * enerocosto) + (febrero * febrerocosto) + (marzo * marzocosto)
print(f"El costo total de los tres meses fue de: {costotal:.2f}")
