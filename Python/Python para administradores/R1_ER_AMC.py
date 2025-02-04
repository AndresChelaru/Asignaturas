import sys
import re

# def ejercicio1(texto):
	# patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	# compilar = re.compile(patron)
	# verificar = compilar.search(texto)
	# if verificar:
		# return True
	# else:
		# return False
	
# def imprimir(verificar):
	# print(verificar)


# def main(args):
	# texto = "ejemplodomain.ext"
	# verificar = ejercicio1(texto)
	# imprimir(verificar)
	# return 0

#-----------------------------------
# def ejercicio2(texto):
	# patron = r"\b\d{2}[-/]\d{2}[-/]\d{4}\b"
	# compilar = re.compile(patron)
	# verificar = compilar.findall(texto)
	# return len(verificar)
	
# def imprimir(cantidad):
	# print(f"Se han encontrado {cantidad} fechas en el texto.")

# def main(args):
	# texto = "Hoy estamos a 04-02-2025 y mañana sera 05/02/2025"
	# cantidad = ejercicio2(texto)
	# imprimir(cantidad)

#----------------------------------
# def ejercicio3(texto):
	# patron = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{3}\b"
	# compilar = re.compile(patron)
	# verificar = compilar.findall(texto)
	# return verificar
	
# def imprimir(verificar):
	# print("Número de teléfonos encontrados:", verificar)
	
# def main(args):
	# texto = "Mi número de telefono es 000-000-000, pero también puedes llamarme al 000000000 o al 000.000.000"
	# verificar = ejercicio3(texto)
	# imprimir(verificar)
	
#---------------------------------
# def ejercicio4(texto):
	# patron = "reemplazar"
	# reemplazo = "cambiar"
	# flag=re.I
	# nuevo_texto=re.sub(patron,reemplazo,texto,count=0,flags=flag)
	# return nuevo_texto

# def imprimir(nuevo_texto):
	# print(nuevo_texto)

# def main(args):
	# texto = "Este será el texto a reemplazar."
	# nuevo_texto = ejercicio4(texto)
	# imprimir(nuevo_texto)	

#--------------------------------
# def ejercicio5(texto):
	# patron = r"</?\w+[^>]*>"
	# compilar = re.compile(patron)
	# verificar = compilar.findall(texto)
	# return verificar
# def imprimir(verificar):
	# print("Se han encontrado las siguientes etiquetas XML:", verificar)

# def leer_archivo_xml(nombre_archivo):
	# try:
		# with open(nombre_archivo, "r", encoding="utf-8") as archivo:
			# return archivo.read()
	# except FileNotFoundError:
		# print("Error: El archivo no se encontró.")
		# return None

# def main(args):
	# nombre_archivo = input("Introduce el nombre del archivo XML: ")
	# contenido = leer_archivo_xml(nombre_archivo)
	
	# if contenido is not None:
		# verificar = ejercicio5(contenido)
		# imprimir(verificar)

#--------------------------------
# def ejercicio6(texto):
	# patron = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
	# compilar = re.compile(patron)
	# ip = compilar.findall(texto)
	# if ip:
		# return ip[0]
	# return None

# def imprimir(ip):
	# print(ip)
	
# def main(args):
	# texto = "Conéctate a la IP 192.168.0.1 o 10.0.0.5."
	# verificar = ejercicio6(texto)
	# imprimir(verificar)
	# return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
