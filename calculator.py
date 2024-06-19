import tkinter as tk
from tkinter import messagebox
import math

def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear_input_field():
    global expression
    expression = ""
    input_text.set(expression)

def evaluate_expression():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear_input_field()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        clear_input_field()

def square_root():
    global expression
    try:
        result = str(math.sqrt(eval(expression)))
        input_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")
        clear_input_field()

def exponentiation():
    global expression
    expression += "**"
    input_text.set(expression)

def add_to_memory():
    global memory
    try:
        memory += float(input_text.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input to add to memory")

def clear_memory():
    global memory
    memory = 0

expression = ""
memory = 0

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("400x500")

input_text = tk.StringVar()
input_frame = tk.Frame(app)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=25, bg="white", bd=10, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = tk.Frame(app)
buttons_frame.pack()

button_texts = [
    ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('√', 1, 3), ('^', 1, 4),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('MR', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('MC', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('M+', 4, 4),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('M-', 5, 4),
]

button_width = 10
button_height = 3

for (text, row, col) in button_texts:
    command = None
    if text not in ['C', '=', '√', '^', 'M+', '(', ')', 'MR', 'MC', 'M-']:
        command = lambda t=text: click_button(t)
    elif text == 'C':
        command = clear_input_field
    elif text == '=':
        command = evaluate_expression
    elif text == '√':
        command = square_root
    elif text == '^':
        command = exponentiation
    elif text == 'M+':
        command = add_to_memory
    elif text == 'MC':
        command = clear_memory

    tk.Button(
        buttons_frame, text=text, fg="black", width=button_width, height=button_height, bd=0,
        bg="white", cursor="hand2", command=command
    ).grid(row=row, column=col)

app.mainloop()
