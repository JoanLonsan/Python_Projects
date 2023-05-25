# FRIENDS DATABASE

This code represents a program that allows you to create a database of friends and their musical preferences. It uses classes and functions to collect and display the data.


## Classes

Friend
The Friend class represents a friend and has the following attributes:

name: The name of the friend.
dni: The DNI (identification number) of the friend.
locality: The locality (city or town) where the friend resides.
country: The country where the friend resides.
It also has a method show_friend_data() that displays the personal data of the friend.


## MusicalPreferences

The MusicalPreferences class represents the musical preferences of a friend and has the following attributes:

favorite_song: The favorite song of the friend.
group: The music group the friend likes.
genre: The musical genre preferred by the friend.
It also has a method show_music_data() that displays the musical preferences of the friend.


## FriendMusicalPref

The FriendMusicalPref class is a subclass that inherits from both the Friend and MusicalPreferences classes. It combines the personal data and musical preferences of a friend. It inherits the attributes and methods from both parent classes.


## Functions

get_friend_data()
This function prompts the user to enter the personal data of a friend (name, DNI, locality, and country) and returns the entered values.

get_music_data()
This function prompts the user to enter the musical preferences of a friend (favorite song, music group, and genre) and returns the entered values.

main()
The main() function is the entry point of the program. It creates an empty list to store friends' data. It prompts the user to enter the friend's data and musical preferences repeatedly until the user chooses to stop. Each friend's data is stored in an instance of the FriendMusicalPref class and added to the list. The user is then given the option to display the list of friends and their musical preferences.


## Usage

To use this program, run it in a Python environment. Follow the prompts to enter the personal data and musical preferences of your friends. You can choose to add multiple friends or view the list of all friends and their musical preferences.

Note: This code uses color codes for console output to enhance readability. These color codes may not work in all console environments.