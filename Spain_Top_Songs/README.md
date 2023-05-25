# TOP SONGS IN SPAIN

This repository contains a Python script that interacts with a SQLite database to answer specific questions about a list of songs. The script executes various SQL queries to retrieve information from the database and prints the results to the console.

## Prerequisites

To run this script, you need to have Python installed on your system. Additionally, ensure that the sqlite3 module is available.

## Usage

1. Clone this repository to your local machine or download the script file.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the following command to execute the script:
	python script.py
Make sure you have Python properly set up in your environment.
4. The script will establish a connection with the SQLite database and execute several SQL queries to answer specific questions about the song list. The results will be displayed in the console.

## Questions Answered

The script answers the following questions about the song list:

- A: ¿Cuál es la canción más antigua de la lista?
	(Eng) What is the oldest song on the list?
- B: ¿Qué artista aparece más veces en esta lista?
	(Eng) Which artist appears the most times on this list?
- C: ¿Qué país tiene más artistas en esta lista?
	(Eng) Which country has the most artists on this list?
- D: ¿Cuantas canciones distintas hay por cada idioma?
	(Eng) How many different songs are there for each language?
- E: ¿Cuál es el continente con más apariciones en la lista?
	(Eng) Which continent has the most appearances on the list?
- F: ¿Qué canción ha estado más % de tiempo al año como número 1?
	(Eng)  Which song has spent the highest percentage of time as number 1 throughout the year?

## Database

The script interacts with a SQLite database file named canciones.db. If the database file does not exist, the script creates it and populates it with the necessary data. The database contains a single table named Canciones with the following columns:

- Tema (TEXT): The title of the song.
- Intérprete (TEXT): The artist of the song.
- Año (INTEGER): The year the song was released.
- Semanas (INTEGER): The number of weeks the song has been on the list.
- País (TEXT): The country associated with the song.
- Idioma (TEXT): The language of the song.
- Continente (TEXT): The continent associated with the song.

## Extra

The auxiliary code retrieves data from a Wikipedia page, populates a SQLite database with the extracted information, and provides methods to retrieve and manipulate the database records. 
It uses the requests library to fetch the web page, BeautifulSoup for HTML parsing, and sqlite3 for database operations. 
The main program executes these functions to scrape a specific Wikipedia page and store the data in the database.