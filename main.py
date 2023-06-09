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
display = "_" * wordLength
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
# print statements for start of the game.
print("guess up to 5 words incorrectly and, you lose")
print(wordlabel.pack)
print("the word has", len (word), "and a letters")
# color for the window
guessremains = tk.Label(window, text=f"Guesses remaining: {max_guesses}", font=("Times New Roman", 12, "bold"), fg="blue")
guessremains.pack()

letter_guess = tk.Label(window, text=f"Guessed Letters: {','.join(guesses)}")
letter_guess.pack()
# game loops (logic)
# functions (to handle game logic)
def handle_Input():
  global max_guesses, display, guesses, word_length
  guess = userInput.get().lower()
  userInput.delete(0, tk.END)
  if not guess.isalpha() or len(guess) != 1:
    return
  if guess in word:
      for i in range(wordLength):
        if word[i] == guess:
          display = display[:i] + guess + display[i + 1:]
      word_length = len(display)
  else:
      max_guesses -= 1
      guessremains.config(text=f"Guesses remaining: {max_guesses}")
  guesses.append(guess)
  letter_guess.config(text=f"Guessed Letters: {', '.join(guesses)}")
  word_Line.config(text=display)

# checking if the game is over
  if max_guesses == 0 or display == word:
      userInput.config(state=tk.DISABLED)
      if max_guesses == 0:
        tk.messagebox.showinfo("Hangman", "You Lose!")
      else:
        tk.messagebox.showinfo("Hangman", "You Win")
userInput.bind("<Return>", lambda event: handle_Input())

# Start the tkinter mainloop
window.mainloop()