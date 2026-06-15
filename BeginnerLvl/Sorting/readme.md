# Movie/Book Rater

Rate and organize your movies and books. Sort by rating or date added.

## What it does

Add movies/books with a rating (1-10). View them sorted by:
- Rating (highest first)
- Date added (newest first)
- Filter by minimum rating

Delete entries, save/load data.

## Run it

```bash
python sorting.py
```

## Features

- ✅ Add entries (name, rating, auto-date)
- 👀 View all entries
- ⭐ Sort by rating (highest first)
- 📅 Sort by date (newest first)
- 🔍 Filter by minimum rating
- ❌ Delete entries
- 💾 Auto-save/load


---

## Key Concept: Sorting

### `sorted()` function
Arranges items in a list based on a condition.

```python
movies = [
    {"Name": "Inception", "Rating": 9},
    {"Name": "Titanic", "Rating": 7},
    {"Name": "Avatar", "Rating": 8}
]



# Sort by rating (highest to lowest)
sorted(movies, key=lambda x: x["Rating"], reverse=True)
# Result: [9, 8, 7]
```

### `reverse=True`
Flips the order. Without it = ascending (low to high). With it = descending (high to low).


### `key=lambda x: x["Rating"]`
Tells `sorted()` **what to sort by**. Here, sort by the "Rating" field.

---

## Example

```
Add: Inception, Rating 9
Add: Avatar, Rating 8
Add: Titanic, Rating 7

Sort by Rating: [9, 8, 7]
```

---

Rate your favorites! 🎬📚
