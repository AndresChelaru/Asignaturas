#EJEMPLOS ORDENACIÓN DE LISTAS  
#  

def main(args):
	from operator import itemgetter
	#creamos una lista de tuplas
	milista=[(2,3,6),(1,4,5),(6,6,6)]

	#podemos ordenar la lista por el primer elemento de cada tupla
	#podemos hacerlo sobre la misma lista
	milista.sort()
	print(milista)

	#o podemos hacerlo creando una nueva lista
	milistaordenada=sorted(milista)
	print("\nLista ordenada")
	print(milistaordenada)

	#podemos ordenar por otro elemento de cada tupla.
	milistaordenada=sorted(milista,key=itemgetter(1))
	print("\nLista ordenada por el segundo elemento de la tupla")
	print(milistaordenada)

	#podemos establecer distintos criterios de ordenación
	milistaordenada=sorted(milista,key=itemgetter(2,1))
	print("\nLista ordenada por el tercer elemento de la tupla. En caso de igualdad por el segundo")
	print(milistaordenada)

	#incluso podemos ordenar en orden inverso
	milistaordenada=sorted(milista,key=itemgetter(1),reverse=True)
	print("\nLista ordenada por el segundo elemento de la tupla en orden inverso")
	print(milistaordenada)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
