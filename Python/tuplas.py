import sys

# def datosip(datosusuario):
	# return datosusuario[3]

# def main(*args):
	# usuario = input("Introduza el nombre del usuario")
	# hostname = input("Introduza el hostname")
	# ip = input("Introduza la IP")
	# email = input("Introduza el email del usuario")
	
	# usuario = (usuario, hostname, ip, email)
	# email=datosip(usuario)
	
	
	# print(email)
def obtener_dominio(email):
	if '@' in email:
		partes = email.split('@')
		if len(partes) > 1:
			return partes[1]




def main(*args):
	email = input("Introduce el email: ")
	dominio = obtener_dominio(email)
	
	if dominio :
		print(f"El dominio del email es : {dominio}")



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
