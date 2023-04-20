from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

# writing a function to print the label after clicking the button

def message():
  lb2 = Label(window, text="Hello World")
  lb2.pack()

# adding a button
btn1 = Button(window, text="Click Me", command = message) # commad is used to set which function should run after button is  clicked
btn1.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()