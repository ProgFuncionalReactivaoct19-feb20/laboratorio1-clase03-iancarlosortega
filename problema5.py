"""
	Problema 5 : Generar el listado de edades que no estén dentro de las black_edades.
	@iancarlosortega
"""

def funcion(x):

	black_edades = [10, 14, 30, 32, 40, 16]

	if x in black_edades:

		return False

	else:

		return True

edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

resultado = filter(funcion,edades)

print(list(resultado))