"""
TAREAS (parte 1):
1 Crear la base de datos ✓
2 Crear la tabla ✓
3 Añadir una columna nueva con el campo IDIOMA ✓
4 Añadir una columna nueva con el campo CONTINENTE ✓
5 Insertar todos los datos ✓
-------------------------------------------------------------------------------
A: ¿Cuál es la canción más antigua de la lista? ✓?
B: ¿Qué artista aparece más veces en esta lista? ✓?
C: ¿Qué país tiene más artistas en esta lista? ✓?
D: ¿Cuantas canciones distintas hay por cada idioma? ✓?
E: ¿Cuál es el continente con más apariciones en la lista? ✓?
F: ¿Qué canción ha estado más % de tiempo al año como número 1? ✓?   """

import requests
from bs4 import BeautifulSoup
import sqlite3

# Método para obtener los datos de la Wikipedia
def get_database(response):
	data_list = []

	if response.status_code == 200:
		soup = BeautifulSoup(response.text, "html.parser")
		table = soup.find("table", class_="wikitable")

		rows = table.find_all("tr")[1:]  # Para excluir el encabezado

		for row in rows:
			columns = row.find_all("td")
			if len(columns) >= 5:
				tema = columns[0].text.strip()
				interprete = columns[1].text.strip()
				anio = columns[2].text.strip()
				semanas = columns[3].text.strip()
				pais = columns[4].text.strip()

				# Creación del dict. con sus Keys
				data_dict = {
					"Tema": tema,
					"Intérprete": interprete,
					"Año": anio,
					"Semanas": semanas,
					"País": pais,
					"Idioma": "",
					"Continente": ""
				}
				data_list.append(data_dict)

	return data_list

# Método para llenar la base de datos con los datos de la URL
def fill_database(conn, url):
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS top_music (tema text, interprete text, año int, semanas int, pais text, idioma text, continente text)')

	response = requests.get(url)
	data_list = get_database(response)

	for data in data_list:
		cursor.execute("INSERT INTO top_music (tema, interprete, año, semanas, pais, idioma, continente) VALUES (?, ?, ?, ?, ?, ?, ?)",
					   (data['Tema'], data['Intérprete'], data['Año'], data['Semanas'], data['País'], data['Idioma'], data['Continente']))

	conn.commit()
	print("Datos insertados en la base de datos correctamente.")

# Método para obtener los registros de la base de datos en forma de lista de diccionarios
def get_database_records(conn):
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM top_music')
	rows = cursor.fetchall()

	records = []
	for row in rows:
		record = {
			"Tema": row[0],
			"Intérprete": row[1],
			"Año": row[2],
			"Semanas": row[3],
			"País": row[4],
			"Idioma": row[5],
			"Continente": row[6]
		}
		records.append(record)

	return records

# Método gral. del programa
def top_songs():
	conn = sqlite3.connect('C:/Users/joanc/OneDrive/Escritorio/Python - Deusto/M7_BasesDatos_DesarrolloWeb/Prueba/music.db')
	if conn:
		print("Conexión establecida correctamente")

	url = "https://es.wikipedia.org/wiki/Anexo:Sencillos_n%C3%BAmero_uno_en_Espa%C3%B1a#N%C3%BAmeros_uno:_D%C3%A9cada_1970s"
	fill_database(conn, url)
	records = get_database_records(conn)

	conn.close()

	# Imprimir los registros obtenidos de la base de datos
	for record in records:
		print(record)

# Llamada al programa
top_songs()
