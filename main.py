from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 9))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if website == '':
        messagebox.showinfo(title="Oops", message="Please don't leave website fields empty!")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading data
                data = json.load(data_file)
                messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                           f"Password: {data[website]['password']}")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        except KeyError:
            messagebox.showinfo(title="Error", message="No Detail for website exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "email": email,
                "password": password,
            }
    }
    if website == '' or password == '' or email == '':
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=70, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", command=find_password, pady=0, width=12)
search_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "harshkulkarni@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate password", command=generate_password, padx=0, pady=0)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, padx=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
