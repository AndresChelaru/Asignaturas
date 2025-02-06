import os
def enviro(variable):
	print(os.environ[variable])

def info():
	print("Usuario actual: ", os.getlogin())
	print("Variables del entorno: ", os.environ)
	print("Sistema operativo: ", os.name)
	a=os.environ["SHELL"]
	return a
	
def main(args):
	info()
	enviro("SHELL")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
