import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter your password and press enter")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input(event):
    if entry.get() == "Pass":
        message = "Password correct!"
        user_input.set(message)
    else:
        message = "Incorrect passwor!"
        user_input.set(message)
root.bind("<Return>", show_input)

root.mainloop()