# Declaración y asignación de las dos listas.
colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre':'Josep'}, {'Nombre':'Claudio'}, {'Nombre': 'Isabel'}, {'Nombre': 'Sheila'}]

# Función switch para la selección de acción a realizar.
def switch(option):
	if option == 1:
		return option_1()
	elif option == 2:
		return option_2()
	elif option == 3:
		return option_3()
	elif option == 4:
		return option_4()
	elif option == 5:
		return option_5()
	elif option == 6:
		return option_6()
	elif option == 7:
		return option_7()

# Añadir colores a la lista.
def option_1():
	global colores
	new_color = input("\033[92mNuevo color: \033[0m")
	""" Recuerda tener en cuenta la mayúscula y minúscula 
	(solo insertar en la lista en minúscula)."""
	new_color = new_color.lower()
	# ADICIONAL: Check de que la entrada de color es únicamente texto.
	if not new_color.isspace() and not new_color.replace(" ", "").isalpha():
		print("\033[91mEntrada inválida. Por favor ingrese únicamente caracteres.\033[0m\n")
		option_1()
	# Comprobar que no existe y añadir a la lista.
	if new_color in colores:
		print("El color ya existe")
		# No salir de "añadir colores", sin añadir un color.
		option_1()
	else:
		colores.append(new_color)

# Mostrar listado de colores.
def option_2():
	global colores
	print(f"\033[92m{colores}\033[0m")

# Ordenar listado de colores alfabéticamente.
def option_3():
	colores.sort()
	print("\033[92mColores ordenados\033[0m")

# Añadir usuarios
def option_4():
	global usuarios
	global colores
	new_user = input("\033[92mNombre del nuevo usuario: \033[0m")
	new_input = {'Nombre': new_user}
	usuarios.append(new_input)
	""" Cada vez que se añade un usuario, hay que agregar un color 
	a la lista si no hay suficientes para repartir entre los usuarios. """
	color_count = len(colores)
	user_count = len(usuarios)
	if user_count > color_count:
		option_1()

# Asignar colores a cada usuario de manera aleatoria.
def option_5():
	import random
	global colores
	global usuarios
	colour_copy = colores.copy()
	for user in usuarios:
		# No repetir color en ningún jugador.
		asign_colour = colour_copy.pop(random.randint(0, len(colour_copy) - 1))
		""" El color debe ser almacenado en el diccionario 
		de cada jugador, añadiendo la clave 'Color'."""
		user["Color"] = asign_colour
		# Mostrar el resultado de la asignación de color en cada jugador.
		print (f"\033[92m{user}\033[0m")

# Función auxiliar para Opt_6, donde ordenamos nombres.
def sort_names(users):
	n = len(users)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if users[i]['Nombre'] > users[j]['Nombre']:
				users[i], users[j] = users[j], users[i]
	return users

# Función auxiliar para Opt_6, donde eliminamos usuarios.
def delete_user(index, find_list):
	user_to_delete = find_list[index - 1]
	usuarios.pop(usuarios.index(user_to_delete))

# Eliminar usuarios
def option_6():
	global usuarios
	# No modificar el orden de la lista original.
	users_copy = usuarios.copy()
	# Algoritmo de ordenación de user_copy con Swaps.
	users_copy = sort_names(users_copy)
	# Mostrar los usuarios por orden alfabético y con índice:
	for i, user in enumerate(users_copy):
		print(str(i+1) + ": " + user['Nombre'])
	# Eliminar usuario.
	try:
		choice = int(input("\033[92mEscoja # del usuario a eliminar: \033[0m"))
		if 1 <= choice <= len(users_copy):
			delete_user(choice, users_copy)
	except ValueError:
		print("Escoja un valor válido.")

# Mostrar usuarios, solo el Nombre.
def option_7():
	global usuarios
	for user in usuarios:
		name = user['Nombre']
		print(f"\033[92m{name}\033[0m")

# Función inicial del programa
def ColorMenu():
	while True:
		print("""\n\033[94m----------------------MENU----------------------\033[0m\n1: Añadir color\n\
			2: Listado de colores\n3: Ordenar listado de colores alfabeticamente\n4: Añadir usuario\n\
			5: Asignar color aleatorio a los usuarios\n6: Eliminar usuario\n7: Mostrar usuarios\n\
			8: Salir""".replace("\t", ""))
		try:
			option = int(input("\033[92mSeleccione acción: \033[0m",))
			print("")
			if option == 8:
				print ("\033[92mSaliendo del programa...\n¡Hasta pronto!\033[0m")
				break
			elif option > 8 or option < 1:
				print ("\033[91mEntrada inválida. Por favor ingrese un número entre 1 y 8.\033[0m\n")
			switch(option)
		except ValueError:
			print("\033[91mEntrada inválida. Por favor ingrese un número válido.\033[0m\n")

# Llamada al programa.
ColorMenu()
