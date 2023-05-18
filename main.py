from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=10,pady=10,bg='red')


canvas = Canvas(width=400,height=400)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(200,200,image=canvas_image)
canvas.pack()


window.mainloop()
