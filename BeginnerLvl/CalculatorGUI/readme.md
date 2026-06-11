# GUI Calculator

A graphical calculator built with tkinter. Click buttons to calculate.

## What it does

Enter numbers and operations. Click "=" to get the result. Click "clear" to reset.

Supports: +, -, *, /

## Run it

```bash
python calculator.py
```

## Requirements

- Python 3.8+
- tkinter (built-in)

---

## Key Concepts Learned

### `StringVar()`
Automatically syncs a variable with an Entry widget.

```python
display = tk.StringVar()
entry = tk.Entry(root, textvariable=display)

display.set("5")        # Entry shows "5"
value = display.get()   # Get what's in entry
```

Without StringVar, you'd manually update the entry every time. With it, they stay in sync automatically.

---

### `eval(expr)`
Evaluates a string as Python code and returns the result.

```python
eval("5+3")      # Returns 8
eval("10*2")     # Returns 20
eval("100/5")    # Returns 20.0
```

Useful for calculators — stores the expression as a string, then evaluates it all at once.

---

### `try/except`
Catches errors and handles them gracefully.

```python
try:
    result = eval("5++3")  # Invalid expression
except:
    print("error")  # Handles the error instead of crashing
```

User might click "+ +" by mistake. Instead of crashing, show "error".

---

### `lambda: press(1)`
Anonymous function that passes arguments to another function.

```python
btn1 = tk.Button(root, text='1', command=lambda: press(1))
```

Without lambda, you'd need a separate function for each button. Lambda lets you pass the button's value directly.

---

## Example

```
Click: 5 → Display shows "5"
Click: + → Display shows "5+"
Click: 3 → Display shows "5+3"
Click: = → Evaluates "5+3", shows "8"
```

---

How fast can you calculate? ⚡