# Ejercicio 3: Gregar personajes a una lista.
# Escriba un programa dónde cree una lista con los siguientes personajes del señor de los anillos.
# Nombrer: Aragorn.
# Clase: Guerrero.
# Raza: Dúnadan del norte.

# Nombre: Gandalf.
# Clase: Mago.
# Raza: Istar.

# Nombre: Legolas.
# Clase: Arquero.
# Raza: Elfo Sindar.

# Tarea: Agregar por lo menos otros tres personajes, que sean a tu elección

# Nombre: Sauron.
# Clase: Espíritu.
# Raza: Maiar.

# Nombre: Galadriel.
# Clase: Clan.
# Raza: Elfos Noldor.

# Nombre: Arwen.
# Clase: Estrella.
# Raza: Peredhil.

personajes = [] # Creamos una lista vacía.
# Creamos diccionarios:
P = {'Nombre': 'Aragorn', 'Clase': 'Guerrero', 'Raza': 'Dúdan del norte'}
personajes.append(P) # Agregamos a la lista un personaje.
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
# Tarea: Agregar por lo menos otros tres personajes, que sean a tu elección
P = {'Nombre': 'Sauron', 'Clase': 'Espíruto', 'Raza': 'Maiar'}
personajes.append(P) # Agregamos a la lista un personaje.
P = {'Nombre': 'Galadriel', 'Clase': 'Clan', 'Raza': 'Elfos Noldor'}
personajes.append(P)
P = {'Nombre': 'Arwen', 'Clase': 'Estrella', 'Raza': 'Peredhil'}
personajes.append(P)
print(personajes)
