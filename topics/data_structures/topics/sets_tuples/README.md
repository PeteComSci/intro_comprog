## Sets and Tuples

Sets and tuples are important data structures in programming, each with its own unique properties and use-cases. Sets are collections of unique elements, while tuples are immutable sequences. Let's explore these data structures with examples in both pseudocode and Python, including detailed inline comments for clarity.

---

### Sets

Sets are collections of unique elements, meaning they do not allow duplicates and are unordered.

#### Pseudocode Example: Sets

```plaintext
// Pseudocode: Working with a set of unique numbers

// Create a set of numbers
Set uniqueNumbers to {1, 2, 3, 4, 5}

// Adding an element
Add 6 to uniqueNumbers

// Trying to add a duplicate element (will have no effect)
Add 3 to uniqueNumbers

// Removing an element
Remove 2 from uniqueNumbers

// Iterating through the set
For each number in uniqueNumbers Do
    Output number
End For
```

In this pseudocode:
- The set `uniqueNumbers` is created with unique elements.
- Elements are added using `Add`.
- Adding a duplicate element has no effect on the set.
- Elements are removed using `Remove`.
- A `For` loop is used to iterate through the set and output each element.

---

#### Python Example: Sets

```python
# Python: Working with a set of unique numbers

# Create a set of numbers
unique_numbers = {1, 2, 3, 4, 5}

# Adding an element
unique_numbers.add(6)

# Trying to add a duplicate element (will have no effect)
unique_numbers.add(3)

# Removing an element
unique_numbers.remove(2)

# Iterating through the set
for number in unique_numbers:
    print(number)
```

In this Python code:
- The set `unique_numbers` is created with unique elements.
- Elements are added using `.add()`.
- Adding a duplicate element has no effect on the set.
- Elements are removed using `.remove()`.
- A `for` loop is used to iterate through the set and print each element.

---

### Tuples

Tuples are immutable sequences, meaning once created, their elements cannot be changed. Tuples are often used for data that should not change throughout the execution of the program.

#### Pseudocode Example: Tuples

```plaintext
// Pseudocode: Working with a tuple of coordinates

// Create a tuple for coordinates
Set coordinates to (10, 20)

// Accessing elements
Output "X coordinate:", coordinates[0]
Output "Y coordinate:", coordinates[1]

// Trying to modify an element (will result in an error)
// Set coordinates[0] to 15 (Not allowed in tuples, as they are immutable)
```

In this pseudocode:
- The tuple `coordinates` is created with two elements.
- Elements are accessed using their index.
- Attempting to modify an element of a tuple is not allowed due to its immutability.

---

#### Python Example: Tuples

```python
# Python: Working with a tuple of coordinates

# Create a tuple for coordinates
coordinates = (10, 20)

# Accessing elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Trying to modify an element (will result in an error)
# coordinates[0] = 15  # Uncommenting this line will raise a TypeError, as tuples are immutable
```

In this Python code:
- The tuple `coordinates` is created with two elements.
- Elements are accessed using their index.
- Attempting to modify an element of a tuple will raise a `TypeError` due to its immutability.

---

These examples illustrate the functionality and use-cases of sets and tuples. Sets are used when you need a collection of unique items, and tuples are used when you have an immutable sequence of elements. Understanding when and why to use these data structures will enhance your ability to manage and manipulate data effectively in your programs.
