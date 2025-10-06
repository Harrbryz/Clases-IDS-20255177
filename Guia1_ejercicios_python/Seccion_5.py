#Crea una variable palabra = 'Python' y muestra: la primera letra, las tres primeras letras, las dos últimas letras
palabra = "Python"
print(f"""La primera letra es: {palabra[0]}
      las tres primeras letras son: {palabra[0:3]}
      las dos ultimas letras son: {palabra[-2:]}""")
#Crea una variable frase = 'Aprender Python es divertido' y muestra la palabra 'Python' usando slicing.
frase = "Aprender Python es divertido"
print(frase[9:15])
#Pide al usuario una palabra y muestra cuántas letras tiene
frase_usuario = input("Inserte una palabra y le dire cuantos caracteres tiene: ")
print(f"La palabra que inserto tiene: {len(frase_usuario)}")
#Pide al usuario una palabra y muestra su primera y última letra.
palabra_usuario = input("Inserte una palabra y le mostrare su primera letra y ultima letra: ")
print(f"Su primera letra es: {palabra_usuario[0]}")
print(f"La ultima letra de su palabra es: {palabra_usuario[-1]}")
#Crea una variable codigo = 'ABC1234XYZ' y muestra solo la parte numérica usando slice
codigo = "ABC1234XYZ"
print(codigo[3:7])
#Crea una variable nombre = 'Juan Pérez' y muestra el apellido usando slice (es decir, utilizando []).
nombre = "Juan Pérez"
print(nombre[5:10])
