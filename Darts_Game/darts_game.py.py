def darts_game():
	# Create Dictionary
	players = {}
	# Assign name to every player.
	for i in range(4):
		player = input(f"Nombre de jugador {i+1}: ")
		# Apply starting score: 121
		players[player] = 121
	# Round Control	
	for round in range(3):
		print(f"Ronda {round+1} de 3")
		# Tuple creation for winner/winners.
		winners = []
		# Each player 3 darts control
		for player, score in players.items():
			print(f"Tira {player}")
			# Sum each score of each dart over 3
			roundScore = sum(int(input(f"Puntuación del tiro {dart+1}: ")) for dart in range(3))
			# Modify player score
			score -= roundScore
			players[player] = score
			# OPTION A: Print each player score after each player's round
			# print (f"Puntuación de{player}: {score}")
			# Check if we have a winner and return name
			if score <= 0:
				winners.append(player)
			else:
				continue
		# OPTION B: Print all player scores after each round
		print(f"Puntuación tras la ronda {round+1}")
		for player, score in players.items():
			print(f"{player}: {score}")
		if winners:
			return winners
	# Return 0 if we finish 3rd round w/out a winner
	return 0

# Function call	
result = darts_game()
# Check if function return is 0 or not, to print winner's name
if result != 0:
	print("Ganador/es:", ", ".join(result))
else:
	print("La partida ha llegado a la 3ª ronda sin ningún ganador")
