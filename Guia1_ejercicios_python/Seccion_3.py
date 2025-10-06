#Crea tres variables: a = 10, b = 3, c = 5. Calcula y muestra: la suma de a y b, el resultado de a dividido entre b, el residuo de dividir a entre c
a = 10
b = 3
c = 5
suma_a_b = a+b
division_a_b = a/b
a_residuo_c = a%c
print("La suma de a y b es:", suma_a_b)
print("El resultado de a dividido entre b es:", division_a_b)
print("El residuo de dividir a entre c es:", a_residuo_c)
#Crea dos variables x = 10, y = 10. Usa los operadores is e is not para verificar si apuntan al mismo objeto en memoria
x = 10
y = 10
print(x is y)
print(x is not y)
#Pide un número al usuario y muestra True si es par, False si es impar (usa el operador %).
num_usuario = int(input("Ingrese un numero: "))
if num_usuario % 2 == 0:
    print("El numero es par")
elif num_usuario % 2 != 0:
    print("El numero es impar")
#Crea una variable booleana registrado = True. Usa operadores lógicos (and, or, not) para mostrar combinaciones posibles.
registrado = True
noregistrado = False
if registrado is False:
     print("Registrado es True")
elif registrado is True and noregistrado is not True:
    print(f"Registrado es: {registrado}")
    print(f"No registrado es: {noregistrado}")
#Pide al usuario dos números y muestra si el primero es mayor o igual que el segundo
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
if num1 >= num2:
    print(num1, "Es mayor o igual que: ", num2)
else:
    print(num1, "No es mayor ni igual que: ", num2)
#Pide al usuario su edad y muestra si tiene edad suficiente para votar (mayor o igual que 18).
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Usted tiene edad suficiente para votar")
else:
    print("Salga de aqui niño")
#Crea un ejemplo que combine operadores relacionales y lógicos, como: edad = 22; estudiante = True; print(edad >= 18 and estudiante).
cantidad_cervezas = int(input("Ingrese la cantidad de cervezas que se toma semanalmente: "))
print("Si usted es borracho se mostrara True, si no False ", cantidad_cervezas >= 10 )