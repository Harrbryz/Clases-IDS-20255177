#vamos a guardar nombres y apellidos
#se pide que proponga dos propuestas de correos a partir del nombre y apellido
#si la perosna escribe mas de una mayuscula no nos importa
nombre = input("escriba su nombre: ").lower()
apellido = input('apellido: ').lower()
print(f'{nombre.lower()}.{apellido.lower()}@ISND.com')
print(f'{nombre.lower()[0]}{apellido.lower()}@ISND.com')