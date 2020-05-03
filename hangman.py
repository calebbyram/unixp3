import random
import tkinter
from tkinter import *

window = Tk()
window.title("Hangman")
window.geometry("600x400")

gameImage = tkinter.PhotoImage(file=image)
gameImageLabel = tkinter.Label(window, image=gameImage)
gameImageLabel.grid(row=0, column=0)

window.mainloop()

chosenWord = ""
guessedLetters = set([])


def choseNewWord():
    with open('words.txt') as file:
        wordDict = [line.rstrip('\n') for line in file if len(line) > 4]
    global chosenWord
    chosenWord = random.choice(wordDict)

def guessLetter(letter):
    guessedLetters.add(letter)

def wordProgress():
    #underscores = "_"*len(chosenWord)
    underscores = [c if c in guessedLetters else "_" for c in chosenWord]
    return underscores




