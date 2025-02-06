#!/usr/bin/env python3

import sys
import subprocess

def main(args):
	comando = "ping -n 5 google.com" if subprocess.os.name == "nt" else "ping -c 5 google.com"
	try:
		resultado = subprocess.run(comando, shell= True, capture_output= True, text=True, check=True)
		lineas = resultado.stdout.splitlines()[:5]
		print("\nPrimeras 5 líneas de la salida del ping:")
		for linea in lineas:
			print(linea)
	except subprocess.CalledProcessError as e:
		print("Error al ejecutar el ping:", e.stderr)
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
