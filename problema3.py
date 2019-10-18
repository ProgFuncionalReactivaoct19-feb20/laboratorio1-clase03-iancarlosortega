"""
	Problema 3 : Filtrar cadenas
	@iancarlosortega
"""


def funcion(x):

	filtrar = ["No", "hay", "que", "lo", "que", "no", "la"]

	if x in filtrar:

		return True

	else:

		return False

frase = "No hay medicina que cure lo que no cura la felicidad"

lista = frase.split()

resultado = filter(funcion,lista)


print(list(resultado))