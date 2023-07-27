# pacMan Game
import tkinter as tk
import random
# create main window
window = tk.Tk()

# create name of title
window.title ("Pac Man")

# setup variables
width = 400
height = 400
cellsize = 30
squareSize = 50
moveDistance = 5
 
# classes and functions
class pacManGame:
   def __init__(self, window):
     self.window = window
     # think of tkinter as your friend to call methods
     self.canvas = tk.Canvas(window, width=width, height=height, bg = "red")
     self.canvas.pack()
     # Creating the moving square object
     self.pacman = self.canvas.create_arc (0, 0, squareSize, squareSize, start = 45, extent = 270, fill = "yellow")
  
  # create the controls to move the square using your keyboard arrow keys
     self.window.bind("<Up>", lambda event: self.move_pacman(0, -moveDistance))
     self.window.bind("<Down>", lambda event: self.move_pacman(0, moveDistance))
     self.window.bind("<Left>", lambda event: self.move_pacman(-moveDistance, 0))
     self.window.bind("<Right>", lambda event: self.move_pacman(moveDistance, 0))
   # create pallet window
   def createfood(self):
    self.food = []
    for i in range(30, width - cellsize, cellsize):
     for y in range(30, height - cellsize, cellsize):
      if (i, y) not in self.walls:
        self.food.append(self.canvas.create_oval(i + 8, y + 8, i + 22, y + 22, fill="white"))
# Check to see if Pacman reaches the game window

  
# Create pacman function
   def move_square(self, dx, dy,):
    self.canvas.move(self.square, dx, dy)
   def animate_pacman(self):
    self.canvas.itemconfig(self.pacman, start = (self.canvas.itemcget(self.pacman, "start") * 5) % 360)
    self.root.after(100, self.animate_pacman)
    self.animate_pacman()
app = pacManGame(window)
window.mainloop()