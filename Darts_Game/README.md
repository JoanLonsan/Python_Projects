# Darts Game

This code represents a simple darts game where four players compete against each other over three rounds. The objective of the game is to reach a score of exactly 0 by subtracting the points earned with each dart throw from the starting score of 121.

## Setup

- The game starts by creating an empty dictionary to store the players' names and scores.
- The code prompts the user to enter the names of the four players and assigns each player a starting score of 121.

## Gameplay

- The game consists of three rounds. For each round, the code prompts each player to take their turn.
- During a player's turn, their name is displayed, and they are asked to enter the score they achieved with each of their three dart throws.
- The scores from the three dart throws are summed up to calculate the round score.
- The player's score is then reduced by the round score.
- If a player's score becomes less than or equal to 0, they are considered a winner for that round.
- After each player has taken their turn, the code displays the updated scores for all players.

## Results

- After the three rounds, the code checks if there is a winner by examining the returned value from the `darts_game()` function.
- If there is a winner (i.e., the returned value is not 0), the code prints the name(s) of the winner(s).
- If there is no winner after the third round, the code prints a message indicating that the game has ended without a winner.

Note: There are two options commented in the code:
- OPTION A: If you uncomment the line that prints each player's score after each player's round, it will display the scores during the game.
- OPTION B: If you uncomment the block that prints all player scores after each round, it will display the scores only at the end of each round.