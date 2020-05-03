import random
import tkinter
from tkinter import *

image = "hang0.png"
chosenWord = ""
guessedLetters = []

def randomNewWord():
    with open('words.txt') as file:
        wordDict = [line.rstrip('\n') for line in file if len(line) > 4]
    global chosenWord
    chosenWord = random.choice(wordDict)

def chooseNewWord(newWord):
    global chosenWord
    chosenWord = newWord

"add a letter to the list of guessed letters. Returns false for new incorrect guesses, else true"
def guessLetter(letter):
    if letter not in guessedLetters:
        guessedLetters.append(letter)
        return letter in chosenWord
    return True

"returns a string of underscores and correctly guessed letters corresponding to the chosen word"
def getWordProgress():
    #underscores = "_"*len(chosenWord)
    underscores = [c if c in guessedLetters else "_" for c in chosenWord]
    str1 = ""
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

window = Tk()
window.title("Hangman")
window.geometry("600x400")

#Game image initial
gameImage = tkinter.PhotoImage(file=image)
gameImageLabel = tkinter.Label(window, image=gameImage)
gameImageLabel.grid(row=0, column=0)

#Guess entry box and label
tkinter.Label(window, text="Guess Letter/Word").grid(row=2, column=1)
userGuess = tkinter.Entry(window)
userGuess.grid(row=2, column=2)

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






