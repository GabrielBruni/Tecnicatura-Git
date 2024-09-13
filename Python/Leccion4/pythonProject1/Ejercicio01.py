# Ejercicio 1: Llenar una lista.
# Llenar una lista con los números de 1 al 50, luego mostrar la lista con un bucle for.
# Los elementos deben ostrarse de la siguiente forma:
# 1-2-3-4-5....-50.

# lista = []
# i = 1
# while i <= 50:
#     lista.append(i)
#     i += 1

lista = list(range(1, 51)) # Algoritmo eficaz.
for i in lista:
    print(i,end='-')