from tkinter import *

base = Tk()
miLienzo = Frame(base,width=200,height=200)
miLienzo.pack()

miLabel = Label(miLienzo, text="Programación ")
miLabel.place(x=30,y=50)
miLabel.config(anchor="ne")
miLabel.config(bg="black")
miLabel.config(fg="white")
miLabel.config(font=("Arial", 10))
miLabel.config(width=15,height=1)

base.mainloop()