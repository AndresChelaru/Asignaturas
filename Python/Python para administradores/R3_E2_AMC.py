#!/usr/bin/env python
import os
def crear_archivo():
	ruta='/home/usuario/Escritorio/prueba'
	os.chdir(ruta)
	try:
		with open("prueba.txt", "w") as prueba:
			prueba.write("Este archivo es de prueba.\n")
	except FileExistsError:
		print("El archivo ya existe.")
	return 0
	
def cambiar_nombre():
	ruta='/home/usuario/Escritorio/prueba'
	os.chdir(ruta)
	os.renames('prueba.txt','log_de_sistema.log')
	return 0

def eliminar_archivo():
	ruta='/home/usuario/Escritorio/prueba/log_de_sistema.log'
	try:
		os.remove(ruta)
	except OSError as e:
		print(f'Error: {ruta} : {e.strerror}')
	return 0
def main(args):
	nuevoarchivo=crear_archivo()
	nuevo_nombre=cambiar_nombre()
	delete_archivo=eliminar_archivo()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
