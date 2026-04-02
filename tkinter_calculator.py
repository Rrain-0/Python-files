# importing
from tkinter import *
from tkinter import ttk

first_number = None
current_operation = None
new_number = True

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
    global new_number

    if new_number:
        entry.delete(0, END)
        new_number = False
    entry.insert(END, num)

def set_operation(op):
    global first_number, current_operation, new_number

    try:
        first_number = float(entry.get())
        current_operation = op
        entry.delete(0, END)
        entry.insert(0, f"{first_number} {op}")
        new_number = True
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")


def calculate():
    global first_number, current_operation, new_number

    try:
        second_number = float(entry.get())

        if current_operation == "+":
            result = first_number + second_number
        elif current_operation == "-":
            result = first_number - second_number
        elif current_operation == "*":
            result = first_number * second_number
        elif current_operation == "/":
            if second_number == 0:
                raise ZeroDivisionError
            result = first_number / second_number
        else:
            return
        entry.delete(0, END)
        entry.insert(0, result)

    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Cannot divide by zero")
        new_number = True
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")
        new_number = True


def clear():
    global first_number, current_operation, new_number
    entry.delete(0, END)
    first_number = None
    current_operation = None
    new_number = True

def backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
     "AC", "X","Close"
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
    elif button in ["+", "-", "*", "/"]:
        btn = ttk.Button (window, text=button, command=lambda op=button: set_operation(op))
    else:
       btn = ttk.Button (window, text=button, command=lambda num=button: click(num))

    btn.grid(row=row, column=column, padx=3, pady=3)

    column += 1
    if column > 3:
        column = 0
        row += 1


# mainloop
window.mainloop()