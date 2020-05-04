import random
import tkinter
from tkinter import *

image = "hang0.png"
chosenWord = ""
guessedLetters = []
guessedWords = []

def randomNewWord():
    with open('words.txt') as file:
        wordDict = [line.rstrip('\n') for line in file if len(line) > 4]
    global chosenWord
    chosenWord = random.choice(wordDict)

def chooseNewWord():
    reset()
    global chosenWord
    userWordString = userWord.get()
    chosenWord = userWordString
    getWordProgress()
    userWord.delete(0, 'end')

def guess():
    input = userGuess.get()
    userGuess.delete(0, 'end')
    if(len(input) == 1):
        guessLetter(input)
    if(len(input) > 1):
        guessWord(input)

    getWordProgress()
    counter = len(getIncorrectGuesses()) + len(getIncorrectWord())

    if(counter > 0 and counter < 7):
        if gameLost():
            gameLosePopUp()
        displayBadGuesses()
        global image
        image = "hang" + str(counter) + ".png"

        icon = tkinter.PhotoImage(file=image)
        gameImageLabel.config(image=icon)
        gameImageLabel.image = icon

#"add a letter to the list of guessed letters. Returns false for new incorrect guesses, else true"
def guessLetter(letter):
    if letter not in guessedLetters:
        guessedLetters.append(letter)
        return letter in chosenWord
    return True

#"same as guessLetter but for words"
def guessWord(word):
    if word not in guessedWords:
        guessedWords.append(word)
        return word == chosenWord
    return True

#"returns a string of underscores and correctly guessed letters corresponding to the chosen word"
def getWordProgress():
    # underscores = "_"*len(chosenWord)
    print("chosenWord: ", chosenWord)
    underscores = [c if c in guessedLetters else "_" for c in chosenWord]
    str1 = " "
    str2 = str1.join(underscores)
    if gameWon():
        gameWonPopUp()
    if chosenWord in guessedWords:
        str2 = chosenWord
    #print("getWordProgress: ", str2)
    guessWordLabel.config(text=str2)
    #return (str1.join(underscores))


#"returns a list of each incorrectly guessed letter"
def getIncorrectGuesses():
    orderedBadGuess = []
    for letters in guessedLetters:
        if letters not in chosenWord:
            orderedBadGuess.append(letters)
    return orderedBadGuess

def getIncorrectWord():
    orderedBadGuess = []
    for letters in guessedWords:
        if letters != chosenWord:
            orderedBadGuess.append(letters)
    return orderedBadGuess

def getCorrectGuesses():
    orderedGuess = []
    for letters in guessedLetters:
        if letters in chosenWord:
            orderedGuess.append(letters)
    return orderedGuess

#"returns if all letters have been guessed correctly, or if the chosen word has been guessed"
def gameWon():
    if chosenWord in guessedWords:
        return True
    for letter in chosenWord:
        if letter not in guessedLetters:
            return False
    return True

def gameLost():
    return len(getIncorrectGuesses()) + len(getIncorrectWord()) > 5

def reset():
    global image
    image = "hang0.png"
    randomNewWord()
    global guessedLetters
    guessedLetters = []
    global guessedWords
    guessedWords = []

    getWordProgress()

    icon = tkinter.PhotoImage(file=image)
    gameImageLabel.config(image=icon)
    gameImageLabel.image = icon

    badGuessLetters.config(text="")

def displayBadGuesses():
    str1 = ","
    str2 = str1.join(getIncorrectGuesses())
    badGuessLetters.config(text=str2)

def gameWonPopUp():
    toplevelWin = Toplevel()
    Winlabel1 = Label(toplevelWin, text="You Win!")
    Winlabel1.pack()
    labelText = "Word Was: " + str(chosenWord)
    Winlabel2 = Label(toplevelWin, text=labelText, width = 50)
    Winlabel2.pack()

    def closeWindowOnWin():
        toplevelWin.destroy()
        window.destroy()
    def resetWindow():
        toplevelWin.destroy()
        reset()

    quitButton = Button(toplevelWin, text="Quit", command = closeWindowOnWin)
    resetButton = Button(toplevelWin, text = "Reset Game", command = resetWindow)
    quitButton.pack()
    resetButton.pack()


def gameLosePopUp():
    toplevelLose = Toplevel()
    Loselabel1 = Label(toplevelLose, text="You Lose!")
    Loselabel1.pack()
    labelText = "Word Was: " + str(chosenWord)
    Loselabel2 = Label(toplevelLose, text=labelText, width=50)
    Loselabel2.pack()

    def closeWindowOnLose():
        toplevelLose.destroy()
        window.destroy()

    def resetWindow():
        toplevelLose.destroy()
        reset()

    quitButton = Button(toplevelLose, text="Quit", command=closeWindowOnLose)
    resetButton = Button(toplevelLose, text="Reset Game", command=resetWindow)
    quitButton.pack()
    resetButton.pack()

def displayChosenWord():
    guessWord(chosenWord)
    getWordProgress()

window = Tk()
window.title("Hangman")
window.geometry("600x400")

randomNewWord()
#print("chosen word: ", chosenWord)

# Game image initial
gameImage = tkinter.PhotoImage(file=image)
gameImageLabel = tkinter.Label(window, image=gameImage)
gameImageLabel.grid(row=1, column=0)

# Guess entry box and label
tkinter.Label(window, text="Guess Letter/Word").grid(row=3, column=1)
userGuess = tkinter.Entry(window)
userGuess.grid(row=3, column=2)

#User custom word selection
tkinter.Label(window, text="Custom Word: ").grid(row=0, column=1)
userWord = tkinter.Entry(window)
userWord.grid(row=0, column=2)
tkinter.Button(window, text="Choose", command=chooseNewWord).grid(row=0, column=3)

#display the current guess progress
guessWordLabel = Label(window)
guessWordLabel.config(text=getWordProgress())
guessWordLabel.grid(row=1, column =2)
tkinter.Label(window, text="WORD: ").grid(row=1, column=1)

#submit user guess
tkinter.Button(window, text="Submit", command=guess).grid(row=3, column=3)

#reset button
tkinter.Button(window, text="Reset", command=reset).grid(row=3, column=0)

#Reveal button
tkinter.Button(window, text="Reveal", command=displayChosenWord).grid(row=4, column=0)

#display bad guesses
badGuessLabel = Label(window)
badGuessLabel.config(text="Guesses: ")
badGuessLabel.grid(row=4, column =1)


badGuessLetters = Label(window)
badGuessLetters.grid(row=4, column=2)


window.mainloop()




