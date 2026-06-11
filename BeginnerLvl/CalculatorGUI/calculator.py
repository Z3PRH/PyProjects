import tkinter as tk
expr = ""


def press(key):
    global expr
    expr += str(key)
    display.set(expr)


def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        display.set("error")
        expr = ""


def clear():
    global expr
    expr = ""
    display.set("")


root = tk.Tk()
root.title("calculator")
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display)
entry.grid(columnspan=4, ipadx=70)

btn1 = tk.Button(root, text='1', command=lambda: press(1), height=1, width=7)
btn1.grid(row=2, column=0)
btn2 = tk.Button(root, text='2', command=lambda: press(2), height=1, width=7)
btn2.grid(row=2, column=1)
btn3 = tk.Button(root, text='3', command=lambda: press(3), height=1, width=7)
btn3.grid(row=2, column=2)
btn4 = tk.Button(root, text='4', command=lambda: press(4), height=1, width=7)
btn4.grid(row=3, column=0)
btn5 = tk.Button(root, text='5', command=lambda: press(5), height=1, width=7)
btn5.grid(row=3, column=1)
btn6 = tk.Button(root, text='6',  command=lambda: press(6), height=1, width=7)
btn6.grid(row=3, column=2)
btn7 = tk.Button(root, text='7',  command=lambda: press(7), height=1, width=7)
btn7.grid(row=4, column=0)
btn8 = tk.Button(root, text='8',  command=lambda: press(8), height=1, width=7)
btn8.grid(row=4, column=1)
btn9 = tk.Button(root, text='9',  command=lambda: press(9), height=1, width=7)
btn9.grid(row=4, column=2)
btn0 = tk.Button(root, text='0',  command=lambda: press(0), height=1, width=7)
btn0.grid(row=5, column=0)

plus = tk.Button(root, text='+', command=lambda: press('+'), height=1, width=7)
plus.grid(row=2, column=3)
minus = tk.Button(root, text='-', command=lambda: press('-'),
                  height=1, width=7)
minus.grid(row=3, column=3)
mult = tk.Button(root, text='*', command=lambda: press('*'), height=1, width=7)
mult.grid(row=4, column=3)
div = tk.Button(root, text='/', command=lambda: press('/'), height=1, width=7)
div.grid(row=5, column=3)

equal_btn = tk.Button(root, text="=", command=equal,
                      height=1, width=7)
equal_btn.grid(row=5, column=2)
clear_btn = tk.Button(root, text="clear", command=clear,
                      height=1, width=7)
clear_btn.grid(row=5, column=1)
root.mainloop()
