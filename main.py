from tkinter import messagebox
from tkinter import *
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}, \nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', mesage=f"No details for {website} exists")




def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for item in range(randint(8, 10))]

    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    passwords_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + passwords_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    name = name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": name,
            "password": password,
    }}

    if website == '' or password == '':
         messagebox.showwarning(title='Oops', message=f"Please don't leave any fields empty")
    elif website == '':
        messagebox.showwarning(title='Oops', message=f"Please don't leave the Website field empty")
    elif password == '':
        messagebox.showwarning(title='Oops', message=f"Please don't leave the Password field empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", 'r') as file:
                data = json.load(file)
                data.update(new_data)

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP -------------------------------

window = Tk()
window.minsize(width=220, height=220)
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=220)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)

name_label = Label(text="Email/Username:")
name_label.grid(row=2, column=0)

name_entry = Entry(width=35)
name_entry.grid(row=2, column=1, columnspan=2)
name_entry.insert(0, "angela@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()