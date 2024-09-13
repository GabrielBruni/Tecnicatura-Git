import math # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)
# Dada la siguiente Tupla:
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la Tupla.
# Crear una lista que sólo incluya los números menores a 5. E imprima por consola [1, 3, 2].

lista = [] # Definimos la lista.
# Filtramos los elementos menores a 5 de la Tupla.
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de Matemáticas:
# Para sacar la raíz cuadrada de un número positivo.
numero = int(input('Digite un número positivo: '))
while numero < 0:
    print('ERROR -> Debería ser un número positivo.')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cudrada es: {math.sqrt(numero):.2f}')
