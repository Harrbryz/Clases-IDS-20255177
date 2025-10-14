nombre = "Harry" #Se almacena esta informacion ya sea texto int booleano o float para asi reutilizar o modificiar despues
print(nombre)
#Cuando se crea un objeto se considera toda su informacion es decir tiene un tipo de dato y una estructura
#Entero, boleano, flotante, etc.
#Tambien existen las estructuras de datos, las cuales se dividen en 5
#String, Lista, Tupla, Diccionario, Matriz, Dataframe
#String: En un solo paquete van varios componentes es decir al crear el nombre con una palabra se constituyen como un solo objeto, es decir "quiero la primera letra, la segunda, etc."
x = "Hola" #Esto es un string
y = [1, x, 3, 4] #Esto es una lista
#Los string van los elementos en orden es decir cuando se dan  print se da la secuencia en la que este fue ingresado
print(x[0:]) #Cuando queremos que sea desde un numero, hasta el final va x: sin ningun numero despues porque esta abierto y llega hasta el final
print(x[-2:])
#si queremos que salte entre algunos caracteres, es 2:5:2 con un salto de 2 el cual es el final
print(x[0:3:1])
print(x[-2:])
palindromo = "reconocer"
print(palindromo[0:4]) #El rango en realidad es como si fuera un intervalo pero con [x,x)
print(palindromo[::-1]) # Con esto podemos construir palabras inversas para demostrar si es un palindromo o no
Palabra = input("Deme una palabra: ").lower() #Con lower se puede haceer minuscula
print(Palabra)
Palabra2 = "ratón"
print(Palabra2[::-1])

reconocer_palindromo = input("Ingrese una palabra para ver si es un palindromo: ").lower()
inverso = reconocer_palindromo[::-1]
if reconocer_palindromo == inverso:
    print("Es un palindromo")
else:
    print("No es un palindromo")
print(Palabra==Palabra[::-1])
#Programa para reconcoer palindromos
#Los espacios tzmbien cuentan como caracteres en un string
#Inicio_Fin:Salto ::
#Un string es una cadena de caracteres al momento del que lo estoy creando
#Por medio del . despues de un objeto lo podemos mostrar o cambiar para que tenga otra propiedad por ejemplo.lower()
#Las tuplas son los objetos que tienen la capacidad de organizar y recolectar datos
#son recolectados por medio de parentesis ()
tupla1 = (17, 18, 19, 19, 18, 19)
print(tupla1[4]) #Las tuplas son inmutables, no se le pueden quitar ni agregar valores, ni cambiar
#Las tuplas sirven cuando yo estoy haciendo un archivo y quiero proteger algunos valores entonces se crea una tupla para que no varie.
lista1 = [17, 18, 19, 19, 18, 19] #Las listas se pueden modificar, estas se crean con []. 
lista1[4] = 17 # se le puede cambiar un componente al componente 5 por ejemplo
#Una lista y una tupla tienen la capacidad de mostrar el largo de los que estan integrados
print(len(tupla1))
print(len(lista1))
