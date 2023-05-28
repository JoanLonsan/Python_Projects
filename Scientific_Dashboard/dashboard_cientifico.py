import csv
import json
import matplotlib.pyplot as plt

# Method to get data from a .csv file and convert it to JSON format
def get_data_to_json():
	results = []
	# Open the .csv file with UTF-8 encoding
	with open('Proyecto_3.csv', encoding='utf-8') as File:
		reader = csv.DictReader(File)
		# Read and store the data in the results list
		for row in reader:
			results.append(row)
	
	# Create a dictionary to store the aggregated data
	aggregated_data = {}

	# Iterate over the data and perform data aggregation
	for row in results:
		fecha = row['date']
		provincia = row['province']
		num_def = int(row['num_def'])
		new_cases = int(row['new_cases'])
		num_hosp = int(row['num_hosp'])
		num_uci = int(row['num_uci'])

		# Group by day of the week and province
		dia_semana = fecha.split(',')[0].strip()
		if dia_semana not in aggregated_data:
			aggregated_data[dia_semana] = {}
		if provincia not in aggregated_data[dia_semana]:
			aggregated_data[dia_semana][provincia] = {
				'num_def': num_def,
				'new_cases': new_cases,
				'num_hosp': num_hosp,
				'num_uci': num_uci
			}
		else:
			aggregated_data[dia_semana][provincia]['num_def'] += num_def
			aggregated_data[dia_semana][provincia]['new_cases'] += new_cases
			aggregated_data[dia_semana][provincia]['num_hosp'] += num_hosp
			aggregated_data[dia_semana][provincia]['num_uci'] += num_uci

	# Save the JSON dictionary to a file
	with open('dashboard_cientifico.json', 'w', encoding='utf-8') as json_file:
		json.dump(aggregated_data, json_file, indent=4, ensure_ascii=False)
	
	# Uncomment to see data from json printed
	"""# Read the JSON file
	with open('dashboard_cientifico.json', 'r', encoding='utf-8') as json_file:
		data = json.load(json_file)
		# Print the contents of the JSON file
		print(data)"""

def load_data():
	with open('dashboard_cientifico.json', 'r', encoding='utf-8') as json_file:
		data = json.load(json_file)
	return data

# Generate and display the graph for defunciones
def show_defunciones(data):
	x = []
	y = []
	# Iterate over the data to extract x and y values
	for date in data:
		for province in data[date]:
			defunctions = data[date][province]['num_def']
			# Add the x and y values to the lists
			x.append(date)
			y.append(defunctions)
	# Plot the graph
	plt.plot(x, y)
	plt.title('Defunciones')
	plt.xticks(rotation=90)
	plt.show()

# Generate and display the graph for casos
def show_casos(data):
	x = []
	y = []
	for date in data:
		for province in data[date]:
			cases = data[date][province]['new_cases']
			x.append(date)
			y.append(cases)
	plt.plot(x, y)
	plt.title('Casos')
	plt.xticks(rotation=90)
	plt.show()

# Generate and display the graph for hospitalizados
def show_hospitalizados(data):
	x = []
	y = []
	for date in data:
		for province in data[date]:
			hospitalized = data[date][province]['num_hosp']
			x.append(date)
			y.append(hospitalized)
	plt.plot(x, y)
	plt.title('Hospitalizados')
	plt.xticks(rotation=90)
	plt.show()

# Generate and display the graph for UCI
def show_uci(data):
	x = []
	y = []
	for date in data:
		for province in data[date]:
			uci = data[date][province]['num_uci']
			x.append(date)
			y.append(uci)
	plt.plot(x, y)
	plt.title('UCI')
	plt.xticks(rotation=90)
	plt.show()

# Generate and display the pie graph for defunciones
def show_top_province_defunciones(data):
	defunciones = {}
	for date in data:
		for province in data[date]:
			defunciones[province] = data[date][province]['num_def']
	sorted_defunciones = sorted(defunciones.items(), key=lambda x: x[1], reverse=True)
	provinces, values = zip(*sorted_defunciones) 
	# Obtain provinces and values for first 6 provinces
	first_provinces = provinces[:6]
	first_values = values[:6]
	# Obtain provinces and values for the rest
	rest_values = values[6:]
	# Calculate rest piece of pie value
	rest_total_value = sum(rest_values)
	# Group provinces and values to display in the graph
	shown_provinces = list(first_provinces) + ['Resto']
	show_values = list(first_values) + [rest_total_value]
	# Create the 'explode' list with a value of 0.05 at the position of the maximum
	explode = [0.05 if prov in first_provinces[0] else 0 for prov in shown_provinces]
	max_prov = provinces[0]
	min_prov = provinces[-1]
	arrow_up = '\u2191'
	arrow_down = '\u2193'
	print(f"Maxima: {max_prov} {arrow_up}\nMínima: {min_prov} {arrow_down}")
	# Generate the pie chart with the specified values, labels, explode, and autopct formatting
	plt.pie(show_values, labels=shown_provinces, explode=explode, autopct='%1.1f%%')
	plt.title('Defunciones por Provincia')
	plt.axis('equal')
	plt.show()

# Generate and display the pie graph for casos
def show_top_province_casos(data):
	casos = {}
	for date in data:
		for province in data[date]:
			casos[province] = data[date][province]['new_cases']
	sorted_defunciones = sorted(casos.items(), key=lambda x: x[1], reverse=True)
	provinces, values = zip(*sorted_defunciones) 
	first_provinces = provinces[:6]
	first_values = values[:6]
	rest_values = values[6:]
	rest_total_value = sum(rest_values)
	shown_provinces = list(first_provinces) + ['Resto']
	show_values = list(first_values) + [rest_total_value]
	explode = [0.05 if prov in first_provinces[0] else 0 for prov in shown_provinces]
	max_prov = provinces[0]
	min_prov = provinces[-1]
	arrow_up = '\u2191'
	arrow_down = '\u2193'
	print(f"Maxima: {max_prov} {arrow_up}\nMínima: {min_prov} {arrow_down}")
	plt.pie(show_values, labels=shown_provinces, explode=explode, autopct='%1.1f%%')
	plt.title('Casos por Provincia')
	plt.axis('equal')
	plt.show()

# Generate and display the pie graph for hospitalizados
def show_top_province_hospitalizados(data):
	hospitalizados = {}
	for date in data:
		for province in data[date]:
			hospitalizados[province] = data[date][province]['num_hosp']
	sorted_defunciones = sorted(hospitalizados.items(), key=lambda x: x[1], reverse=True)
	provinces, values = zip(*sorted_defunciones) 
	first_provinces = provinces[:6]
	first_values = values[:6]
	rest_values = values[6:]
	rest_total_value = sum(rest_values)
	shown_provinces = list(first_provinces) + ['Resto']
	show_values = list(first_values) + [rest_total_value]
	explode = [0.05 if prov in first_provinces[0] else 0 for prov in shown_provinces]
	max_prov = provinces[0]
	min_prov = provinces[-1]
	arrow_up = '\u2191'
	arrow_down = '\u2193'
	print(f"Maxima: {max_prov} {arrow_up}\nMínima: {min_prov} {arrow_down}")
	plt.pie(show_values, labels=shown_provinces, explode=explode, autopct='%1.1f%%')
	plt.title('Hospitalizados por Provincia')
	plt.axis('equal')
	plt.show()

# Generate and display the pie graph for UCI
def show_top_province_uci(data):
	uci = {}
	for date in data:
		for province in data[date]:
			uci[province] = data[date][province]['num_uci']
	sorted_defunciones = sorted(uci.items(), key=lambda x: x[1], reverse=True)
	provinces, values = zip(*sorted_defunciones) 
	first_provinces = provinces[:6]
	first_values = values[:6]
	rest_values = values[6:]
	rest_total_value = sum(rest_values)
	shown_provinces = list(first_provinces) + ['Resto']
	show_values = list(first_values) + [rest_total_value]
	explode = [0.05 if prov in first_provinces[0] else 0 for prov in shown_provinces]
	max_prov = provinces[0]
	min_prov = provinces[-1]
	arrow_up = '\u2191'
	arrow_down = '\u2193'
	print(f"Maxima: {max_prov} {arrow_up}\nMínima: {min_prov} {arrow_down}")
	plt.pie(show_values, labels=shown_provinces, explode=explode, autopct='%1.1f%%')
	plt.title('UCI por Provincia')
	plt.axis('equal')
	plt.show()

def menu_ex2():
	while True:
		try:
			print("\033[1m Gráficas de defunciones, casos, hospitalizados y UCI\033[0m")
			choice = int(input("""\033[34m¿Qué gráfica te gustaría ver?\033[0m\n\033[34m1.\033[0m Defunciones\n\033[34m2.\033[0m Casos\n\033[34m3.\033[0m Hospitalizados\n\033[34m4.\033[0m UCI\n\033[34m5.\033[0m Volver\033[32m\nSelección: \033[0m"""))
			if choice == 1:
				data = load_data()
				show_defunciones(data)
			elif choice == 2:
				data = load_data()
				show_casos(data)
			elif choice == 3:
				data = load_data()
				show_hospitalizados(data)
			elif choice == 4:
				data = load_data()
				show_uci(data)
			# Back to Main Menu
			elif choice == 5:
				print("\033[3mVolviendo al menú anterior...\033[0m")
				break
			# Save program to close if number out of range
			else:
				print("\033[91mSelección inválida. Escoja de nuevo una opción.\033[0m")
		# Save program to close if input isalpha
		except ValueError:
			print("\033[91mError: Entrada inválida. Por favor, introduce un número.\033[0m")

def menu_ex3():
	while True:
		try:
			print("\033[1m Provincias más afectadas\033[0m")
			choice = int(input("""\033[34m¿Qué gráfica te gustaría ver?\033[0m\n\033[34m1.\033[0m Defunciones\n\033[34m2.\033[0m Casos\n\033[34m3.\033[0m Hospitalizados\n\033[34m4.\033[0m UCI\n\033[34m5.\033[0m Volver\033[32m\nSelección: \033[0m"""))
			if choice == 1:
				data = load_data()
				show_top_province_defunciones(data)
			elif choice == 2:
				data = load_data()
				show_top_province_casos(data)
			elif choice == 3:
				data = load_data()
				show_top_province_hospitalizados(data)
			elif choice == 4:
				data = load_data()
				show_top_province_uci(data)
			# Back to Main Menu
			elif choice == 5:
				print("\033[3mVolviendo al menú anterior...\033[0m")
				break
			# Save program to close if number out of range
			else:
				print("\033[91mSelección inválida. Escoja de nuevo una opción.\033[0m")
		# Save program to close if input isalpha
		except ValueError:
			print("\033[91mError: Entrada inválida. Por favor, introduce un número.\033[0m")

def main_menu():
	while True:
		try:
			print("\033[1m DASHBOARD CIENTÍFICO\033[0m")
			choice = int(input("""\033[34mQué quieres consultar?\033[0m\n\033[34m1.\033[0m Gráficas de defunciones, casos, hospitalizados y UCI\n\033[34m2.\033[0m Provincias más afectadas\n\033[34m3.\033[0m Salir\033[32m\nSelección: \033[0m"""))
			# Exercise 2
			if choice == 1:
				menu_ex2()
			# Exercise 3
			elif choice == 2:
				menu_ex3()
			# Exit program
			elif choice == 3:
				print("\033[3mSaliendo del programa...\033[0m\nNo dude en consultarme de nuevo si lo necesita")
				break
			else:
				print("\033[91mSelección inválida. Escoja de nuevo una opción.\033[0m")
		except ValueError:
			print("\033[91mError: Entrada inválida. Por favor, introduce un número.\033[0m") 

# General method of the program
def main():
	# Exercise 1
	get_data_to_json()
	# Exercises 2 and 3
	main_menu()

main()
