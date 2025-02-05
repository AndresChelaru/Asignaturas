#!/usr/bin/env python3
import os

def cambiar_directorio():
	if os.name=='posix':
		ruta='/home/usuario/Escritorio/prueba'
	else:
		ruta='/home/usuario'
	os.chdir(ruta)
def mostrar_directorio():
	print(os.getcwd())
	return 0

def crear_subdirectorio():
	ruta='/home/usuario/Escritorio'
	os.chdir(ruta)
	os.mkdir('prueba')
	
def listar_subdirectorio():
	print(os.listdir())
def main(args):
	create_directory=crear_subdirectorio()
	change_directory=cambiar_directorio()
	directory=mostrar_directorio()
	list_directory=listar_subdirectorio()
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
