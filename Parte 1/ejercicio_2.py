#Ejercicio_2
dic={1:'piedra',2:'papel',3:'tijeras'}
def menu(dic):
	for a,b in dic.items():
		print(f'{a}. {b}')
	print('4. Salir')
	print('Jugaremos piedra, papel o tijera?')

def ingreso_num_2(dic):
	menu(dic)
	while True:
		adivinanza = input('Ingrese una opción: ')
		if adivinanza.isdigit():
			adivinanza=int(adivinanza)
			if adivinanza in range(1,5):
				return adivinanza
		print('Ingrese un numero entero entre el rango de 1 a 4')



def juego_2(dic):
	v,e,d=0,0,0
	cond=True
	while cond:
  
		opcion=ingreso_num_2(dic)
		import random 
		opcion_computador = random.randint(1, 3)
		desicion=''

		if opcion==opcion_computador:
			e+=1
			desicion+='empate'
		elif opcion==1:
			if opcion_computador==2:
				d+=1
				desicion='Derrota'
			else:
				v+=1
				desicion = 'Victoria'
		elif opcion==2:
			if opcion_computador==3:
				d+=1
				desicion='Derrota'
			else:
				v+=1
				desicion = 'Victoria'
		elif opcion == 3:
			if opcion_computador==1:
				d+=1
				desicion='Derrota'
			else:
				v+=1
				desicion = 'Victoria'
		else:
			cond=False
			print('Resultados: ')
			print(f'Victorias {v}')
			print(f'Empates {e}')
			print(f'Derrotas {d}')

		if cond:
			print(f'Tu eleccion: {dic[opcion]}')
			print(f'Eleccion de la computadora: {dic[opcion_computador]}')
			print(f'Resultado: {desicion}')
			print()

juego_2(dic)
