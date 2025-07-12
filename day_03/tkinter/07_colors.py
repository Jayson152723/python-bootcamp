import tkinter
root = tkinter.Tk()
label = tkinter.Label(root, text="Hello",
                      fg="red",
                      bg="black",
                      font=("Times New Roman", 100),
                      width = 200,
                      height= 200)
label.pack()
root.mainloop()