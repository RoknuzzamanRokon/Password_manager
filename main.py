from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = len(entry_1.get())
    nr_symbols = len(entry_2.get())
    nr_numbers = len(entry_1.get())

    password = []
    for i in range(1, int(nr_letters / 2)):
        password += random.choice(letters)

    for i in range(1, int(nr_symbols / 3)):
        password += random.choice(numbers)

    for i in range(1, int(nr_numbers / 2)):
        password += random.choice(symbols)

    random.shuffle(password)
    join_word = ''.join(password)

    # print(join_word)
    # entry_3.config(text=join_word,width=31, highlightthickness=0)
    entry_3.insert(0, string=join_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_key():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()

    new_date = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:

        messagebox.showerror(title="Error", message="This is empty.Pleas fill up all information.")

    # else:
    #     # with open("data01.json", mode='w') as file:
    #     #     json.dump(new_date,file,indent=4)
    #
    #     with open("data01.json", mode='r') as read_data:
    #         r_data = json.load(read_data)
    #
    #         r_data.update(new_date)
    #
    #     with open("data01.json", mode='w') as write_date:
    #         json.dump(r_data, write_date, indent=4)
    #
    #     entry_1.delete(0, END)
    #     entry_3.delete(0, END)

    else:
        try:
            with open("data.json", mode='r') as data_file:
                # Read the json file.
                read_json = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # write a json file.
                json.dump(new_date, data_file, indent=4)

        else:
            # Update a json file.
            read_json.update(new_date)
            with open("data.json", mode="w") as data_file:
                # write a json file.
                json.dump(read_json, data_file, indent=4)

        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)


# ---------------------------- Search Button ------------------------------- #
def search_button_function():
    website = entry_1.get()

    try:
        with open("data.json", mode='r') as read_file:
            data = json.load(read_file)

    except FileNotFoundError:
        messagebox.showinfo(title="error", message=f"No data found.")

    else:
        if website in data:
            data_email = data[website]["email"]
            data_password = data[website]["password"]

            messagebox.showinfo(title="check info", message=f"This website information has already saved.\n"
                                                            f"email:{data_email}\n"
                                                            f"password:{data_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
entry_1.config(width=32, highlightthickness=0)
entry_1.focus()
entry_1.grid(row=2, column=2, columnspan=1)

entry_2 = Entry()
entry_2.config(width=50, highlightthickness=0)
entry_2.insert(0, "rokon.ali@gmail.com")
entry_2.grid(row=3, column=2, columnspan=2)

entry_3 = Entry()
entry_3.config(width=32, highlightthickness=0)
entry_3.grid(row=4, column=2)

# Create Button.
button_1 = Button()
button_1.config(text="Generate Password", command=pass_generator)
button_1.grid(row=4, column=3)

button_2 = Button()
button_2.config(text="Add", width=42, command=add_key)
button_2.grid(row=5, column=2, columnspan=2)

search_button = Button()
search_button.config(text="Search", width=14, command=search_button_function)
search_button.grid(row=2, column=3, columnspan=2)


window.mainloop()
