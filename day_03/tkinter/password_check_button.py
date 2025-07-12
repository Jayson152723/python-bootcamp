import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.pack()
from tkinter import messagebox
user_input = tkinter.StringVar(root, value="Enter your password and press enter")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input():
    if entry.get() == "Pass":
        message = "Password correct!"
        user_input.set(message)
    else:
        message = "Incorrect password!"
        user_input.set(message)
        messagebox.showerror(
            "Error",
            "This is an error message."
        )
button = tkinter.Button(root, text = "Submit", command=show_input)
button.pack()

root.mainloop()