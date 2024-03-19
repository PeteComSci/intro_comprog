### Project Introduction and Instructions

**Project Title: CodeForge: Paired Programming for Real-World Solutions**

**Introduction:**
Welcome to CodeForge, a paired programming project where you and your partner will forge solutions to real-world problems through code. This initiative is designed to enhance your computational thinking, coding proficiency, and collaborative skills. You will work together to conceptualize, design, and implement a software solution that has practical applications and addresses genuine needs.

**Objective:**
The goal of CodeForge is to collaboratively create a Python application that solves a selected real-life problem. This project will test your ability to integrate various programming constructs, including loops, conditional statements, functions, and data structures like lists, dictionaries, and files, all within a teamwork-driven environment.

**Project Criteria:**
Your project will be assessed based on the following criteria:

1. **Random Module Usage** (9%)
2. **File Input/Output** (14%)
3. **Searching** (9%)
4. **Lists and Parallel Lists** (14%)
5. **Dictionaries** (14%)
6. **Error Handling** (9%)
7. **Specific Functions and Naming Conventions** (9%)
8. **Video, Computational Thinking Skills, and Collaboration/Teamwork** (9%)
9. **In-line Comments and Computational Thinking** (7%)
10. **Loops and Conditional Statements** (6%)

**Instructions:**
- **Select a Problem**: Choose a real-life problem to address. Ensure it is something both partners are passionate about and can contribute to solving.
- **Plan Your Strategy**: Discuss and plan your approach, distributing tasks based on each partner’s strengths. Aim for a balanced workload where both members contribute equally.
- **Code Collaboratively**: Practice paired programming, with one partner coding while the other reviews and suggests improvements in real-time. Switch roles regularly to maintain engagement and share perspectives.
- **Continuously Test**: Test your application throughout the development process to ensure functionality and usability. Debug and refine your code together to achieve the best outcome.
- **Document Your Journey**: Keep detailed in-line comments and documentation to explain your thought process, design choices, and code functionality.
- **Prepare a Joint Presentation**: Create a video presentation (5 to 7 minutes) that demonstrates your application, highlights the problem-solving process, and showcases the effectiveness of your collaboration.

**Submission Requirements:**
- The final source code of your application, fully commented for clarity and understanding.
- A detailed page on your e-portfolio documenting your collaborative process, how you addressed each evaluation criterion, and the impact of your solution.
- A video presentation (5 to 7 minutes) that effectively communicates your project's purpose, process, and performance.



### Project Evaluation Criteria

#### Random Module Usage
- **0%**: No use of the random module.
- **Poor**: Minimal and ineffective use of the random module, lacking practical application.
- **Average**: Meaningful use of the random module at least once, enhancing functionality.
- **Good**: Uses the random module effectively in various parts of the program, showing understanding and application in a practical context.
- **Exceptional**: Meaningful and practical use of the random module, utilizing functions like `random.randint()` and `random.choice()` in conjunction with other algorithms and functions.

#### File Input/Output
- **0%**: No implementation of file input/output.
- **Poor**: Incomplete or erroneous implementation of file input/output.
- **Average**: Basic functionality for writing to and reading from a single file.
- **Good**: Efficient use of file input/output with error handling, reading from, and writing to files seamlessly.
- **Exceptional**: Advanced handling of multiple file operations, integrating well with the rest of the program’s functionality.

#### Searching
- **0%**: No searching functionality implemented.
- **Poor**: Basic implementation of linear search using built-in functions.
- **Average**: Manual implementation of a linear search algorithm for specific purposes.
- **Good**: Implementation of advanced search algorithms or well-designed search functions that are integrated into the program.
- **Exceptional**: Multiple, efficient search algorithm implementations, designed for reusability and integration across the program, enhancing functionality and efficiency.

#### Lists and Parallel Lists
- **0%**: No use of lists or parallel lists.
- **Poor**: Basic use of lists without parallel lists or advanced list operations.
- **Average**: Purposeful use of both lists and parallel lists with fundamental operations like adding, editing, and deleting.
- **Good**: Efficient and meaningful use of lists and parallel lists in conjunction with advanced data structures and algorithms.
- **Exceptional**: Comprehensive use of lists and parallel lists integrated with other functionalities like searching and sorting, demonstrating advanced understanding and application.

#### Error Handling
- **0%**: No error handling implemented.
- **Poor**: Minimal error handling with limited user feedback.
- **Average**: Basic error handling using built-in structures with some meaningful user feedback.
- **Good**: Advanced error handling strategies integrated with program functionalities, improving user experience and program robustness.
- **Exceptional**: Comprehensive and thoughtful error handling across the program, ensuring robustness and providing clear, helpful user feedback.

#### Specific Functions and Naming Conventions
- **0%**: No adherence to naming conventions or functional programming.
- **Poor**: Limited function use, with less than 6 functions, poor naming conventions, and overlap in functionality.
- **Average**: Use of 6 to 10 functions with basic adherence to Python’s naming conventions and some unique functionality.
- **Good**: More than 10 functions, each with a clear, distinct purpose, well-integrated into the program, demonstrating good programming practices.
- **Exceptional**: More than 10 well-defined functions, excluding menu and main, with clear naming conventions and minimal redundancy, each serving a unique and critical role in the program.

#### Video, Computational Thinking Skills, and Collaboration/Teamwork
- **0%**: No video submission or demonstration of computational thinking and teamwork.
- **Poor**: Video shorter than 5 minutes, lacking clear demonstration of program functionality and team collaboration.
- **Average**: Video between 5 to 7 minutes, demonstrating basic functionality and some aspects of teamwork.
- **Good**: Video between 5 to 7 minutes, clearly demonstrating program functionality, computational thinking, and balanced team collaboration.
- **Exceptional**: Video between 5 to 7 minutes, excellently showcasing full program functionality, strategic planning, equal team participation, and high-quality presentation.

#### In-line Comments and Computational Thinking
- **0%**: No in-line comments or evidence of computational thinking.
- **Poor**: Sparse, uninformative comments, not explaining code logic.
- **Average**: Comments present but lacking in detailed explanation of logic and implementation.
- **Good**: Detailed comments providing clear explanations of the code’s logic and implementations, reflecting computational thinking.
- **Exceptional**: Comprehensive and informative comments throughout, enhancing understanding of complex coding principles and computational thinking.

#### Loops and Conditional Statements
- **0%**: No implementation of loops or conditional statements.
- **Poor**: Basic or incorrect use of loops and conditional statements, with limited functionality.
- **Average**: Correct use of simple “for” and “while” loops and basic conditional statements for specific tasks.
- **Good**: Effective use of complex loops and conditional structures, including nested loops and advanced conditionals, for data processing and control flow.
- **Exceptional**: Sophisticated use of multiple and nested loops and conditional statements, integrating deeply with program logic for efficient data handling and processing.

---

### Add Student Function

```python
# Function to add a new student record to the dictionary of students
# Allows for the inclusion of new entries, even with some missing information.

def add_student(students_dict, student_id, name=None, grade=None):
    """
    Add a new student or update an existing one in the dictionary of students.

    Parameters:
    students_dict (dict): The dictionary of current student records, keyed by student ID.
    student_id (int): The ID of the student to add or update.
    name (str, optional): The name of the student. Default is None.
    grade (int, optional): The grade of the student. Default is None.

    Returns:
    dict: The updated dictionary of students.
    """

    # Check if the student_id already exists in the dictionary
    if student_id in students_dict:
        print(f"Updating existing student with ID {student_id}.")
    else:
        print(f"Adding new student with ID {student_id}.")

    # Update or add the student record in the dictionary
    # If name or grade are not provided, they will remain as None
    students_dict[student_id] = {"name": name, "grade": grade}

    return students_dict

# Example usage of the function:
# current_students = {1: {'name': 'Alice', 'grade': 88}, 2: {'name': 'Bob', 'grade': 92}}
# updated_students = add_student(current_students, 3, 'Charlie', 85)
# print(updated_students)

```

### Update Student Function

```python
# Function to update the details of an existing student in the list of students
# This function is vital for maintaining current and accurate student records.

def update_student(students, student_id, updated_details):
    """
    Update an existing student's details in the list of students.

    Parameters:
    students (list): The list of current student records.
    student_id (int): The ID of the student whose record is to be updated.
    updated_details (dict): A dictionary containing the updated details for the student.

    Returns:
    list: The list of student records after the update, or None if the update fails.
    """

    # Iterate over the list of students to find the one with the matching ID
    for i in range(len(students)):
        # Access the student at the current index
        student = students[i]
        # Check if the current student's ID matches the given student_id
        if student['id'] == student_id:
            # Update the student's details with the provided updated_details
            # This updates the student record with the new values for each provided key
            students[i].update(updated_details)
            print(f"Student with ID {student_id} has been updated.")
            return students  # Return the updated list after modifying the student record

    # If no student with the matching ID is found, print a message and return None
    print(f"No student found with ID {student_id}.")
    return None

# Example usage of the function:
# current_students = [{'id': 1, 'name': 'Alice', 'grade': 88}, {'id': 2, 'name': 'Bob', 'grade': 92}]
# updated_details = {'name': 'Alice Cooper', 'grade': 91}
# updated_students = update_student(current_students, 1, updated_details)
# print(updated_students)
```

### Delete Student Function

```python
# Function to remove a student record from the list of students based on the student ID
# This function allows for managing the dataset by removing entries that are no longer needed.

def remove_student(students, student_id):
    """
    Remove a student from the list of students based on the student ID.

    Parameters:
    students (list): The list of current student records.
    student_id (int): The ID of the student to be removed.

    Returns:
    list: The updated list of student records after removal.
    """

    # Iterate over the list of students using the index to find the one with the matching ID
    for i in range(len(students)):
        student = students[i]
        # Check if the current student's ID matches the given student_id
        if student['id'] == student_id:
            # If a match is found, remove the student from the list
            del students[i]
            print(f"Student with ID {student_id} has been removed.")
            return students  # Return the updated list after removing the student

    # If no student with the matching ID is found, print a message and return the unchanged list
    print(f"No student found with ID {student_id}.")
    return students

# Example usage of the function:
# current_students = [{'id': 1, 'name': 'Alice', 'grade': 88}, {'id': 2, 'name': 'Bob', 'grade': 92}]
# updated_students = remove_student(current_students, 1)
# print(updated_students)
```

### Searching

```python
# Function to search for a student by name in a list
# This function illustrates the concept of searching, a fundamental
# computational process used to locate specific data within a collection.

def search_student_by_name(students, name):
    """
    Search for a student by name in the list of students.

    Parameters:
    students (list): The list of student records.
    name (str): The name of the student to search for.

    Returns:
    dict: The student record if a match is found, otherwise None.
    """
    # Iterate through each student in the list
    for student in students:
        # Check if the current student's name matches the search query
        if student['name'] == name:
            print(f"Found student with name {name}: {student}")
            return student  # Return the student record if a match is found

    print("Student not found with name {name}.")
    return None  # Return None if no matching student is found

# Example usage:
# students = [{'name': 'Alice', 'grade': 88}, {'name': 'Bob', 'grade': 92}]
# print(search_student_by_name(students, 'Alice'))
```

```python
# Function to search for a student by ID in a dictionary
# This function demonstrates the process of locating a specific entry in a dictionary,
# a common operation in data management.

def search_student(students_dict, student_id):
    """
    Search for a student by ID in the dictionary of students.

    Parameters:
    students_dict (dict): The dictionary of student records, keyed by student ID.
    student_id (int): The ID of the student to search for.

    Returns:
    dict: The student record if found, otherwise None.
    """
    # Iterate over each student in the dictionary
    for id, details in students_dict.items():
        # Check if the current student's ID matches the search ID
        if id == student_id:
            print(f"Found student with ID {student_id}: {details}")
            return details  # Return the student record if found

    print(f"Student not found with ID {student_id}.")
    return None  # Return None if the student is not found

# Example usage:
# current_students = {1: {'name': 'Alice', 'grade': 88}, 2: {'name': 'Bob', 'grade': 92}}
# print(search_student(current_students, 1))
```

### Random Module Usage

```python
import random

# Function to select a random student from a list
# This demonstrates the use of randomness to simulate real-world scenarios,
# such as randomly picking a student for a classroom activity.

def select_random_student(students):
    """
    Selects a random student from the list of students.

    Parameters:
    students (list): A list of student records or names.

    Returns:
    dict or str: The record or name of the randomly selected student.
    """
    # Ensure there are students in the list to avoid IndexError
    if not students:
        print("No students in the list.")
        return None

    # Generate a random index to select a student from the list
    # The randint function is used to ensure the index is within the list's range
    random_index = random.randint(0, len(students) - 1)
    
    # Return the student at the randomly selected index
    selected_student = students[random_index]
    print(f"Randomly selected student: {selected_student}")
    return selected_student

# Example usage:
# students = ["Alice", "Bob", "Charlie"]
# print(select_random_student(students))
```

### File Input/Output

#### List and Text File

```python
# Function to read student data from a file
# This simulates how applications retrieve data from storage,
# a common operation in many software systems.

def read_students_from_file(filename):
    """
    Reads student data from a specified file.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    list: A list of student records or names read from the file.
    """
    students = []  # Initialize an empty list to hold the student data

    try:
        # Attempt to open the file in read mode ('r')
        with open(filename, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace from the line
                # and append the processed line to the students list
                students.append(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")

    # Return the list of students read from the file
    return students

# Example usage:
# students = read_students_from_file('students.txt')
# print(students)

# Function to write student data to a file
# This represents the process of saving data to persistent storage.

def write_students_to_file(filename, students):
    """
    Writes student data to a specified file.

    Parameters:
    filename (str): The name of the file to write to.
    students (list): A list of student records or names to write.

    Returns:
    bool: True if writing was successful, False otherwise.
    """
    try:
        # Attempt to open the file in write mode ('w') to save the student data
        with open(filename, 'w') as file:
            for student in students:
                # Write each student on a new line in the file
                file.write(str(student) + "\n")
        return True
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return False

# Example usage:
# students = ["Alice", "Bob", "Charlie"]
# success = write_students_to_file('students.txt', students)
# if success:
#     print("Students written to file successfully.")
# else:
#     print("Failed to write students to file.")
```
#### Dictionary and Text File

```python
# Function to read student data from a text file into a dictionary
# Assumes each line of the file contains comma-separated values like 'id,name,grade'

def read_students_dict_from_file(filename):
    """
    Reads student data from a specified file and constructs a dictionary.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    dict: A dictionary of student records, keyed by student ID.
    """
    students_dict = {}  # Initialize an empty dictionary to hold the student data

    try:
        # Attempt to open the file in read mode ('r')
        with open(filename, 'r') as file:
            for line in file:
                # Strip any leading/trailing whitespace and split the line by comma
                id, name, grade = line.strip().split(',')
                # Populate the dictionary with the student data, converting grade to int
                students_dict[int(id)] = {'name': name, 'grade': int(grade)}
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")

    # Return the dictionary of students read from the file
    return students_dict

# Example usage:
# students_dict = read_students_dict_from_file('students.txt')
# print(students_dict)

# Function to write student data from a dictionary to a text file
# Exports the dictionary data into comma-separated values like 'id,name,grade'

def write_students_dict_to_file(filename, students_dict):
    """
    Writes student data to a specified file from a dictionary.

    Parameters:
    filename (str): The name of the file to write to.
    students_dict (dict): A dictionary of student records, keyed by student ID.

    """
    try:
        # Attempt to open the file in write mode ('w')
        with open(filename, 'w') as file:
            for student_id, details in students_dict.items():
                # Construct a comma-separated string from each student's data
                line = f"{student_id},{details['name']},{details['grade']}\n"
                # Write the constructed line to the file
                file.write(line)
        print(f"Student data successfully written to {filename}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage:
# students_dict = {1: {'name': 'Alice', 'grade': 88}, 2: {'name': 'Bob', 'grade': 92}}
# write_students_dict_to_file('students.txt', students_dict)


```

### Sorting Students Function

```python
# Function to sort a list of students by grade using the bubble sort algorithm
# This sorting function is a classic example of how algorithmic concepts are applied
# in practical programming tasks, particularly in organizing and structuring data.

def sort_students_by_grade(students):
    # Start with the assumption that a swap might occur
    swap_happened = True

    # Continue looping until no swaps occur in a full pass through the list,
    # which means the list is sorted
    while swap_happened:
        # Assume no swap will happen in this pass; this flag will be reset if a swap occurs
        swap_happened = False

        # Iterate through the list, stopping before the last element to avoid
        # comparing the last element with a non-existent next element
        for i in range(len(students) - 1):
            # Compare adjacent elements (students) by their grade
            if students[i]['grade'] > students[i + 1]['grade']:
                # Swap the elements if they are in the wrong order
                # Temporarily store one element to swap the values without losing any
                temp = students[i]
                students[i] = students[i + 1]
                students[i + 1] = temp

                # Since we made a swap, set the flag to True to indicate
                # that another pass is necessary to ensure sorting
                swap_happened = True

    # Return the sorted list
    return students

# Example usage:
# students = [{'name': 'Alice', 'grade': 88}, {'name': 'Bob', 'grade': 92}]
# print("Before sorting:", students)
# sorted_students = sort_students_by_grade(students)
# print("After sorting:", sorted_students)
```

```python
# Function to sort students by name using the bubble sort algorithm
def sort_students_by_name(students_dict):
    # Convert the dictionary to a list of tuples to enable sorting
    students_list = list(students_dict.items())
    swap_happened = True
    
    # Continue looping until no swaps are made, indicating the list is sorted
    while swap_happened:
        swap_happened = False
        for i in range(len(students_list) - 1):
            # Compare the names of adjacent students
            if students_list[i][1]['name'] > students_list[i + 1][1]['name']:
                # Swap the student tuples if they are in the wrong order
                students_list[i], students_list[i + 1] = students_list[i + 1], students_list[i]
                swap_happened = True

    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(students_list)
    return sorted_dict

# Example usage of the function:
# sorted_students = sort_students_by_name(current_students)
# print(sorted_students)

```

### Explanation for `students_list = list(students_dict.items())` and `students_list[i][1]`

In the sorting function, we convert the dictionary of students into a list of tuples using `students_dict.items()`. This is because dictionaries are not ordered and cannot be sorted directly like lists. Each tuple in the list contains two elements: the first element (`[0]`) is the student ID (key in the dictionary), and the second element (`[1]`) is the student's details (value in the dictionary).

- `students_list = list(students_dict.items())`: This line converts the dictionary into a list of tuples to make it sortable. Each tuple represents a key-value pair from the dictionary, where the key is the student ID and the value is another dictionary containing the student's details.

- `students_list[i][1]`: In this notation, `students_list[i]` accesses the ith tuple in the list (representing a student's ID and their details). Adding `[1]` accesses the second element of the tuple, which is the dictionary containing the student's details (like name and grade).

---

### Error Handling

```python
# Function to safely get a student ID from user input
# Demonstrates error handling in user input, a common issue in programming.

def get_student_id():
    try:
        # Attempt to convert the user input into an integer
        student_id = int(input("Enter student ID: "))
        return student_id
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid ID. Please enter a numeric value.")
        # Returning None indicates that the input was invalid
        return None

# Example usage:
# student_id = get_student_id()
# if student_id is not None:
#     print(f"Student ID is {student_id}")
# else:
#     print("No valid ID provided.")
```

### Loops and Conditional Statements

```python
# Function to manage a simple student management system menu
# This function illustrates the use of loops and conditional statements to create a user interface.

def manage_students():
    while True:
        # Display the menu options to the user
        print("1. Add Student\n2. Remove Student\n3. Show Students\n4. Exit")
        choice = input("Enter your choice: ")

        # Execute an action based on the user's choice
        if choice == '1':
            # Add student logic (not shown here for brevity)
            print("Adding a student...")
        elif choice == '2':
            # Remove student logic (not shown here for brevity)
            print("Removing a student...")
        elif choice == '3':
            # Show students logic (not shown here for brevity)
            print("Showing all students...")
        elif choice == '4':
            # Exit the program
            print("Exiting program.")
            break  # Break the loop to exit
        else:
            # Handle invalid choices entered by the user
            print("Invalid choice, please try again.")

# Example usage:
# manage_students()
```

