from tkinter import *

# Create window
root = Tk()
root.title("GUI Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Entry field
entry = Entry(root, width=20, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Clear function
def button_clear():
    entry.delete(0, END)

# Operation functions
def button_add():
    first_number = entry.get()
    global f_num
    global operation
    operation = "addition"
    f_num = float(first_number)
    entry.delete(0, END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global operation
    operation = "subtraction"
    f_num = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global operation
    operation = "multiplication"
    f_num = float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num
    global operation
    operation = "division"
    f_num = float(first_number)
    entry.delete(0, END)

# Equal function
def button_equal():
    second_number = float(entry.get())
    entry.delete(0, END)

    if operation == "addition":
        entry.insert(0, f_num + second_number)

    elif operation == "subtraction":
        entry.insert(0, f_num - second_number)

    elif operation == "multiplication":
        entry.insert(0, f_num * second_number)

    elif operation == "division":
        if second_number == 0:
            entry.insert(0, "Error")
        else:
            entry.insert(0, f_num / second_number)

# Buttons
button_1 = Button(root, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, command=lambda: button_click(0))

button_add_btn = Button(root, text="+", padx=29, pady=20, command=button_add)
button_sub_btn = Button(root, text="-", padx=31, pady=20, command=button_subtract)
button_mul_btn = Button(root, text="*", padx=31, pady=20, command=button_multiply)
button_div_btn = Button(root, text="/", padx=31, pady=20, command=button_divide)

button_equal_btn = Button(root, text="=", padx=68, pady=20, command=button_equal)
button_clear_btn = Button(root, text="C", padx=68, pady=20, command=button_clear)

# Grid placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear_btn.grid(row=4, column=1, columnspan=2)
button_equal_btn.grid(row=5, column=1, columnspan=2)

button_add_btn.grid(row=1, column=3)
button_sub_btn.grid(row=2, column=3)
button_mul_btn.grid(row=3, column=3)
button_div_btn.grid(row=4, column=3)

root.mainloop()
