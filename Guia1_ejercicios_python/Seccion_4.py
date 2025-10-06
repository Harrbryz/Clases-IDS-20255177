#Crea tres variables (nombre, producto, precio) y muestra el mensaje: Hola Ana, el producto Laptop cuesta $1200.00 usando una f-string.
nombre = "Ana"
producto = "Laptop"
precio = 1200.00
print(f"Hola {nombre}, el producto {producto} cuesta ${precio}")
#Pide el nombre y el país de un usuario y muestra: Hola, Carlos de El Salvador, ¡bienvenido!
nombreusuario = input("Ingrese su nombre: ")
paisusuario = input("Ingrese su pais: ")
print(f"Hola, {nombreusuario} de {paisusuario}, ¡bienvenido!")
# Crea un mini formulario que pida nombre, edad y ciudad, y luego muestre un resumen de la información en varias líneas usando f-strings
nombre_usuario = input("Ingrese su nombre: ")
edad_usuario = int(input("Ingrese su edad: "))
ciudad_usuario = input("Ingrese su ciudad: ")
print(f"""Nombre: {nombre_usuario}
      edad: {edad_usuario}
      ciudad: {ciudad_usuario}""")
#Muestra el área de un rectángulo con base y altura dadas por el usuario. El resultado debe aparecer con dos decimales.
base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
area_rectangulo = base * altura
print(f"El area del rectangulo es de:  {area_rectangulo:.2}")
#Muestra una tabla como esta: Producto: Pan, Precio: $1.50, Cantidad: 4, Total: $6.00 (Usa variables y f-strings)
producto2 = "Pan"
precio2 = 1.50
cantidad2 = 4
total2 = precio2 * cantidad2
print(f"Producto: {producto2}, Precio: ${precio2}, Cantidad: {cantidad2}, Total: ${total2:.2}")