from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

def find_password():
    w = website_entry.get().title()

    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No json file to read!")
    else:
        try:
            p = data[w]["password"]
            u = data[w]["email"]
        except KeyError:
            messagebox.showinfo(title="Oops", message="No password for that Website!")
        else:
            messagebox.showinfo(title=f"{w}", message=f"Username: {u}\nPassword: {p}")
            pyperclip.copy(p)


        # ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w = website_entry.get().title()
    u = eu_entry.get().lower()
    p = pass_entry.get()
    new_data = {
        w: {
            "email": u,
            "password": p,
        }
    }

    if len(w) == 0 or len(p) == 0:
        messagebox.showinfo(title="Oops", message="Please provide data for all fields")
    else:
        try:
            with open("data.json", mode="r") as f:
                # Read old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as f:
                # Save updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = ImageTk.PhotoImage(Image.open("logo.gif"))
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

eu_label = Label(text="Email/Username:")
eu_label.grid(column=0, row=2)
eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)
eu_entry.insert(0, "keeganleary@gmail.com")

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=22)
pass_entry.grid(column=1, row=3)

generate_button = Button(text="Generate", width=10, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()