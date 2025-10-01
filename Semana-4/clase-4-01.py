usuario = "Harry" #tipo string es decir de tipo texto
cantidad_harrys = 74 #tipo int es decir numero entero
media_harrys = 18.4 #tipo float es decir numero con decimales
#vemos los tipos de datos
print(type(usuario))
print(type(cantidad_harrys))
print(type(media_harrys))
#comprobamos si el tipo de dato es el que esperamos
print(type(cantidad_harrys) is int)
print(type(media_harrys) is int)
print(type(media_harrys) is float)
montohope=1234.56656
#meter formato al texto
print(f"El usuario es {usuario}")
print(f"colecto {montohope:,.2f}")
#Valores absolutos
print(abs(-56))
#Redondeo
print(round(3.1416,2))
#Conversiones