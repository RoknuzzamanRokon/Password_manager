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

    else:
        try:
            with open("data.json", mode='r') as data_file:
                # Read the json file.
                read_json = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # write a json file.
                json.dump(read_json, data_file, indent=4)

        else:
            # Update a json file.
            read_json.update(new_date)
            with open("data.json", mode="w") as data_file:
                # write a json file.
                json.dump(read_json, data_file, indent=4)

        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)

