import sys
import os
import shutil

def crear_directorio():
	estructura = [
		"proyecto",
		"proyecto/datos",
		"proyecto/scripts",
		"proyecto/informes"
	]
	for directorio in estructura:
		os.makedirs(directorio, exist_ok=True) #exist_ok=True: El parámetro exist_ok=True en os.makedirs(directorio, exist_ok=True) permite que la función cree el directorio sin generar un error si este ya existe.
	print("Estructura creada.")

def comprimir_directorio():
	shutil.make_archive("proyecto", "zip", "proyecto") #"proyecto": Es el nombre base del archivo comprimido resultante (se generará proyecto.zip). "zip": Especifica el formato de compresión (puede ser zip, tar, gztar, bztar, etc.). "proyecto": Es la ruta del directorio que se comprimirá.
	print("Directorio 'proyecto' comprimido en proyecto.zip")

def descomprimir_archivo():
	shutil.unpack_archive("proyecto.zip", "proyecto_descomprimido")
	print("Archivo 'proyecto.zip' descomprimido en 'proyecto_descomprimido'")
	
def main(args):
	crear_estructura_directorios()
	comprimir_directorio()
	descomprimir_archivo()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
