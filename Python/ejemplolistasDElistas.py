#EJEMPLOS LISTAS  DE LISTAS PARA CREAR MATRICES


def main(args):
	#creación de una matriz de 3x4
	matriz=[]
	for i in range(3):#para cada fila
		matriz.append([])#añadimos una lista vacía
		for j in range(4):
			dato=input(f"Introduzca el elemento {i},{j}: ")
			matriz[i].append(dato)
	print(matriz)
	#podemos mejorar la forma en que la mostramos
	print("MATRIZ MOSTRADA POR FILAS")
	for i in range(3):
		print(matriz[i])
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
