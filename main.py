from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_key():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    with open("data.txt", mode='w') as data_file:
        data_file.write(f"{website} | {email} | {password} ")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Import image..
canvas = Canvas(width=200, height=200)
canvas_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_image)
canvas.grid(row=1, column=2)


# Create Label..
label_1 = Label(padx=5, pady=5, text="Website:")
label_1.grid(row=2, column=1)
label_2 = Label(padx=5, pady=5, text="Email:")
label_2.grid(row=3, column=1)
label_3 = Label(padx=5, pady=5, text="PassWord:")
label_3.grid(row=4, column=1)


# Create Entry.
entry_1 = Entry()
entry_1.config(width=50, highlightthickness=0)
entry_1.focus()
entry_1.grid(row=2, column=2, columnspan=2)

entry_2 = Entry()
entry_2.config(width=50, highlightthickness=0)
entry_2.insert(0, "rokon.ali@gmail.com")
entry_2.grid(row=3, column=2, columnspan=2)

entry_3 = Entry()
entry_3.config(width=31, highlightthickness=0)
entry_3.grid(row=4, column=2)

# Create Button.
button_1 = Button()
button_1.config(text="Generate Password")
button_1.grid(row=4, column=3)

button_2 = Button()
button_2.config(text="Add", width=42, command=add_key)
button_2.grid(row=5, column=2, columnspan=2)


window.mainloop()
