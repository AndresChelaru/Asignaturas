def devuelveip(datosusuario):
	return datosusuario[3]
def devuelveemail(datosusuario):
	print(email)

def main(args):
	usuario=input("Introduce el usuario: ")
	hostname=input("Introduce el hostname: ")
	ip=input("Introduce la IP: ")
	email=input("Introduce el email: ")
	
	usuario=(usuario,hostname,ip,email)
	email=devuelveip(usuario)
		
	print(email)
	

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
