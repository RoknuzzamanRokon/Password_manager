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
canvas.grid(row=1,column=2)


# Create Label..
label_1 = Label(padx=5,pady=5,text="website:")
label_1.grid(row=2,column=1)


label_2 = Label(padx=5,pady=5,text="Email:")
label_2.grid(row=3,column=1)


label_3 = Label(padx=5,pady=5,text="PassWord:")
label_3.grid(row=4,column=1)


# Create Entry.
entry_1 = Entry()
entry_1.config(width=50,highlightthickness=2)
entry_1.grid(row=2,column=2)


entry_2 = Entry()
entry_2.config(width=50,highlightthickness=2)
entry_2.grid(row=3,column=2)


entry_3 = Entry()
entry_3.config(width=20,highlightthickness=2)
entry_3.grid(row=4,column=2)

# Create Button.
button_1 = Button()
button_1.config(text="Generate Password")
button_1.grid(row=4,column=3)


button_2 = Button()
button_2.config(text="Add", width=42)
button_2.grid(row=5,column=2)
window.mainloop()
