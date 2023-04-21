from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

# Pgrm to print the label after clicking the button

def message():
  lb = Label(window, text="Hello World")
  lb.pack()

# adding a button
btn = Button(window, text="Click Me", command = message) # commad is used to set which function should run after button is  clicked
btn.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()