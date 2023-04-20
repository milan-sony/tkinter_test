from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

# widgets

# adding a sample label
lb1 = Label(window, text="Hello world!")
lb1.pack()

# adding a textbox
tb1 = Entry(window)
tb1.pack()

# adding a button
btn1 = Button(window, text="Click Me")
btn1.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()

