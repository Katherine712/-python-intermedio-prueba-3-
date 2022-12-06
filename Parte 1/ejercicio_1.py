#Ejercicio_1
import random as rd

def ingreso_num():
	while True:
		adivinanza = input('Adivina el numero entre 1 y 100: ')
		if adivinanza.isdigit():
			return int(adivinanza)
		print('Ingrese un numero entero entre 1 y 100 ')
def juego():
	num_random=rd.randint(1,100)

	count=0
	cond=True
	while cond and count!=10:
		count+=1
		print(f'Intento {count}')
		adivinanza=ingreso_num()
		if adivinanza==num_random:
			cond=False
			print(f'Correcto, es el número {num_random}')
		elif adivinanza>num_random:
			print('Su estimación es muy alta')
		else:
			print('Su estimación es muy baja')
		print()
	if count==10 and cond:
		print('Se acabaron los intentos')
		print(f'El numero secreto era el {num_random}')

juego()
