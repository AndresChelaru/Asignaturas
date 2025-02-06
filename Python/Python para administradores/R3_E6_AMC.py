#!/usr/bin/env python3

import sys
import subprocess

def listar_archivos():
	comando = "dir" if subprocess.os.name == "nt" else "ls"
	with open("lista_archivos.txt", "w") as archivo:
		subprocess.run(comando, shell=True, stdout=archivo, stderr=subprocess.PIPE, text=True)
	print("Listado de archivos guardado en 'lista_archivos.txt'")
	
def leer_archivo():
	with open("lista_archivos.txt", "r") as archivo:
		contenido = archivo.read()
	print("Contenido de 'lista_archivos.txt':\n")
	print(contenido)

def main(args):
	listar_archivos()
	leer_archivo()
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
