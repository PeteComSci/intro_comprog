# File Input/Output in Python

### Learning Objectives:

- Understand how to open, read, write, and close files in Python.
- Learn to handle exceptions, such as file not found errors, to prevent program crashes.
- Practice manipulating data and reflecting changes in a persistent storage format.

File Input/Output (I/O) operations are essential for reading data from files and writing data to files, allowing data to persist beyond the runtime of a program. This capability is crucial for applications that require data storage, retrieval, and manipulation.

---

### Concept and Practical Use:

Imagine running a small business where you need to keep track of inventory items, their prices, and stock levels. File I/O operations enable you to save this information in a file and update or retrieve it as needed.

**Python Example for Writing Data:**
```python
# Inventory items and their details
items = ["Notebook", "Pen", "Eraser"]
prices = [1.5, 0.5, 0.2]
stocks = [100, 200, 150]

# Function to save inventory data to a file
def save_inventory(filename):
    with open(filename, 'w') as file:
        for i in range(len(items)):
            file.write(f"{items[i]},{prices[i]},{stocks[i]}\n")
```

**Explanation:**
- `open(filename, 'w')` opens a file for writing. If the file doesn't exist, it's created. If it does, it's overwritten.
- `for i in range(len(items))` iterates over the indexes of the `items` list.
- `file.write(f"{items[i]},{prices[i]},{stocks[i]}\n")` writes a line for each item to the file, formatting it as comma-separated values (CSV), followed by a newline character to separate each item's data.

---

**Python Example for Reading Data:**
```python
# Function to load inventory data from a file
def load_inventory(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                item, price, stock = line.strip().split(',')
                print(f"Item: {item}, Price: {price}, Stock: {stock}")
    except FileNotFoundError:
        print("Inventory file not found.")
```

**Explanation:**
- `try` block attempts to open and read the file. If the file doesn't exist, it jumps to the `except` block.
- `open(filename, 'r')` opens the file for reading.
- `for line in file:` iterates over each line in the file.
- `line.strip().split(',')` removes whitespace from the ends of the line (like newline characters) and splits the line into parts wherever commas are found.
- `except FileNotFoundError:` catches the case where the file does not exist, printing an error message.

---

### Why File I/O is Important:

File I/O is handy for scenarios requiring data logging, configuration settings, data analysis, and more. For example, in a classroom setting, teachers can keep digital records of student grades and attendance, allowing for easy updates and retrievals.

By mastering File I/O operations, you can build more dynamic, data-driven applications, enhancing your overall programming capabilities.

---

For practicing File I/O in Python, here are some simple and straightforward exercises that align with the examples provided earlier, focusing on fundamental skills such as reading from and writing to files, handling exceptions, and manipulating file data.

### Exercise 1: Write Greetings to a File
Write a program that asks the user for their name and writes a greeting to a file named `greetings.txt`.

---

### Exercise 2: Log Your Daily Activities
Create a simple diary logger. Prompt the user to enter a daily activity and append it to a file named `diary.txt` with the current date.

---

### Exercise 3: Read and Display Contents of a File
Write a program that reads the contents of a file named `notes.txt` and displays them on the screen.

---

### Exercise 4: Count the Number of Lines in a File
Create a program that reads a file and counts the number of lines in it. Use any text file you have, such as `diary.txt`.

---

### Exercise 5: Error Handling in File Reading
Improve the file reading program from Exercise 3 by adding error handling to manage the case where the file does not exist.

Each exercise is designed to build proficiency with Python's file handling capabilities, from basic operations like writing and reading files to more advanced topics such as error handling and file data manipulation.

