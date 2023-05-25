from pip._vendor import requests
import os
import sys

# Función para obtener datos desde la url entrante
def get_data(url):
	response = requests.get(url)
	return response.json()

# Función para obtener listado con los equipos
def get_teams(data):
	teams = data['clubs']
	return teams

# Función para mostrar los datos
def show_data(teams):
	for team in teams:
		name = team.get('name')
		if name:
			print("Club:", name)
			code = team.get('code')
			if code:
				print("Código:", code)
				print("-----")
			else:
				print("Código: No disponible")
				print("-----")

# Función para guardar datos en un .txt. Si no existe, lo crea
def save_data(teams):
	file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Equipos.txt")
	with open(file, "w", encoding='utf-8') as file:
		file.write(f"Equipos en la Liga: {len(teams)}\n----------------------\n")
		for team in teams:
			file.write(f"\nNombre: {team['name']}\n")
			file.write(f"Código: {team['code']}\n")
			file.write("-----")

# Menú de selección
def menu():
	print("\033[34mSeleccione una liga:\033[0m" +
		"\n1: Española" +
		"\n2: Alemana" +
		"\n3: Italiana" +
		"\n4: Austríaca" +
		"\n5: Inglesa" +
		"\n6: Salir")
	choice = input("\033[32mEscoja el número de la opción deseada: \033[0m")
	return choice


# Links a los que recurrir
def main():
	leagues = {
		'1': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/es.1.clubs.json',
		'2': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/de.1.clubs.json',
		'3': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/it.1.clubs.json',
		'4': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/at.2.clubs.json',
		'5': 'https://raw.githubusercontent.com/openfootball/football.json/master/2020-21/en.1.clubs.json'
	}

	# Gestión de la opción escogida
	choice = menu()
	# Opción para SALIR
	if choice == '6':
		sys.exit()
	# Gestión de opción por Liga
	if choice in leagues:
		url = leagues[choice]
		data = get_data(url)
		teams = get_teams(data)
		show_data(teams)
		save_data(teams)
		print("\033[34mEquipos en la Liga: \033[0m", len(teams))
		print("\033[32mDatos guardados en: \"Equipos.txt\"\033[0m")
	# Gestión de Errores sin salir del programa
	else:
		print("\033[31mSelección errónea\n\033[0m")
		main()

main()
