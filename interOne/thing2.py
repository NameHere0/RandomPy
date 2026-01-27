import tkinter as tk
from tkinter import ttk


def reverse():
    try:
        newStr.set(str(usrPut.get())[::-1])
    except ValueError:
        newStr.set("invalid")


root = tk.Tk()
root.title("Hello wold ")

mainframe = ttk.Frame(root, padding=(5, 5, 10, 10))
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))  # type: ignore

usrPut = tk.StringVar()
usrPutEntry = ttk.Entry(mainframe, width=7, textvariable=usrPut)
usrPutEntry.grid(column=2, row=1, sticky=(tk.W, tk.E))  # type: ignore

newStr = tk.StringVar()
ttk.Label(mainframe, width=10, textvariable=newStr).grid(
    column=2,
    row=2,
    sticky=(tk.W, tk.E),  # type: ignore
)

ttk.Button(mainframe, text="Reverse", command=reverse).grid(
    column=3, row=3, sticky=tk.W
)



root.mainloop()
