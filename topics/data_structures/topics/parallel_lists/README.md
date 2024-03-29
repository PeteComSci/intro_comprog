# Parallel Lists

Parallel lists are a fundamental concept in programming, especially useful when you need to maintain relationships between different sets of data without using more complex data structures like dictionaries or objects. Each list holds a different type of information, but related elements are aligned at the same index positions across these lists. This organization allows for a structured way to access and manipulate related data points.

Imagine planning a trip where you have a list of destinations, the cost associated with each, and activities available at each destination.

**Python Example:**
```python
destinations = ["Paris", "Tokyo", "New York"]
costs = [1000, 2000, 1500]
activities = ["Sightseeing", "Shopping", "Museums"]

for i in range(len(destinations)):
    print(f"Destination: {destinations[i]}, Cost: {costs[i]}, Activity: {activities[i]}")
```

---

#### Why Use Parallel Lists?

Parallel lists are particularly handy in scenarios where you're dealing with related datasets that are conceptually distinct but need to be processed together. For example, if you're handling data where each entry involves a name, a date, and a specific value, keeping these as parallel lists ensures that you can access all related information by using a single index.

#### Simple Practical Example

Consider a scenario where you're managing a classroom: you have students, their grades in math, and their attendance percentage. Using parallel lists, you can easily organize and manipulate this information.

**Python Implementation:**

```python
students = ["Alice", "Bob", "Charlie"]
grades = [88, 92, 75]
attendance = [90, 95, 80]

# Displaying each student's details
for i in range(len(students)):
    print(f"{students[i]}: Grade = {grades[i]}, Attendance = {attendance[i]}%")
```

---

## Manipulating Parallel Lists

Manipulation of parallel lists involves adding, removing, or modifying elements in a synchronized manner across all lists to maintain the relationship between them.

### Adding Elements

When adding new data, it's crucial to update all lists to keep the parallel structure intact.

```python
# Adding a new student
students.append("Diana")
grades.append(85)
attendance.append(88)

# Verify the addition
print(students, grades, attendance)
```

---

### Removing Elements

To remove data, you must ensure that the related elements are removed from all lists, typically by using the same index.

```python
# Remove the third student (Charlie)
index_to_remove = 2
del students[index_to_remove]
del grades[index_to_remove]
del attendance[index_to_remove]

# Verify the removal
print(students, grades, attendance)
```

---

### Modifying Elements

Modifying elements in parallel lists requires updating the specific indexes across all lists.

```python
# Improve Bob's grade and attendance
index_to_modify = 1
grades[index_to_modify] = 95
attendance[index_to_modify] = 98

# Verify the modification
print(f"Modified {students[index_to_modify]}'s Grade to {grades[index_to_modify]}, Attendance to {attendance[index_to_modify]}%")
```

---

### Searching for Elements

Finding elements involves iterating over one list and using the current index to access related elements in other lists.

```python
# Find and display Bob's details
search_name = "Bob"
if search_name in students:
    index = students.index(search_name)
    print(f"{students[index]}: Grade = {grades[index]}, Attendance = {attendance[index]}%")
else:
    print(f"{search_name} not found.")
```

---

Parallel lists provide a simple yet powerful way to manage related data sets. They are particularly useful in situations where using more complex data structures is not necessary or would add unwanted complexity. Proper manipulation of these lists, as shown through the examples above, ensures data integrity and accessibility, making them a valuable tool in a programmer's toolkit.

---

### Exercises

#### Exercise 1: Adding New Data

Given three parallel lists representing students' names, their math grades, and their attendance percentages, add a new student's information to these lists.

```python
students = ["Alice", "Bob", "Charlie"]
grades = [88, 92, 75]
attendance = [90, 95, 80]

# Your task: Add "Diana", with a grade of 85 and attendance of 88, to the lists.
```

---

#### Exercise 2: Removing a Student

Remove a student named "Charlie" from the lists. Ensure that the related grade and attendance information are also removed.

```python
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [88, 92, 75, 85]
attendance = [90, 95, 80, 88]

# Your task: Remove "Charlie" and the corresponding grade and attendance.
```

---

#### Exercise 3: Modifying Data

Find a student named "Bob" and update his grade to 95 and attendance to 98.

```python
students = ["Alice", "Bob", "Diana"]
grades = [88, 92, 85]
attendance = [90, 95, 88]

# Your task: Update Bob's grade to 95 and attendance to 98.
```

---

#### Exercise 4: Displaying Information

Display the name, grade, and attendance of all students, formatted nicely.

```python
students = ["Alice", "Bob", "Diana"]
grades = [88, 92, 85]
attendance = [90, 95, 88]

# Your task: Print each student's name, grade, and attendance in a formatted string.
```

---

#### Exercise 5: Searching for a Student

Given a student's name, find and display their grade and attendance. If the student is not found, print a message indicating so.

```python
students = ["Alice", "Bob", "Diana"]
grades = [88, 92, 85]
attendance = [90, 95, 88]

# Your task: Search for "Bob" and display his grade and attendance. If not found, indicate so.
```

---

### Mini Project 1: Library Management System

**Scenario:** You're tasked with managing a small library system. You have lists tracking book titles, the year of publication, and whether the book is currently checked out (True or False).

- **Initial Data:**
    ```python
    titles = ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
    years = [1925, 1949, 1960]
    checked_out = [False, True, False]
    ```
- **Tasks:**
    1. Add a new book to the system.
    2. Remove a book by title.
    3. Update the status of a book (checked out or not).
    4. Display the list of books, showing title, year, and availability.

**Learning Objective:** Practice adding to, removing from, and modifying parallel lists; use conditions to display data based on availability.

---

### Mini Project 2: Event Registration Tracker

**Scenario:** You're organizing a community event and need to track registrants. You maintain lists for registrant names, their chosen activities (e.g., "Singing", "Dance", "Art"), and their contact email.

- **Initial Data:**
    ```python
    names = ["Alice", "Bob", "Charlie"]
    activities = ["Singing", "Dance", "Art"]
    emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    ```
- **Tasks:**
    1. Allow a new registrant to sign up, adding their information.
    2. Provide a function to cancel a registration.
    3. Modify the activity choice for a registrant.
    4. Display all registrants and their chosen activities in a nicely formatted way.

**Learning Objective:** Enhance skills in list manipulation and provide an introduction to managing user input in a dynamic list-based system.

