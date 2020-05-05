```
_                                   
| |_  ___ ._ _  ___ ._ _ _  ___ ._ _ 
| . |<_> || ' |/ . || ' ' |<_> || ' |
|_|_|<___||_|_|\_. ||_|_|_|<___||_|_|
               <___'
```
               

Run the project with python hangman.py inside the directory for the game
Hangman will pick a random word (of at least 4 characters) out of words.txt
Your goal is to guess the word either one letter at a time, or by guessing the whole word
Incorrectly guessed letters are shown at the bottom of the game window, labeled 'Guesses'

'Reset'     choose a new word, and reset the progress of the hanging man
'Submit'    guess a letter/word
'Choose'    manually select your own word, have your friends try and guess it
'Reveal'    reveal the hidden word 

Upon winning or losing a game, a pop-up window will appear revealing the word and
stating that you have won or lost the game. On the pop-up window are several choice buttons:

'Quit'        close the pop-up window/game window and exit the game
'Reset Game'  close the pop-up window and reset the game to the initial play state to play again


*NOTE*: Fedora users may have to run: "sudo dnf install python3-tkinter" to install the tkinter python
module if presented with a 'ModuleNotFoundError' when attempting to run the game
