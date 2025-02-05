#!/usr/bin/env python3
import os
import shutil
def crear_archivo():
	try:
		with open("documento.txt", "w") as prueba:
			prueba.write("Este archivo es de prueba.\n")
	except FileExistsError:
		print("El archivo ya existe.")
	return 0
def crear_directorio():
	ruta='/home/usuario/Documentos'
	os.chdir(ruta)
	os.mkdir('backup')
def copiar_ficheros():
	origen='/home/usuario/Documentos/documento.txt'
	destino='/home/usuario/Documentos/backup/documento.txt'
	shutil.copy(origen,destino)
	return 0
def main(args):
	create_archivo=crear_archivo()
	crear_dire=crear_directorio()
	copy_ficher=copiar_ficheros()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
