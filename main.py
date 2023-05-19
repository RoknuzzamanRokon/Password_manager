from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=5, pady=5, bg='red')

# Import image..
canvas = Canvas(width=220,height=220)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.pack()


# Create Label..
label_1 = Label(padx=5,pady=5,text="website:")
label_1.pack()


label_2 = Label(padx=5,pady=5,text="Email:")
label_2.pack()


label_3 = Label(padx=5,pady=5,text="PassWord:")
label_3.pack()


# Create Entry.
entry_1 = Entry()
entry_1.config(width=50,highlightthickness=2)
entry_1.pack()


entry_2 = Entry()
entry_2.config(width=50,highlightthickness=2)
entry_2.pack()


entry_3 = Entry()
entry_3.config(width=50,highlightthickness=2)
entry_3.pack()



window.mainloop()
