from tkinter import *

# creating an object of class Tk()
window = Tk()

# change window title
window.title("Hello World")

# change/giving fixed size to window
window.geometry("600x400") # 600 = width & 400 = height

# change the window icon, the icon should be of .ico file
window.iconbitmap("./icon.ico")

#! Pgrm to get 2 number from 2 txtboxes and print the sum on after clicking the button

lb = Label(window, text="Enter 1st number")
lb.pack()
tb = Entry(window)
tb.pack()

lb2 = Label(window, text="Enter 2nd number")
lb2.pack()
tb2 = Entry(window)
tb2.pack()

def sum():
  sum = int(tb.get()) + int(tb2.get())
  result.set(sum)
result = StringVar()

lb3 = Label(window, text="The sum is")
lb3.pack()

lb4 = Label(window, textvariable=result)
lb4.pack()

# tb3 = Entry(window, textvariable=result)
# tb3.pack()

btn = Button(window, text="SUM", command=sum)
btn.pack()

# mainloop is used to  run the window/tinker 
window.mainloop()