#Ejercicio:Búsqueda de correos electrónicos

def lista_correo(nombre='correos.txt'):
    lista=[]
    archivo=open(nombre,encoding='UTF-8')
    for lineas in archivo:
        lista.append(lineas.strip())
    return lista



def busqueda_correo(lista):
    correo=input('Ingrese el correo a buscar: ').strip()
    for i in range(len(lista)):
        if lista[i]==correo:
            return i
    return -1


def filtrar_correo(lista):
    provedor_input = input('Ingrese un provedor de correo: ').strip()

    lista_provedor = []

    for elementos in lista:
        nombre, provedor = elementos.split('@')
        if provedor == provedor_input:
            lista_provedor.append(elementos)

    return lista_provedor

correos=lista_correo()

total=len(correos)

busqueda=busqueda_correo(correos)

if busqueda==-1:
    print('No se encontro el correo en la lista')
else:
    print(f'La posicion del correo esta en la posicion {busqueda}')
    print(f'Hay en total {total} correos en la lista')
    nombre,provedor=correos[busqueda].split('@')
    print(f'El provedor del correo es {provedor}')
    print()



filtro=filtrar_correo(correos)

if len(filtro)==0:
    print('No se encontro correos con ese provedor en la lista')
else:
    print(f'Correos con el provedor ingresado')
    for elementos in filtro:
        print(elementos)
