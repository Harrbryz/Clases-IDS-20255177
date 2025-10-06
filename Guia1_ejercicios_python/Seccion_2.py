#Pide al usuario su nombre usando input() y muéstrale un saludo personalizado.
nombre_usuario = input("Ingresa tu nombre: ")
print("Hola", nombre_usuario, "Pasa un feliz dia")
#Pide al usuario su edad y muestra un mensaje con el doble de esa edad. 
edad_usuario = int(input("ingresa tu edad: "))
doble_edad = edad_usuario * 2
print("El doble de tu edad es:", doble_edad)
#Pide dos números enteros al usuario, súmalos y muestra el resultado.
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
suma_de_ambos = num1+num2
print(f"La suma de ambos numeros es: {suma_de_ambos}")
#Pide al usuario un número decimal y muestra su mitad.
num_decimal = float(input("Ingresa tu numero decimal: "))
mitad_num_decimal = num_decimal / 2
print("La mitad de tu numero decimal es:", mitad_num_decimal)
#Pide al usuario su año de nacimiento y calcula su edad (usando 2025 como año actual)
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = 2025
edad_aproximada = año_actual - año_nacimiento
print("Tu edad aproximada es:", edad_aproximada)
#Pide al usuario el precio de un producto y el número de unidades. Muestra el total a pagar.
precio_producto = float(input("Ingrese el precio de los productos: "))
unidades_producto = int(input("Ingrese la cantidad de productos "))
precio_a_pagar = precio_producto * unidades_producto
print(f"El precio total a pagar es de: $ {precio_a_pagar:.2f}")
#Pide al usuario un número entero y muestra el cuadrado de ese número
numero_entero = int(input("Ingrese el numero entero al que le sacara el cuadrado "))
num_al_cuadrado = numero_entero * numero_entero
print("El numero al cuadrado es:", num_al_cuadrado)
#Pide al usuario dos números y muestra su promedio
numero1promedio = float(input("Ingrese el primer numero para sacar su promedio: "))
numero2promedio = float(input("Ingrese el segundo numero para sacar su promedio: "))
promedio = (numero1promedio + numero2promedio) / 2
print("El promedio de ambos numeros es:", promedio)
#Pide al usuario su nombre completo y su edad, y muestra un mensaje con formato fstring como: Hola, Juan Pérez. Tienes 20 años
nombre_completo = input("Ingrese su nombre completo: ")
edad_usuario = int(input("Ingrese su edad: "))
print(f"Hola, {nombre_completo} Tienes {edad_usuario} años.")
