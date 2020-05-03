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


"add a letter to the list of guessed letters. Returns false for new incorrect guesses, else true"
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
    global guessWordLabel
    underscores = [c if c in guessedLetters else "_" for c in chosenWord]
    str1 = " "
    print("getWordProgress: ", str1.join(underscores))
    return (str1.join(underscores))


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
userWordProgress = getWordProgress()

# Game image initial
gameImage = tkinter.PhotoImage(file=image)
gameImageLabel = tkinter.Label(window, image=gameImage)
gameImageLabel.grid(row=1, column=0)

# Guess entry box and label
tkinter.Label(window, text="Guess Letter/Word").grid(row=3, column=1)
userGuess = tkinter.Entry(window)
userGuess.grid(row=3, column=2)

#submit user guess
tkinter.Button(window, text="Submit", command=guessLetter(userGuess.get())).grid(row=3, column=3)

#User custom word selection
userWord = tkinter.Entry(window)
userWord.grid(row=0, column=1)
tkinter.Button(window, text="Choose Word", command=chooseNewWord()).grid(row=0, column=2)

#display the current guess progress
guessWordLabel = Label(window, text=userWordProgress)
guessWordLabel.grid(row=1, column =2)
tkinter.Label(window, text="WORD: ").grid(row=1, column=1)

# testing functions here
randomNewWord()
guessLetter("a")
guessLetter("e")
guessLetter("i")
guessLetter("o")
guessLetter("u")
guessLetter("y")
guessLetter("s")
guessLetter("r")
guessLetter("t")
print(chosenWord)
print(getIncorrectGuesses())
print(getCorrectGuesses())
print(getWordProgress())

window.mainloop()




