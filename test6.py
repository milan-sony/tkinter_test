from tkinter import *

window = Tk()

window.title("Widget Styling")

window.geometry("600x400")

window.iconbitmap("./icon.ico")

img = PhotoImage(file="./img.png")

lb = Label(
            window,
            text="Hello World",
            font="Impact 20 bold",
            fg="#0A4D68",
            bg="#F7D060",
            # width=20, # width = 10 - will give the space of 10 characher size
            # height=10, # heigth = 10 - will give the line height of 10
            # padx=20, # padx=20 - will give 20px padding from left and right of the text
            # pady=10, # pady=10 - wiil give 10px padding from top and bottom of the text
            # anchor=SW, # anchor - is used to place the text/ give text position. Its values are N, S, E, W, NE, NW, SE, SW. It can be used only with the width and height property
            # state=DISABLED, # state = DISABLED - is use to disable the item
            # image=img, # image is used to give the image
            cursor="plus" # cursor -  is used to give the cursor a style. Its values are plus, clock, circle etc
          ) 
lb.pack()

tb = Entry(
            window,
            font="Impact 20",
            bg="#FFDCB6",
            fg="#9384D1",
            width=10,
            # show="*", # show = "*" - show is used to hash the text entered into the text field like password field
            # state=DISABLED, # disable the textbox
            justify=RIGHT, # justify is used to change the text input position. By default it is LEFT other values are RIGHT & CENTER
            cursor="clock"
          )
tb.pack()

btn = Button(
              window,
              text="Click Me",
              font="Impact 20",
              bg="#0B2447",
              fg="#A5D7E8",
              # width=20,
              # height=5,
              padx=20,
              pady=20,
              activebackground="red",
              activeforeground="white",
              cursor="circle",
              # state=DISABLED
              # anchor=N
            )
btn.pack()

window.mainloop()