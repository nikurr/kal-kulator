from tkinter import *
import math

def calculate_log():
    try:
        number = float(entry.get())
        result = math.log(number)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Ошибка")

def switch_mode():
    global mode
    if mode == "basic":
        mode = "scientific"
    else:
        mode = "basic"
        button_sqrt.grid_remove()
        button_power.grid_remove()

# Функция для вычисления выражения
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Ошибка")

root = Tk()
root.title("Калькулятор")
entry = Entry(root, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

button_0 = Button(root, text="0", width=5, height=2, command=lambda: entry.insert(END, "0"))
button_0.grid(row=4, column=1, padx=5, pady=2)

button_1 = Button(root, text="1", width=5, height=2, command=lambda: entry.insert(END, "1"))
button_1.grid(row=3, column=0, padx=5, pady=2)

button_2 = Button(root, text="2", width=5, height=2, command=lambda: entry.insert(END, "2"))
button_2.grid(row=3, column=1, padx=5, pady=2)

button_3 = Button(root, text="3", width=5, height=2, command=lambda: entry.insert(END, "3"))
button_3.grid(row=3, column=2, padx=5, pady=2)

button_4 = Button(root, text="4", width=5, height=2, command=lambda: entry.insert(END, "4"))
button_4.grid(row=2, column=0, padx=5, pady=2)

button_5 = Button(root, text="5", width=5, height=2, command=lambda: entry.insert(END, "5"))
button_5.grid(row=2, column=1, padx=5, pady=2)

button_6 = Button(root, text="6", width=5, height=2, command=lambda: entry.insert(END, "6"))
button_6.grid(row=2, column=2, padx=5, pady=2)

button_7 = Button(root, text="7", width=5, height=2, command=lambda: entry.insert(END, "7"))
button_7.grid(row=1, column=0, padx=5, pady=2)

button_8 = Button(root, text="8", width=5, height=2, command=lambda: entry.insert(END, "8"))
button_8.grid(row=1, column=1, padx=5, pady=2)

button_9 = Button(root, text="9", width=5, height=2, command=lambda: entry.insert(END, "9"))
button_9.grid(row=1, column=2, padx=5, pady=2)

button_plus = Button(root, text="+", width=5, height=2, command=lambda: entry.insert(END, "+"))
button_plus.grid(row=2, column=3, padx=5, pady=2)

button_minus = Button(root, text="-", width=5, height=2, command=lambda: entry.insert(END, "-"))
button_minus.grid(row=3, column=3, padx=5, pady=2)

button_equals = Button(root, text="=", width=5, height=2, command=evaluate_expression)
button_equals.grid(row=4, column=3, padx=5, pady=2)

button_multiply = Button(root, text="*", width=5, height=2, command=lambda: entry.insert(END, "*"))
button_multiply.grid(row=4, column=2, padx=5, pady=2)

button_divide = Button(root, text="/", width=5, height=2, command=lambda: entry.insert(END, "/"))
button_divide.grid(row=4, column=0, padx=5, pady=2)

button_clear = Button(root, text="Del", width=5, height=2, command=lambda: entry.delete(0, END))
button_clear.grid(row=1, column=3, padx=5, pady=2)

mode_button = Button(root, text="Swap", width=5, height=2, command=switch_mode)
mode_button.grid(row=5, column=3, padx=5, pady=2)

button_sqrt = Button(root, text="√", width=5, height=2, command=lambda: entry.insert(END, "sqrt("))
button_sqrt.grid(row=5, column=0, padx=5, pady=2)


button_power = Button(root, text="^", width=5, height=2, command=lambda: entry.insert(END, "**"))
button_power.grid(row=5, column=1, padx=5, pady=2)

buttonlog = Button(root, text="log", width=5, height=2, command=calculate_log)
buttonlog.grid(row=5, column=2, padx=5, pady=2)


mode = "basic"

root.mainloop()
