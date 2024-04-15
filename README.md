# Music Wheel coding project

You have been tasked with making a game that allows a user to practice their music theory.

Please refer to the following videos:

<https://www.justinguitar.com/guitar-lessons/the-note-circle-bc-152>

<https://www.justinguitar.com/guitar-lessons/note-circle-with-a-jam-buddy-mt-106>

The game is to be played in a terminal.

## The user experience

1. When the user starts the game they will be presented with 2 random notes (eg A# and Eb)
2. The user will get to guess how many semitones are between the notes. They can enter a number
3. If the user guesses correctly,  tell them they are correct and let them play the game again
4. If the user guesses incorrectly, tell them that they are incorrect and let them keep trying
5. The user should be able to "give up" at any time. When the user gives up then:
   1. display the correct answer
   2. give the user the option to start the game over again

## How To Run

In order to run the python file in your terminal please follow the steps below:

1. Clone the repo to your local machine
2. Open the terminal and navigate to the folder where the repo is located
3. Run the following command in your terminal: `python3 notecircle.py`
4. Follow the instructions in the terminal to play the game

## How To Play The Game

1. When the game starts, you will be asked to enter a 1 to begin the game or a Q to quite the game.
2. If you enter 1, then you will be presented with 2 random notes (eg A# and Eb)
3. You will get to guess how many semitones are between the notes. You can enter a number
4. If you guess correctly, you will be told that you are correct and you can play the game again
5. If you guess incorrectly, you will be told that you are incorrect and you can keep trying
6. You can "give up" at any time. When you give up then:
   1. The correct answer will be displayed
   2. You will be given the option to start the game over again
   3. If you choose to start the game over again, you will be presented with 2 new random notes
7. If you choose to quit the game, you will be thanked and told that the game has ended.

## How To Run Tests

In order to run the tests for the python file in your terminal please follow the steps below:

1. Clone the repo to your local machine
2. Open the terminal and navigate to the folder where the repo is located
3. Run the following command in your terminal: `python3 -m unittest discover`
4. The tests will run and the results will be displayed in the terminal

## Code Logic and Structure

The code is structured into 3 function sets:

### Getter Functions

1. The first function set is the `get_notes()` function set. This function set is responsible for generating the random notes that the user will be presented with. The `get_notes()` function set contains 2 functions:
   1. The `get_random_note()` function is responsible for generating a random note from the `note_circle` dictionary. The `note_circle` list contains all the notes that are used in the game. The `get_random_note()` function returns a random note from the `note_circle` list.
   2. The `get_notes()` function is responsible for calling the `get_random_note()` function twice and returning the 2 random notes that are generated. It is also responsible for ensuring that the same note is not used twice but it
   does allow in-harmonic notes to be selected.
2. The other function is the `get_key_by_value` function which is important for the look up functionality of the note-circle to ensure positioning on the table and for the `get_distance` function to calculate the distance between the notes.
3. The `get_distance` function is key to the game as the player must enter a guess and the function determines the distance between to notes. Its return value is used to determine if the player has guessed correctly or not.

### Game Functions

1. The game function are set into 3, name `game_start`, `game_play` and `game_retry`.
   1. The `game_start` function is responsible for the opening sequence of the game. It is responsible for asking the user if they would like to play the game or quit the game. The `game_start` function takes in 1 argument, the command to either start the game or quit the game.
   2. The `game_play` function is responsible for running the game. The `game_play` function takes in 2 arguments, the 2 notes that the user is presented with. The `game_play` function returns the number of semitones between the 2 notes that the user is presented with. The `game_play` function uses the `get_distance` to function to calculate the number of semitones between the 2 notes that the user is presented with.
   3. The `game_retry` function is responsible for asking the user if they would like to play the game again. The `game_retry` function prompts the user for input.
