from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

# Pgrm to get text from the txtbox and print it after clicking the button

# adding a label
lb = Label(window, text="Enter your name")
lb.pack()

# adding a textbox
tb = Entry(window)
tb.pack()

def message():
  name = tb.get()
  lb2 = Label(window, text="Hello " + name)  
  lb2.pack()

# adding a button
btn = Button(window, text="Click Me", command = message)
btn.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()