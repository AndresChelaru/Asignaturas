#!/usr/bin/env python3

import sys
import subprocess

def ejecutar_script():
	script = "hello.sh"
	try:
		resultado = subprocess.run(["bash", script], capture_output=True, text=True, check=True)
		print("\nSalida del script:")
		print(resultado.stdout)
	except subprocess.CalledProcessError as e:
		print("Error al ejecutar el script:", e.stderr)
	
	return 0

def main(args):
	script = ejecutar_script()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
