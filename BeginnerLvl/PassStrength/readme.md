# Password Strength Checker

Check if your password is strong enough. (Spoiler: It's probably not.)

## What it does

Enter a password. System checks:
- Length (8+ characters)
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Gives a strength rating based on how many checks pass.

## Run it

```bash
python password_strength_checker.py
```

## Features

- Checks 5 criteria[Check above in features]
- Strength score (1-5)
- Feedback on what to improve
- Check multiple passwords


## New Functions Used

### `any()`
Checks if **ANY** item in a sequence is True.

```python
# Example
items = [False, False, True, False]
any(items)  # Returns True (because at least one is True)

# With password checking
has_upper = any(char.isupper() for char in password)
# Returns True if ANY character is uppercase
```

---

### `char.isupper()` / `char.islower()`
Checks if a **single character** is uppercase/lowercase.

```python
"A".isupper()  # True
"a".islower()  # True
"1".isupper()  # False (numbers aren't uppercase/lowercase)
```

---

### `char.isdigit()`
Checks if a **single character** is a digit (0-9).

```python
"5".isdigit()   # True
"A".isdigit()   # False
" ".isdigit()   # False
```

---

## Example

```
Enter password: Pass123!
Password Score: 5
The Password Contain UpperCase, LowerCase, Digits and has Character length more than 8
```

---

How strong is your password? 🔐