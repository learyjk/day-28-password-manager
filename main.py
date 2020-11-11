from tkinter import *
from PIL import ImageTk, Image


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = ImageTk.PhotoImage(Image.open("logo.gif"))
canvas.create_image(100, 100, image=logo_img)
canvas.pack()


window.mainloop()