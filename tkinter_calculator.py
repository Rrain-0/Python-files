# importing
from tkinter import *
from tkinter import ttk

# GUI interaction
window = Tk()
window.geometry("450x300")
window.title("Calculator")

# Adding inputs

# Entry box
entry = Entry(window, width=45, borderwidth=3, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button
def click(num):
    if entry.get() == "Error":
        entry.delete(0, END)

    result = entry.get()
    entry.delete(0, END)
    entry.insert(END, str(result) + str(num))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, END)

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "(", ")", "AC", "X",
    "Close"
]
row = 1
column = 0
for button in buttons:
    if button == "=":
        btn = ttk.Button (window, text=button, command=calculate)
    elif button == "AC":
        btn = ttk.Button (window, text=button, command=clear)
    elif button == "X":
        btn = ttk.Button (window, text=button, command=backspace)
    elif button == "Close":
        btn = ttk.Button (window, text=button, command=window.destroy)
    else:
        btn = ttk.Button (window, text=button, command=lambda x=button:click(x))

    btn.grid(row=row, column=column, padx=3, pady=3)

    column += 1
    if column > 3:
        column = 0
        row += 1


# mainloop
window.mainloop()