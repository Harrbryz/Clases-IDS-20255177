#ingresar salario con simbolo 
#validar por medio de un mensaje que el valor ingresado cumple dos condiciones
#el valor ingresado lleva un simbolo $
#El valor ingresado con simbolo $ al inicio
salario = input('ingrese su salario: ')

print(salario.count('$')==1)
print(salario[0]=='$')
