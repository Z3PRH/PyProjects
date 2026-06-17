import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

A = "0"
operator = None
B = None

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "white"

window = tk.Tk()
window.title("calculator")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text="0", foreground=color_white, font=("Arial", 45),
                 background=color_black, anchor="e", width=column_count)
label.grid(row=0, columnspan=column_count, sticky="ew")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        btn = tk.Button(frame, text=value, font=("Arial", 30),
                        width=column_count, height=1,
                        command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            btn.config(foreground=color_black, background=color_light_grey)
        elif value in right_symbols:
            btn.config(foreground=color_black, background=color_orange)
        else:
            btn.config(foreground=color_white, background=color_dark_grey)
        btn.grid(row=row+1, column=column)

frame.pack()


def clear():
    global A, B, operator
    A = "0"
    operator = None
    B = None


def remove_all_zero(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator
    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if operator == "+":
                    label["text"] = remove_all_zero(numA+numB)
                elif operator == "-":
                    label["text"] = remove_all_zero(numA-numB)
                elif operator == "×":
                    label["text"] = remove_all_zero(numA*numB)
                elif operator == "÷":
                    label["text"] = remove_all_zero(numA/numB)

                clear()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
            operator = value
    elif value in top_symbols:
        if value == "AC":
            clear()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_all_zero(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_all_zero(result)
        elif value == "√":
            num = float(label["text"])
            label["text"] = remove_all_zero(num ** 0.5)
    else:  # this part holds the  '.' and digits
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value


window.mainloop()
