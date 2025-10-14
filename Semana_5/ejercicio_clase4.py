#nombre de 7 alumnos en el orden que ingresaron al aula
#a medida que lo escribo asi lo puedo ordenar y recuperar
orden_alumnos = ['Jerson', 'Ari', 'Lindaura', 'Angel', 'Gabo', 'harry', 'tonito']

orden = int(input('Orden en el que entraste(1-7): '))
print(f'El nino que entro en {orden} se llama {orden_alumnos[orden-1]}')