"""
	Problema 1 : Determinar los estudiantes que pasan de ciclo
	@iancarlosortega
"""

# Abrir el archivo

archivo = open("promedios.txt")

# Leer el archivo

lectura = archivo.read()

# Transformar a lista el archivo

list(lectura)

# Separar la lista con el metodo split

lista = lectura.split(',')

# Transformar la lista tipo cadena a entero para poder operar

lista = list(map(int,lista))

resultado = filter(lambda x : x>=16.5,lista)

print(list(resultado))