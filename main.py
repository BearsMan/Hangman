import random
import tkinter as tk
# variables to set the game up.
# sets up a window
window = tk.Tk()
# create a window title
window.title ("Hangman")

words = ["chicken", "linguine", "soup", "greenbeans", "mashed potatoes"]
word = random.choice(words)
wordLength = len(word)
line = "_"* wordLength
guesses = []
max_guesses = 5

# adding window title
wordlabel = tk.Label(window, text="welcome to hangman", font=("times new roman", 14, "bold",))
wordlabel.pack()
# intro for label
introLabel = tk.Label (window, text="how to play(click on the console window \n and it will guess between 1 to 5 words. \n I recommend that you go back to think of you think what the word should be") 
introLabel.pack()
word_Line = tk.Label(window, text= line)

# sets up a word label for each word. 
word_Line.pack()

# setup input
userInput = tk.Entry(window)
userInput.pack()
guessremains = tk.Label(window, text=f"guesses remaining {max_guesses}")
guessremains.pack()
# print statements for start of the game.
print("guess up to 5 words incorrectly and, you lose")
print(wordlabel.pack)
print("the word has", len (word), "and a letters")
# game loops (logic)
while max_guesses > 0:
  word_state = ""
  for letter in word:
    if letter in guesses:
      word_state += letter
    else: word_state += "_"
  print ("Current word" , word_state)
  guess = input ("guess a letter")
  guesses.append(guess)
  if guess in word:
    print("correct")
  else:
    print("incorrect")
    max_guesses -= 1
  if set(word) <= set(guesses):
    print("you win", "the word was", word)
    break
  elif max_guesses == 0:
    print("you lose")
    break