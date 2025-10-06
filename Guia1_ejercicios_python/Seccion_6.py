#Crea una variable frase = 'La programación es poderosa'. Muestra un mensaje si lapalabra 'poderosa' está dentro de la frase. 
frase = "La programación es poderosa"
print("poderosa" in frase)
#Usa el operador not in para verificar si 'Java' no aparece en la frase anterior.
print("Java" not in frase)
#Crea una variable palabra = 'hola' y muestra esa palabra repetida 5 veces usando
palabra = "hola"
for i in range(5):
    print (palabra)
#Crea una variable texto = 'banana' y muestra cuántas veces aparece la letra 'a'.
texto = "banana"
letra = "a"
cantidad_a_en_banana = texto.count(letra)
print("La letra a se repite: ", cantidad_a_en_banana, "en la palabra banana")
#Crea una variable mensaje = 'El Salvador es un gran país' y muestra la posición donde aparece la palabra 'gran' usando .index().
mensaje = "El salvador es un gran pais"
print(mensaje.index("gran"))
