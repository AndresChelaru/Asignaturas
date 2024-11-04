#EJEMPLOS LISTAS  
#  

def main(args):
	#podemos crear listas vacías
	lista1=[]
	lista2=list()

	#podemos crear listas con valores
	lista3=[7,8,12,4]
	lista4=['Juan','María','Marcelo']

	#podemos crear una lista a partir de una cadena o de una tupla
	lista5=list("Pyton")
	lista6=list((5,6,7,8,9))
	

	#podemos crear una lista de tuplas
	lista6=[('Marta','1.64'),('José','1.79'),('Mateo','1.75')]

	#podemos mostrar las listas completas
	print("\nEsto es una lista vacía", lista1)
	print("\nEsta es la lista 2. También está vacía ",lista2)
	print("\nEsta es la lista 3", lista3)
	print("\nEsta es la lista 4", lista4)
	print("\nListas creadas a partir de cadena y tupla")
	print(lista5)
	print(lista6)
	print("\nEsto es una lista donde cada elemento es una tupla")
	print(lista6)
	

	#son elementos iterables, así que podemos hacer esto
	print("\nPodemos mostrar los elementos de uno en uno")
	for numero in lista3:
		print(numero)

	#y otras cosas chulas como esto
	print("\nLista de números multiplicada por 2")
	print([elemento*2 for elemento in lista3])
	

	#son elementos mutables. Podemos modificar sus elementos
	print("\nLista 4 modificada")
	lista4[2]='Jorge'
	print(lista4)

	#python nos da herrmientas para manipularlas
	
	#podemos añadir elementos a una lista ya creada
	lista2.append('Hola')
	print("\n Ahora lista2 ya no está vacía")
	print(lista2)

	#podemos añadir una lista a otra (extender)
	lista2.extend(lista4)
	print("\n Lista2 ha crecido")
	print(lista2)

	#buscar la posición de un elemento
	i=lista2.index('Juan')
	print(f"Juan está en la posición {i}")

	#podemos insertar en una posición concreta
	lista2.insert(1,'Pablo')
	print("\nLas posiciones han cambiado. Hay nuevos elementos")
	print(lista2)

	#podemos sacar elementos de la lista usando su posición
	lista2.pop()
	lista2.pop(1)
	print("\nLas posiciones han cambiado. Alguno se ha ido")
	print(lista2)

	#podemos eliminar elementos
	lista2.remove('María')
	print("\nAdiós María")
	print(lista2)

	#podemos darle la vuelta
	lista2.reverse()
	print("\nCambiados de sitio.")
	print(lista2)

	#y podemos borrar todos los elementos de la lista
	lista2.clear()
	print("\nAquí ya no hay nada")
	print(lista2)

	#podemos ordenar listas. Lo vemos en otro ejemplo.
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
