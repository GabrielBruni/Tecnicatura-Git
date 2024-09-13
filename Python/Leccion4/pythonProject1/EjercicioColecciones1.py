# Ejercicio 1: Eliminar duplicados de una lista.
# Escriba un programa donde tenga una lista y que a continuación
# elimine los elementos repetidos, por último mostrar la lista.

# Creamos una lista:
lista = [1, 2, 3, "Gabriel", 7, 7, 3, "Ariel", 1, "Gabriel", 2, "Ariel"]
# conjunto = set(lista) # Convertimos la lista a un conjunto de tipo set.
# lista = list(conjunto) # Convertimos el conjunto en una lista.
lista = list(set(lista)) # La conversión hecha en una sóla línea de código. (Programa más Eficiente).
print(lista)
