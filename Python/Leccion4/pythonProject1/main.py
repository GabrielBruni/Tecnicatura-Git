# lista = Ariel, Liliana, Natalia, Osvaldo
# Colecciones en Python: ##CLASE02 26-08-24

# Las listas es lo que se conoce en otros lenguajes como Arreglos o Vectores. ##CLASE02 26-08-24

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2]) # Sólo muestra el índice 0, 1 ; pero no el índice 2.
# Ir del inicio de la lista al índice (sin incluirlo).
print(nombres[ :3]) # índices a mostrar 0, 1, 2.
# Desde el índice indicado hasta el final:
print(nombres[1: ])
# Modificamos un valor:
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista:
for nombre in nombres: # nombre es singular, la lista es plural.
    print(nombre)
else:
    print('Se acabaron los elementos de la lista.')

# Preguntarnos cuántos elementos tiene una lista.
print(len(nombres)) # Le pasamos como parámetro la lista.

# Agregamos un elemento a nuestra lista.
nombres.append('Gabriel')
nombres.append([1, 2, 3]) ##CLASE02 26-08-24
nombres.append(True) ##CLASE02 26-08-24
nombres.append(10.45) ##CLASE02 26-08-24
nombres.append([4, 5]) ##CLASE02 26-08-24
nombres.append(7) ##CLASE02 26-08-24
print(nombres)

# Insertar un elemento en un índice específico de nuestra lista.
nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Débora')
print(nombres)

# Eliminamos un elemento de nuetra lista.
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento de la lista.
nombres.pop()
print(nombres)

# Eliminar un índice específico de la lista.
del nombres[2] # 'del' significa delete (eliminar).
print(nombres)

# Eliminar, borrar o limpiar todos los elementos de una lista.
nombres.clear()
print(nombres)

# Eliminar la lista.
del nombres
#print(nombres) # Aquí nos mostrará un error.

# Definir una TUpla:
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes; NO paréntesis.
print(cocina[0])
print(cocina[-1])
print(cocina[-2])

# Acceder a un rango:
print(cocina[0:2]) # No se incluye el último elemento.

# Ejemplo
verduras = ('papa',) #Una Tupla necesita aunque sea de un elemento: la coma.
# de lo contrario sólo sería un tipo str cadena.

# Recorremos los elementos de la Tupla:
for cocinar in cocina: # print está usando \n para saltos de líneas.
    print(cocinar, end=' ') # usamos end= para eliminar los saltos de líneas.

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n',cocina)

# del cocina # esto es para eliminar una Tupla.

# Tipo set. ##CLASE02 26-08-24
planetas = {'Marte','Júpiter','Venus'}
print(len(planetas)) # Usamos la función len = lenght significa largo.

# Revisar si un elemento existe dentro de set.
print('Júpiter' in planetas)

# Agregar un elemento.
planetas.add('Tierra') # add es una función.
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe.
planetas.remove('Júpiter') # Esta función ante un mal ingreso u inexitencia del elemento da error.
print(planetas)
planetas.discard('tierra') # Esta función no nos presenta ningún error.
print(planetas)

# Limpiar set.
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra fun error.

# 'Maradona':10 Un diccionario está compusto por dos elementos.
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario.
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con llave (key).
print(diccionario['IDE'])

# Otra forma de recuperar un elemento.
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos.
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Cómo recorrer los elementos.
for termino in diccionario: # Recorremos mostrando sólo las llaves.
    print(termino)

# Necesitamos una función para recorrer un Diccionario.
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un Diccionario.
for termino in diccionario.keys(): # Estamos usando una función.
    print(termino) # Muestra sólo las llaves.

for valor in diccionario.values(): # Usamos una función para acceder al valor.
        print(valor)

# Comprobar la existencia de algún elemento.
print('IDE' in diccionario) # Devuelve un booleano.

# Agregar un elemento.
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento.
diccionario.pop('SABD')
print(diccionario)

# Vaciar un Diccionario.
diccionario.clear()
print(diccionario)

# Eliminar Diccionario.
del diccionario # El Diccionario se borró.

# Concatenar listas.
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenamos.
print(lista3)

lista3.extend([7, 8, 9, 1]) # Función para agregar varios elementos a una lista.
print(lista3)

print(lista3.index(5)) # Función para ubicar en qué índice está el valor ingresado.
# print(lista3.index(0)) # Esto daría error por no ser el elemento parte de la lista.

# Cómo saber cuántos valores repetidos hay dentro de una lista.
print(lista3.count(1)) # Cuenta cuántos valores iguales hay dentro de la lista.

# Para poner nuestra lista al revés. (Ascendente o Descendente)
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos.
lista3 = lista3 * 2
print(lista3)

# En Python es una función:
# Métodos de Ordenamiento; Ascendentemente. (Método de Burbuja, Inserción y de Selección)
lista3.sort() # Ordena los elementos ascendentemente.
print(lista3)

# Métodos de Ordenamiento; Descendentemente. (Método de Burbuja, Inserción y de Selección)
lista3.sort(reverse=True) # Ordena los elementos descendentemente.
print(lista3)

# Repaso de Tuplas.
tupla = (4, 'Hola' , 6.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro.
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana.
# Lo que podemos usar dentro de Tuplas son: index; count; len.
# En Tuplas se puede convertir de Tupla a lista y de lista a Tupla.
##CLASE02 26-08-24

##CLASE03 02-09-24
# Repaso de Set o Conjunto.
# Para definir un conjunto.
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el número 3 NO estpa en el conjunto1.

# Cómo hacer la igualdad de dos conjuntos.
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano.

# Operaciones en conjuntos.
conjunto3 = conjunto1 | conjunto2 # La línea une los dos conjuntos.
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Qué elemento tiene en común.
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que está en el conjunti1 y NO en el conjunto2.
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # Elementos que NO comparten o que son diferentes entre ambos.
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # Aquí preguntamos si un conjunto es un subconjunto dentro de otro.
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 están dentro del conjunto3.
print(conjunto3.issuperset(conjunto2)) # Si es "True" quiere decir que el conjunto3 es un superconjunto.
print(conjunto2.issuperset(conjunto3))


# Cómo saber si ambos conjuntos son Disconexos. (No comparten elementos en común).
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en común.

# Convertir un conjunto totalmente en Inmutables.
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente Inmutable.
# No se puede agregar, modificar ni eliminar elementos del conjunto.

# Repaso de Diccionarios:
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Cómo eliminar:
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los Diccionarios pueden almacenar diferentes tipos de datos:
diccionario2 = {'Gabriel': {'Edad': 24, 'Altura': 1.78}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo Derecho'},
    11: {'Nombre': 'Ángel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posición': 'Extremo Derecho'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posición': 'Portero'},
    24: {'Nombre': 'Enzo Fernández', 'Edad': 23, 'Altura': 1.78, 'Precio': '75 Millones', 'Posición': 'CentroCampista'},
    9: {'Nombre': 'Julián Álvarez', 'Edad': 24, 'Altura': 1.70, 'Precio': '30 Millones', 'Posición': 'Delantero'},
    23: {'Nombre': 'Emiliano Martinez', 'Edad': 32, 'Altura': 1.95, 'Precio': '80 Millones', 'Posición': 'Portero'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 30, 'Altura': 1.82, 'Precio': '25 Millones', 'Posicion': 'CentroCampista'},
    20: {'Nombre': 'Alexis Mac Allister', 'Edad': 25, 'Altura': 1.76, 'Precio': '75 Millones', 'Posición': 'CentroCampista'}
}
print(seleccionArgentina)
print(seleccionArgentina[10])
print(seleccionArgentina.values())

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores más al diccionario: seleccionArgentina.
print('Tenemos cargados en el diccionario la cantidad de: ',end=' ')
print(len(seleccionArgentina))

# Pilas usando listas.
pila = [1, 2, 3]

# Agregar elementos a la pila por el final.
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final.
pila.pop()
print(pila)

# Sacamos elementos desde el final.
elementoBorrado = pila.pop() # Quita el último elemento y lo guarda en la variable.
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')

# Colas con listas.
# Estructura de datos tipo fifo: (first input / first output).
cola = ['Gabriel', 'Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola.
cola.append('Natalia')
cola.append('José')
print(cola)

# Sacamos elementos de la cola.
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)
##CLASE03 02-09-24

##CLASE04 09-09-24
# Seguimos mostrando cómo recorrer un diccionario con el ciclo for.
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
##CLASE04 09-09-24
