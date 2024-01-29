# Arrays and Lists

Arrays and [lists](https://github.com/PeteComSci/intro_comprog/tree/4636ef0377a265e43ed7fee1fce340ef16f89132/topics/basics/topics/lists) are fundamental data structures in programming used for storing sequences of elements. Arrays typically have a fixed size, while lists are more dynamic. Let's explore these concepts with detailed examples in pseudocode and Python, including inline comments for clarity.

---

Arrays and [lists](https://github.com/PeteComSci/intro_comprog/tree/4636ef0377a265e43ed7fee1fce340ef16f89132/topics/basics/topics/lists) provide sequential storage, meaning elements are stored in a specific order and can be accessed by their position (or index) in the sequence.

> [!IMPORTANT]
> Python doesn't have a built-in array type as in some other languages, 

### Pseudocode Example

```plaintext
// Pseudocode: Working with an array/list of student names

// Create an array/list of student names
Set studentNames to ["Alice", "Bob", "Charlie", "Diana"]

// Accessing elements
Output "First student:", studentNames[0]  // Accessing the first element (index starts at 0)
Output "Second student:", studentNames[1]  // Accessing the second element

// Modifying elements
Set studentNames[2] to "Chuck"  // Changing "Charlie" to "Chuck"

// Adding elements (more applicable to lists as arrays are fixed-size)
Add "Edward" to studentNames

// Removing elements (also more applicable to lists)
Remove studentNames[3]  // Removing "Diana" from the list

// Iterating through the array/list
For each name in studentNames Do
    Output name
End For
```

In this pseudocode:
- `Set studentNames to [...]` creates an array/list of student names.
- Elements are accessed and modified using their index (e.g., `studentNames[0]`).
- `Add` and `Remove` operations are used to manipulate the list (note that in strict arrays, the size is fixed, and these operations may not apply).
- A `For` loop is used to iterate through the array/list and output each name.

---

### Python Example: [Lists](https://github.com/PeteComSci/intro_comprog/tree/4636ef0377a265e43ed7fee1fce340ef16f89132/topics/basics/topics/lists)

Lists in Python are dynamic and can be used similarly to both arrays and lists from other languages.

```python
# Python: Working with a list of student names

# Create a list of student names
student_names = ["Alice", "Bob", "Charlie", "Diana"]

# Accessing elements
print("First student:", student_names[0])  # Accessing the first element (index starts at 0)
print("Second student:", student_names[1])  # Accessing the second element

# Modifying elements
student_names[2] = "Chuck"  # Changing "Charlie" to "Chuck"

# Adding elements
student_names.append("Edward")  # Adding "Edward" to the list

# Removing elements
student_names.remove("Diana")  # Removing "Diana" from the list

# Iterating through the list
for name in student_names:
    print(name)
```

In this Python code:
- `student_names = [...]` creates a list of student names.
- Elements are accessed and modified using their index (e.g., `student_names[0]`).
- `.append()` and `.remove()` methods are used to manipulate the list.
- A `for` loop is used to iterate through the list and print each name.

---

> [!NOTE]
> For more information, go to the [Lists](https://github.com/PeteComSci/intro_comprog/tree/4636ef0377a265e43ed7fee1fce340ef16f89132/topics/basics/topics/lists) page.

---

These examples demonstrate how arrays and lists are used to store sequences of elements, providing various operations to access, modify, and iterate through the elements, making them versatile structures for handling ordered data.
