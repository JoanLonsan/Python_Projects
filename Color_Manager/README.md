# Color Manager

This repository contains a Python program that allows users to manage a list of colors and users. The program provides various options to add, sort, assign colors, delete users, and display the list of users.

## Getting Started

To run the program, follow these steps:

1. Make sure you have Python installed on your machine.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to execute the program:
	python color_manager.py

## Program Description

The program consists of the following files:
- color_manager.py: The main Python program containing the color management functionality.

## Program Features

The program provides the following options:

1. Add Color: Allows you to add a new color to the list.
2. List Colors: Displays the current list of colors.
3. Sort Colors: Sorts the list of colors in alphabetical order.
4. Add User: Adds a new user to the list of users.
5. Assign Colors: Assigns a random color to each user from the available colors.
6. Delete User: Deletes a user from the list.
7. Show Users: Displays the list of users' names.
8. Exit: Exits the program.


## Usage

When you run the program, a menu will be displayed with the available options. You can select an option by entering the corresponding number. Follow the on-screen prompts to perform the desired actions.

Please note the following:

When adding a color, make sure to enter the color name in lowercase.
When adding a user, if there are more users than colors, a color will be automatically added to the list before adding the user.
The program prevents assigning the same color to multiple users.

## Example
Here is an example session of running the program:


----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List of Colors Alphabetically
4: Add User
5: Assign Random Colors to Users
6: Delete User
7: Show Users
8: Exit
Select an action: 2

['amarillo', 'azul', 'verde', 'rojo']

----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List of Colors Alphabetically
4: Add User
5: Assign Random Colors to Users
6: Delete User
7: Show Users
8: Exit
Select an action: 4

Name of the new user: John

----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List of Colors Alphabetically
4: Add User
5: Assign Random Colors to Users
6: Delete User
7: Show Users
8: Exit
Select an action: 5

{'Nombre': 'John', 'Color': 'verde'}

----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List of Colors Alphabetically
4: Add User
5: Assign Random Colors to Users
6: Delete User
7: Show Users
8: Exit
Select an action: 6

1: John
Select the number of the user to delete: 1

----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List of Colors Alphabetically
4: Add User
5: Assign Random Colors to Users
6: Delete User
7: Show Users
8: Exit
Select an action: 7

Josep
Claudio
Isabel
Sheila

----------------------MENU----------------------
1: Add Color
2: List Colors
3: Sort List