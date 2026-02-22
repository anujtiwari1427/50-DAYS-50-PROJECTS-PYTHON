
from tkinter import *

root = Tk()
root.title("Calculator")

expression = ""

def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except:
        entry_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry_text.set("")

entry_text = StringVar()
entry = Entry(root, textvariable=entry_text, font=("Arial", 18), bd=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0
for b in buttons:
    if b == "=":
        Button(root, text=b, width=5, height=2, command=equal).grid(row=row, column=col)
    else:
        Button(root, text=b, width=5, height=2,
               command=lambda x=b: press(x)).grid(row=row, column=col)
    col += 1
    if col == 4:
        row += 1
        col = 0

Button(root, text="Clear", width=22, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()