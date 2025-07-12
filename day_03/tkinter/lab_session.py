import json
import tkinter
root = tkinter.Tk()

entry1 = tkinter.Entry(root)
entry1.pack()

text1 = tkinter.StringVar(root, value="Name")
label1 = tkinter.Label(root, textvariable=text1)
label1.pack()

entry2 = tkinter.Entry(root)
entry2.pack()

text2 = tkinter.StringVar(root, value="Age")
label2 = tkinter.Label(root, textvariable=text2)
label2.pack()

text3 = tkinter.StringVar(root, value="Preferred Theme")
label3 = tkinter.Label(root, textvariable=text3)
label3.pack()

radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
root, text="Light", variable=radio_var, value="Light")
radio1.pack()
radio2 = tkinter.Radiobutton(
root, text="Dark", variable=radio_var, value="Dark")
radio2.pack()

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
root,
text="Subscribe to newsletter",
variable=check_value
)
checkbox.pack()

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=slider_value
)
slider.pack()

def show_input():
    user = {
        "Name":entry1.get(),
        "Age": entry2.get(),
        "Theme": text3.get(),
        "Subscribe": check_value.get(),
        "Rate": slider_value.get()
    }
    with open('people.json', 'w') as file:
        json.dump(user, file)

button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()



root.mainloop()