# Student Grades Tracker Starter Code

# Instructions: This Python script is designed to help you manage student grades using parallel lists.
# You will need to implement various functions to complete this program.
# Follow the TODO comments and replace the 'pass' statements with your own code.

# Parallel lists to store student names and their grades in math and science
# Initialize parallel lists
students = ['Alice', 'Bob', 'Charlie', 'Diana']
math_grades = [92, 85, 88, 79]
science_grades = [94, 88, 90, 85]

# TODO: Implement a function to display all students and their grades
def display_grades():
    pass  # Replace this with your implementation


# TODO: Implement a function to add a new student and their grades
def add_student():
    pass  # Replace this with your implementation


# TODO: Implement a function to remove a student by name
def remove_student():
    pass  # Replace this with your implementation


# TODO: Implement a function to search for a student by name and display their grade
def search_student(student_name):
    """
    Searches for a student by name in the students list and prints their grade.

    Parameters:
    - student_name (str): The name of the student to search for.

    If the student is found, print their name and grade.
    If the student is not found, print a message indicating they are not on the list.
    """
    pass  # Replace this with your implementation


# TODO: Implement a function to read students and their grades from a file
# Hint: Use the format 'name,math_grade,science_grade' for each line in the file
def read_students(file_path):
    pass  # Replace this with your implementation


# TODO: Implement a function to save the current list of students and their grades to a file
def save_students(file_path):
    pass  # Replace this with your implementation


# TODO: Implement error handling for file operations (e.g., file not found, incorrect file format)
def safe_file_operation(operation, file_path):
    pass  # Replace this with your implementation


# Function to select a student randomly for a surprise quiz or reward
def select_student_for_surprise(students, math_grades, science_grades):
    """
    Selects a student randomly for a surprise quiz or reward based on their grades.
    Higher grades increase the chance of being selected for a reward,
    while lower grades increase the chance of being selected for a quiz to encourage improvement.
    
    Args:
    - students: List of student names.
    - math_grades: Parallel list of math grades corresponding to each student.
    - science_grades: Parallel list of science grades corresponding to each student.
    
    Returns:
    - A string message with the selected student's name and the reason for their selection (quiz or reward).
    """
    pass  # Replace this with your implementation


# Menu function to display options and capture user input
def menu():
    while True:
        display_grades()
        print("\nOptions: ")
        print("1. Add a new student")
        print("2. Remove a student")
        print("3. Exit")
        option = input("What would you like to do? ")

        if option == '1':
            add_student()
        elif option == '2':
            remove_student()
        elif option == '3':
            print("Thank you for using the Student Grades Tracker!")
            break
        else:
            print("Invalid option, please try again.")


# Main function to initiate the program
def main():
  print(welcome to)
  menu()


# Ensuring the script runs only when it's not being imported
if __name__ == "__main__":
    main()


# Instructions for Students:
# 1. Carefully read the TODO comments and implement the missing parts of the code.
# 2. Test each function separately before implementing the next one.
# 3. Make sure to handle errors gracefully where indicated.
# 4. Feel free to add additional features or improve the user interface as an extra challenge.
