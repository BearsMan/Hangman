import random
import tkinter as tk


window = tk.Tk()
window.title ("Hangman")
wordlabel = tk.Label(window, text="welcome to hangman")
wordlabel.pack()
words = ["chicken", "linguine", "soup", "greenbeans", "mashed potatoes"]
word = random.choice(words)
guesses = []
max_guesses = 5
print("welcome to hangman")
print("guess up to 5 incorrectly and, you lose")
print("the word has", len (word), "and a letters")
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