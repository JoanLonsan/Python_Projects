# Base de datos de nuestros amigos
class Friend:
	# Inicializamos clase Friend
	def __init__(self, name, dni, locality, country):
		self.name = name
		self.dni = dni
		self.locality = locality
		self.country = country
	# Método para mostrar los datos personales de nuestro amigo
	def show_friend_data(self):
		print("\033[94m --------- Datos del Amigo ---------\033[0m" +
			"\nNombre: " + self.name + 
			"\nDNI: " + self.dni + 
			"\nLocalidad: " + self.locality + 
			"\nPais: " + self. country)

# Base de datos de los gustos musicales de nuestro amigos
class MusicalPreferences:
	# Inicializamos clase MusicalPreferences
	def __init__(self, favorite_song, group, genre):
		self.favorite_song = favorite_song
		self.group = group
		self.genre = genre

	# Método para mostrar los gustos musicales de nuestro amigo
	def show_music_data(self):
		print("\033[94m--- Gustos musicales: " + self.name + " ---\033[0m\nCanción favorita: " + self.favorite_song +
			"\nGrupo: " + self.group + 
			"\nEstilo musical: " + self.genre)

# Clase que herede de Friend y de Gustos musicales
class FriendMusicalPref(Friend, MusicalPreferences):
	# Iniciamos clase hija de Friend y MusicPref.
	def __init__(self, name, dni, locality, country, favorite_song, group, genre):	
		Friend.__init__(self, name, dni, locality, country)
		MusicalPreferences.__init__(self, favorite_song, group, genre)
	# Método para imprimir AMBOS datos
	def show_data(self):
		self.show_friend_data()
		self.show_music_data()

# Función para obtener datos Friend
def get_friend_data():
	# Obtención de datos de Friends
	name = input("\033[92mNombre y apellidos: \033[0m").title() # .title para 1ª letra en mayus de cada palabra
	dni = input("\033[92mDNI: \033[0m")
	locality = input("\033[92mPoblación: \033[0m").title() 
	country = input("\033[92mPaís: \033[0m").upper() # .upper para todos mayus.

	# Check estructura del DNI.
	while True:
		if len(dni) != 9 or not dni[:-1].isalnum() or not dni[-1].isalpha():
			print("\033[91mError: El DNI debe indicarse con ocho números más letra al final.\033[0m")
			dni = input("DNI: ")
		else:
			break

	return name, dni, locality, country

# Función para obtener datos Musicales
def get_music_data():
	song = input("\033[92mCanción favorita: \033[0m").title()
	group = input("\033[92mGrupo: \033[0m").title()
	genre = input("\033[92mEstilo musical: \033[0m").upper()

	return song, group, genre

def main():
	print("\n\033[94m--- Formulario: Gustos musicales ---\033[0m")
	# Lista para almacenar los amigos
	friends = []
	# Condición True para poder almacenar más de un FRIEND
	while True:
		name, dni, locality, country = get_friend_data()
		song, group, genre = get_music_data()
		friend = FriendMusicalPref(name, dni, locality, country, song, group, genre)
		# Mostramos data recién creada
		friend.show_data()
		# Agregamos la nueva información a la lista
		friends.append(friend)
		choice = input("\n¿Deseas agregar a otro amigo? \033[92m(s/n)\033[0m: ")
		# Opción para salir del bucle
		if choice.lower() != 's':
			break

	choice = input("\n¿Deseas ver el listado de todos los amigos? \033[92m(s/n)\033[0m: ")
	# Opción para ver el listado de FRIENDS y sus gustos musicales
	if choice.lower() == 's':
		for friend in friends:
			friend.show_data()

# Inicio de programa
main()