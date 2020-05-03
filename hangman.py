import random
import tkinter
from tkinter import *

image = "hang0.png"
chosenWord = ""
guessedLetters = []
guessedWords = []
displayWord = ""

def randomNewWord():
    with open('words.txt') as file:
        wordDict = [line.rstrip('\n') for line in file if len(line) > 4]
    global chosenWord
    chosenWord = random.choice(wordDict)

def chooseNewWord():
    global chosenWord
    userWordString = userWord.get()
    chosenWord = userWordString

def guess():
    input = userGuess.get()
    if(len(input) == 1):
        guessLetter(input)
    if(len(input) > 1):
        guessWord(input)

    getWordProgress()
    counter = len(getIncorrectGuesses())

    if(counter > 0):
        global image
        image = "hang" + str(counter) + ".png"

        icon = tkinter.PhotoImage(file=image)
        gameImageLabel.config(image=icon)
        gameImageLabel.image = icon
    #turnsLeft.config(text="Turns Left: " + str(6 - badCounter))
    #if (counter == 6):
        #displayLose()

#"add a letter to the list of guessed letters. Returns false for new incorrect guesses, else true"
def guessLetter(letter):
    if letter not in guessedLetters:
        guessedLetters.append(letter)
        return letter in chosenWord
    return True

"same as guessLetter but for words"
def guessWord(word):
    if word not in guessedWords:
        guessedWords.append(word)
        return word == chosenWord
    return True

"returns a string of underscores and correctly guessed letters corresponding to the chosen word"
def getWordProgress():
    # underscores = "_"*len(chosenWord)
    underscores = [c if c in guessedLetters else "_" for c in chosenWord]
    str1 = " "
    str2 = str1.join(underscores)
    print("getWordProgress: ", str2)
    guessWordLabel.config(text=str2)
    #return (str1.join(underscores))


"returns a list of each incorrectly guessed letter"
def getIncorrectGuesses():
    orderedBadGuess = []
    for letters in guessedLetters:
        if letters not in chosenWord:
            orderedBadGuess.append(letters)
    return orderedBadGuess

def getCorrectGuesses():
    orderedGuess = []
    for letters in guessedLetters:
        if letters in chosenWord:
            orderedGuess.append(letters)
    return orderedGuess

"returns if all letters have been guessed correctly, or if the chosen word has been guessed"
def gameWon():
    if chosenWord in guessedWords:
        return True
    for letter in chosenWord:
        if letter not in guessedLetters:
            return False
    return True

def gameLost():
    return len(getIncorrectGuesses()) > 5

window = Tk()
window.title("Hangman")
window.geometry("600x400")

randomNewWord()
print("chosen word: ", chosenWord)

# Game image initial
gameImage = tkinter.PhotoImage(file=image)
gameImageLabel = tkinter.Label(window, image=gameImage)
gameImageLabel.grid(row=1, column=0)

# Guess entry box and label
tkinter.Label(window, text="Guess Letter/Word").grid(row=3, column=1)
userGuess = tkinter.Entry(window)
userGuess.grid(row=3, column=2)

#User custom word selection
userWord = tkinter.Entry(window)
userWord.grid(row=0, column=1)
tkinter.Button(window, text="Choose Word", command=chooseNewWord()).grid(row=0, column=2)

#display the current guess progress
guessWordLabel = Label(window)
guessWordLabel.config(text=getWordProgress())
guessWordLabel.grid(row=1, column =2)
tkinter.Label(window, text="WORD: ").grid(row=1, column=1)

#submit user guess
tkinter.Button(window, text="Submit", command=guess).grid(row=3, column=3)

# testing functions here
#randomNewWord()
#guessLetter("a")
#guessLetter("e")
#guessLetter("i")
#guessLetter("o")
#guessLetter("u")
#guessLetter("y")
#guessLetter("s")
#guessLetter("r")
#guessLetter("t")
#print(chosenWord)
#print(getIncorrectGuesses())
#print(getCorrectGuesses())
#print(getWordProgress())

window.mainloop()




