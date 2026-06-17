from tkinter import ttk
import tkinter as tk


category_values = ["Temperature", "Distance", "Weight"]
units = []


def clear():
    global category, value_label, from_combo, to_combo, display_result

    value_label.delete(0, tk.END)
    display_result.config(text="Your Result Will Be Displayed Here")

    category.set("")
    from_combo.set("")
    to_combo.set("")

    from_combo["values"] = []
    to_combo["values"] = []


def update_units(event):
    global units, category_values, from_combo, to_combo
    catergory_input = category.get()

    if catergory_input == "Temperature":
        units = ["C", "F"]

        from_combo["values"] = units
        to_combo["values"] = units

        from_combo.current(0)
        to_combo.current(1)
    elif catergory_input == "Distance":
        units = ["Km", "mi"]

        from_combo["values"] = units
        to_combo["values"] = units

        from_combo.current(0)
        to_combo.current(1)
    else:
        units = ["Kg", "lbs"]

        from_combo["values"] = units
        to_combo["values"] = units

        from_combo.current(0)
        to_combo.current(1)


def confirmclick():
    global value_label, category, from_combo, to_combo
    value = value_label.get()
    if not value:
        display_result.config(text="Please Enter Value to Convert")
    else:
        try:
            input_value = float(value)
        except ValueError:
            display_result.config(text="Please enter a valid number")
            return
        if category.get() == "Temperature":
            if from_combo.get() == "C":
                input_value = float(value)
                result = (input_value * 9/5) + 32
                display_result.config(text=f"{input_value}C == {result}F")
            else:
                input_value = float(value)
                result = (input_value - 32) * 5/9
                display_result.config(text=f"{input_value}F == {result}C")
        elif category.get() == "Distance":
            if from_combo.get() == "Km":
                input_value = float(value)
                result = input_value * 0.62137
                display_result.config(text=f"{input_value}Km == {result}mi")
            else:
                input_value = float(value)
                result = input_value/(0.621371)
                display_result.config(text=f"{input_value}mi == {result}Km")
        else:
            if from_combo.get() == "Kg":
                input_value = float(value)
                result = input_value * 2.20462
                display_result.config(text=f"{input_value}kG == {result}lbs")
            else:
                input_value = float(value)
                result = input_value/(2.20462)
                display_result.config(text=f"{input_value}lbs == {result}Kg")


window = tk.Tk()
window.geometry("500x250")
window.title("Unit Coverter")

frame = tk.Frame(window)
frame.pack(expand=True)

label = tk.Label(
    frame,
    text="Unit Converter",
    font=("Helvetica", 16, "bold")
)
label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

category_label = tk.Label(frame, text="Select Category:")
category_label.grid(row=1, column=0, sticky="e", padx=(0, 5), pady=3)

category = ttk.Combobox(frame, state="readonly", values=category_values)
category.grid(row=1, column=1, pady=3)
category.bind("<<ComboboxSelected>>", update_units)
category.current(0)

entry_label = tk.Label(frame, text="Enter Value:")
entry_label.grid(row=2, column=0, sticky="e", padx=(0, 5), pady=3)

value_label = tk.Entry(frame)
value_label.grid(row=2, column=1, pady=3)

from_label = tk.Label(frame, text="From Unit:")
from_label.grid(row=3, column=0, sticky="e", padx=(0, 5), pady=3)

from_combo = ttk.Combobox(frame, state="readonly", values=units)
from_combo.grid(row=3, column=1, pady=3)

to_label = tk.Label(frame, text="To Unit:")
to_label.grid(row=4, column=0, sticky="e", padx=(0, 5), pady=3)

to_combo = ttk.Combobox(frame, state="readonly", values=units)
to_combo.grid(row=4, column=1, pady=3)

convert = tk.Button(frame, text="Convert", command=confirmclick)
convert.grid(row=5, column=0, pady=5)

clr = tk.Button(frame, text="Clear", command=clear)
clr.grid(row=5, column=1, pady=5)

exit_btn = tk.Button(frame, text="Exit", command=window.destroy)
exit_btn.grid(row=5, column=2, pady=5)

display_result = tk.Label(
    frame,
    text="Your Result Will Be Displayed Here",
    font=("Helvetica", 10, "bold")
)
display_result.grid(row=6, column=0, columnspan=3, pady=8)

window.mainloop()
