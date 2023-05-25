import sqlite3

def question_a(cursor):
	print("\033[32mA: ¿Cuál es la canción más antigua de la lista?\033[0m")
	# Filtro de la database = Seleccionamos la columna TEMA de la database CANCIONES y ordenamos por AÑO de forma ASCENDENTE y nos quedamos con 1 único RESULTADO
	cursor.execute("SELECT Tema FROM Canciones ORDER BY Año ASC LIMIT 1")
	# Obtenemos el 1r resultado obtenido
	result = cursor.fetchone()
	# Check de que existe un resultado
	if result:
		# Para acceder al "FETCHONE", hacemos uso de result[0]
		print("\033[34mRespuesta: \033[0m", result[0])

def question_b(cursor):
	print("\033[32mB: ¿Qué artista aparece más veces en esta lista?\033[0m")
	# Filtro: Columna INTÉRPRETE, contamos filas de cada artistas, ordenando la columna por intérpretes en orden DESC y nos quedamos con el 1r RESULTADO
	cursor.execute("SELECT Intérprete, COUNT(*) AS count FROM Canciones GROUP BY Intérprete ORDER BY count DESC LIMIT 1")
	result = cursor.fetchone()
	if result:
		# Accedemos igual que en Q:A
		print("\033[34mRespuesta: \033[0m", result[0])

def question_c(cursor):
	print("\033[32mC: ¿Qué país tiene más artistas en esta lista?\033[0m")
	# Filtro: Por columna PAÍS, quitando duplicados por ARTISTAS y ordenamos por orden descendente y nos quedamos con el 1r RESULTADO
	cursor.execute("SELECT País, COUNT(DISTINCT Intérprete) AS count FROM Canciones GROUP BY País ORDER BY count DESC LIMIT 1")
	result = cursor.fetchone()
	if result:
		# Obtenemos resultado igual que en Q:A y Q:B
		print("\033[34mRespuesta: \033[0m", result[0])

def question_d(cursor):
	print("\033[32mD: ¿Cuantas canciones distintas hay por cada idioma?\033[0m")
	# Filtro: Por IDIOMA, descartando TEMAS duplicados y agrupándolos por IDIOMA
	cursor.execute("SELECT Idioma, COUNT(DISTINCT Tema) AS count FROM Canciones GROUP BY Idioma")
	# Cambiamos .fetchone por .fetchall para seleccionar todo el filtrado que hicimos
	results = cursor.fetchall()
	# Al ser el resultado, un listado -> result[0] nos dice idioma y result[1] la cantidad. Recorremos todos los resultados obtenidos
	for result in results:
		print(f"\033[34mRespuesta:\033[0m\nIdioma: {result[0]} - Cantidad de canciones: {result[1]}")

def question_e(cursor):
	print("\033[32mE: ¿Cuál es el continente con más apariciones en la lista?\033[0m")
	# Filtro: Por Continente, agrupando y ordenando DESCENDIENTE y nos quedamos con el 1r RESULTADO
	cursor.execute("SELECT Continente, COUNT(*) AS count FROM Canciones GROUP BY Continente ORDER BY count DESC LIMIT 1")
	result = cursor.fetchone()
	if result:
		# Igual que en Q:A, Q:B y Q:C
		print("\033[34mRespuesta: \033[0m", result[0])

def question_f(cursor):
	print("\033[32mF: ¿Qué canción ha estado más % de tiempo al año como número 1?\033[0m")
	# Filtro: Por Temas, ordenando SEMANAS por DESCENDENTE y quedandonos con el 1r RESULTADO
	cursor.execute("SELECT Tema FROM Canciones ORDER BY Semanas DESC LIMIT 1")
	result = cursor.fetchone()
	if result:
		# Igual que Q:A, Q:B, Q:C y Q:E
		print("\033[34mRespuesta: \033[0m", result[0])

# Método para generar la base de datos
def create_data_base(cursor, conn):
	# Pude obtener el grueso de los datos de ./Entrega_M7_aux.py
	records = [
		{'Tema': 'Colgando en tus manos', 'Intérprete': 'Carlos Baute', 'Año': 2009, 'Semanas': 27, 'País': 'Venezuela', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': 'Despacito', 'Intérprete': 'Luis Fonsi', 'Año': 2017, 'Semanas': 26, 'País': 'Puerto Rico', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': '"You\'re the One That I Want"', 'Intérprete': 'John Travolta', 'Año': 1978, 'Semanas': 20, 'País': 'Estados Unidos', 'Idioma': 'Inglés', 'Continente': 'América del norte'},
		{'Tema': 'Bailando', 'Intérprete': 'Enrique Iglesias', 'Año': 2014, 'Semanas': 20, 'País': 'España', 'Idioma': 'Español', 'Continente': 'Europa'},
		{'Tema': 'El Perdón', 'Intérprete': 'Enrique Iglesias', 'Año': 2015, 'Semanas': 18, 'País': 'España', 'Idioma': 'Español', 'Continente': 'Europa'},
		{'Tema': 'Sorry', 'Intérprete': 'Justin Bieber', 'Año': 2015, 'Semanas': 17, 'País': 'Canadá', 'Idioma': 'Inglés', 'Continente': 'América del norte'},
		{'Tema': 'Waka Waka (Esto es África)', 'Intérprete': 'Shakira', 'Año': 2010, 'Semanas': 17, 'País': 'Colombia', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': 'Tusa', 'Intérprete': 'Karol G', 'Año': 2019, 'Semanas': 16, 'País': 'Colombia', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': "Gimme Hope Jo'anna", 'Intérprete': 'Eddy Grant', 'Año': 1988, 'Semanas': 15, 'País': 'Guyana', 'Idioma': 'Inglés', 'Continente': 'América del sur'},
		{'Tema': 'On the Floor', 'Intérprete': 'Jennifer López', 'Año': 2011, 'Semanas': 15, 'País': 'Estados Unidos', 'Idioma': 'Inglés', 'Continente': 'América del norte'},
		{'Tema': 'Voyage, Voyage', 'Intérprete': 'Desireless', 'Año': 1987, 'Semanas': 15, 'País': 'Francia', 'Idioma': 'Francés', 'Continente': 'Europa'},
		{'Tema': 'Yo Te Esperaré', 'Intérprete': 'Cali', 'Año': 2012, 'Semanas': 15, 'País': 'Colombia', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': 'Ai Se Eu Te Pego', 'Intérprete': 'Michel Teló', 'Año': 2011, 'Semanas': 14, 'País': 'Brasil', 'Idioma': 'Portugués', 'Continente': 'América del sur'},
		{'Tema': 'Candle in the wind', 'Intérprete': 'Elton John', 'Año': 1987, 'Semanas': 14, 'País': 'Reino Unido', 'Idioma': 'Inglés', 'Continente': 'Europa'},
		{'Tema': 'Quevedo: BZRP Music Sessions, Vol. 52', 'Intérprete': 'Bizarrap', 'Año': 2022, 'Semanas': 13, 'País': 'Argentina', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': 'La Bicicleta', 'Intérprete': 'Carlos Vives', 'Año': 2016, 'Semanas': 13, 'País': 'Colombia', 'Idioma': 'Español', 'Continente': 'Europa'},
		{'Tema': 'Lambada', 'Intérprete': 'Kaoma', 'Año': 1989, 'Semanas': 13, 'País': 'Brasil', 'Idioma': 'Portugués', 'Continente': 'América del sur'},
		{'Tema': 'Duele El Corazón', 'Intérprete': 'Enrique Iglesias', 'Año': 2016, 'Semanas': 12, 'País': 'España', 'Idioma': 'Español', 'Continente': 'Europa'},
		{'Tema': 'Mambo No. 5', 'Intérprete': 'Lou Bega', 'Año': 1999, 'Semanas': 12, 'País': 'Alemania', 'Idioma': 'Inglés', 'Continente': 'Europa'},
		{'Tema': 'Loca', 'Intérprete': 'Shakira', 'Año': 2010, 'Semanas': 12, 'País': 'Colombia', 'Idioma': 'Español', 'Continente': 'América del sur'},
		{'Tema': 'Always on My Mind', 'Intérprete': 'Pet Shop Boys', 'Año': 1988, 'Semanas': 11, 'País': 'Reino Unido', 'Idioma': 'Inglés', 'Continente': 'Europa'},
		{'Tema': 'La Gozadera', 'Intérprete': 'Marc Anthony', 'Año': 2015, 'Semanas': 11, 'País': 'Cuba', 'Idioma': 'Español', 'Continente': 'America del sur'},
		{'Tema': 'Infinity', 'Intérprete': 'Guru Josh', 'Año': 1990, 'Semanas': 10, 'País': 'Reino Unido', 'Idioma': 'Inglés', 'Continente': 'Europa'},
		{'Tema': 'Te Voy A Esperar', 'Intérprete': 'Juan Magán', 'Año': 2012, 'Semanas': 10, 'País': 'España', 'Idioma': 'Inglés', 'Continente': 'Europa'},
		{'Tema': 'The Final Countdown', 'Intérprete': 'Europe', 'Año': 1987, 'Semanas': 10, 'País': 'Suecia', 'Idioma': 'Inglés', 'Continente': 'Europa'}
	]

	# Crear la tabla "Canciones"
	cursor.execute('''CREATE TABLE Canciones
					(Tema TEXT, Intérprete TEXT, Año INTEGER, Semanas INTEGER, País TEXT, Idioma TEXT, Continente TEXT)''')

	# Insertar los registros en la tabla
	for record in records:
		cursor.execute('''INSERT INTO Canciones (Tema, Intérprete, Año, Semanas, País, Idioma, Continente) VALUES (?, ?, ?, ?, ?, ?, ?)''',
			(record['Tema'], record['Intérprete'], record['Año'], record['Semanas'], record['País'], record['Idioma'], record['Continente']))
	print("Base de datos creada")
	# Guardar los cambios
	conn.commit()

# Método ppal. del programa.
def questions():
	# Conectamos con la base de datos, si existiera una
	conn = sqlite3.connect('C:/Users/joanc/OneDrive/Escritorio/Python - Deusto/M7_BasesDatos_DesarrolloWeb/Prueba/canciones.db')
	if conn:
		print("\033[3mConexión establecida correctamente\033[0m")
	# Creamos cursor
	cursor = conn.cursor()
	# Escogemos el título del fichero(database)
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Canciones'")
	result = cursor.fetchone()
	# Creamos la base de datos, si ésta no existiera
	if result is None:
		create_data_base(cursor, conn)
	# Vamos método a método encontrando respuesta a cada una de las cuestiones
	question_a(cursor)
	question_b(cursor)
	question_c(cursor)
	question_d(cursor)
	question_e(cursor)
	question_f(cursor)
	# Cerramos conexión con la base de datos
	conn.close
	print("\033[3mDesconectado de la base de datos\033[0m")


questions()