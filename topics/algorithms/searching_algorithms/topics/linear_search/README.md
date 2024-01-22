# Linear Search

Linear search, also known as sequential search, is a method for finding a particular value in a list by checking each element one by one until the desired element is found or the list ends. Let's delve into the concept with examples in both pseudocode and Python, along with detailed inline comments for clarity.

---

### Pseudocode Example: Linear Search

```plaintext
// Pseudocode: Linear Search to find a book on a shelf

// List of books on the shelf
Set books to ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick"]

// The book we are searching for
Set targetBook to "1984"

// Variable to store the position of the found book
Set position to -1  // We start with -1 to indicate that the book hasn't been found

// Iterate over each book in the list
For i from 0 to length of books - 1 Do
    // Check if the current book is the one we're looking for
    If books[i] equals targetBook Then
        // If it is, store the position where the book was found
        Set position to i
        // Exit the loop as we found the book
        Break
    End If
End For

// Check if the book was found and output the result
If position is not equal to -1 Then
    Output "Book found at position: ", position
Else
    Output "Book not found."
End If
```

In this pseudocode:
- The list `books` contains the names of the books on the shelf.
- `targetBook` is the book we are looking for.
- The `For` loop iterates through each book, comparing it with `targetBook`.
- If the book is found, the loop is exited using `Break`, and `position` reflects where the book was found.
- The final condition checks whether the book was found and outputs the result.

---

### Python Example: Linear Search

```python
# Python: Linear Search to find a book on a shelf

# List of books on the shelf
books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "Moby Dick"]

# The book we are searching for
target_book = "1984"

# Variable to store the position of the found book
position = -1  # Start with -1 to indicate that the book hasn't been found

# Iterate over each book in the list
for i in range(len(books)):
    # Check if the current book is the one we're looking for
    if books[i] == target_book:
        # If it is, store the position where the book was found
        position = i
        # Break out of the loop as we found the book
        break

# Check if the book was found and output the result
if position != -1:
    print(f"Book found at position: {position}")
else:
    print("Book not found.")
```

In this Python code:
- The list `books` contains the names of the books on the shelf.
- `target_book` is the book we are looking for.
- The `for` loop iterates through each book, comparing it with `target_book`.
- If the book is found, the loop is exited using `break`, and `position` reflects where the book was found.
- The final condition checks whether the book was found and prints the result.

---

These examples illustrate the linear search algorithm in both pseudocode and Python, demonstrating a basic yet fundamental approach to searching through a collection by examining each element sequentially.
