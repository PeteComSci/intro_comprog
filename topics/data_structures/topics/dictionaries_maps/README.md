## Dictionaries or Maps (Key-Value Pairs)

Dictionaries or maps are versatile data structures used to store data in key-value pairs. Each key is unique and maps to a value, allowing for efficient data retrieval and manipulation. Let's explore dictionaries/maps and operations such as adding, retrieving, and removing items with examples in both pseudocode and Python.

---

#### Pseudocode Example: Dictionaries/Maps

```plaintext
// Pseudocode: Working with a dictionary/map of student grades

// Create a dictionary/map of student grades
Set studentGrades to {"Alice": 85, "Bob": 92, "Charlie": 78}

// Adding an item
Set studentGrades["Diana"] to 95  // Adds Diana to the dictionary with a grade of 95

// Retrieving an item
Set aliceGrade to studentGrades["Alice"]
Output "Alice's grade:", aliceGrade  // Outputs: Alice's grade: 85

// Removing an item
Remove studentGrades["Charlie"]  // Removes Charlie from the dictionary

// Iterating through the dictionary/map
For each student, grade in studentGrades Do
    Output student, "'s grade: ", grade
End For
```

In this pseudocode:
- The dictionary/map `studentGrades` stores student names as keys and their grades as values.
- New items are added using `Set`.
- Items are retrieved by specifying their key.
- Items are removed using `Remove`.
- A `For` loop is used to iterate through the dictionary/map and output each key-value pair.

---

#### Python Example: Dictionaries

```python
# Python: Working with a dictionary of student grades

# Create a dictionary of student grades
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Adding an item
student_grades["Diana"] = 95  # Adds Diana to the dictionary with a grade of 95

# Retrieving an item
alice_grade = student_grades["Alice"]
print("Alice's grade:", alice_grade)  # Outputs: Alice's grade: 85

# Removing an item
del student_grades["Charlie"]  # Removes Charlie from the dictionary

# Iterating through the dictionary
for student, grade in student_grades.items():
    print(student, "'s grade: ", grade)
```

In this Python code:
- The dictionary `student_grades` stores student names as keys and their grades as values.
- New items are added using `=`.
- Items are retrieved by specifying their key.
- Items are removed using `del`.
- The `.items()` method and a `for` loop are used to iterate through the dictionary and print each key-value pair.

---

These examples demonstrate the utility of dictionaries/maps in storing and managing data in key-value pairs. They provide an efficient way to access, add, and remove data, making them an excellent choice for various use-cases where quick data retrieval and structured storage are required.
