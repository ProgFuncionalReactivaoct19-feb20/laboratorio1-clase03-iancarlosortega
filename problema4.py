"""
	Problema 4 : Filtrar notas cualitativas
	@iancarlosortega
"""
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

nota_cuali = lambda x : x[3]

resultado = filter(lambda x : x[3] == "Regular" or x[3] == "Bueno",notas)

print(list(resultado))
