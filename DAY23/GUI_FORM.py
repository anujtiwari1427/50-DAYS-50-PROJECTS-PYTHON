



from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Registration Form")

def submit():
    info = f"Name: {name.get()}\nEmail: {email.get()}\nGender: {gender.get()}\nSubscribed: {sub.get()}"
    messagebox.showinfo("Submitted Data", info)

Label(root, text="Name").grid(row=0, column=0)
Label(root, text="Email").grid(row=1, column=0)

name = Entry(root)
email = Entry(root)
name.grid(row=0, column=1)
email.grid(row=1, column=1)

sub = IntVar()

Checkbutton(root, text="Subscribe", variable=sub).grid(row=2, column=1)

gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=3, column=0)
Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=3, column=1)

Button(root, text="Submit", command=submit).grid(row=4, column=1)

root.mainloop()
