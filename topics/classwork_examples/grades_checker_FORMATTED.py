"""
Program Description:

This Python program is designed as an educational tool to demonstrate various fundamental programming concepts through interactive functions.
The program features a series of functions that perform a range of operations, including:

1. Determining if a number is even or odd (chkEvOd).
2. Checking if a number is positive, negative, or zero (chkPstNgt).
3. Searching for a specific grade in a list of student grades (search).
4. Checking if a number is divisible by 5 (div5).
5. Allowing the user to check divisibility by a number of their choice (divBy).
6. Finding the highest and lowest grades in a list (highest_grade and lowest_grades).

Additionally, the program includes a menu-driven CLI interface that allows users to interactively choose which operation to perform.
Test cases are provided at the end of the program as comments to validate the functionality of each component.

The program is structured to encourage exploration of control flow, comparison operations, loops, and basic input/output operations in Python.

Usage:
Run the program and follow the on-screen prompts to explore different functionalities. Input values as requested, and observe the outputs to understand how the program processes and responds to various inputs.

Intended Audience:
This program is intended for educational use, particularly for students learning programming basics and educators seeking to provide practical programming examples.

"""

#Function to check if a given number is even or odd using modulo operation.
# The modulo operator (%) returns the remainder of division. If the remainder is 0 when divided by 2, the number is even; otherwise, it's odd.
def chkEvOd(num):
    if num % 2 == 0:  # Checks if the number is divisible by 2 with no remainder, indicating it's even.
        print("It is an even number.")
    else:
        print("It is an odd number.")

# Function to determine and print whether a number is positive, negative, or zero.
# It uses comparison operators to compare the number against zero.
def chkPstNgt(number):
    if number > 0:  # Checks if number is greater than zero, indicating it's positive.
        print("Your number is positive.")
    elif number < 0:  # Checks if number is less than zero, indicating it's negative.
        print("Your number is negative.")
    else:  # The only remaining possibility: number is exactly zero.
        print("Your number is 0.")

# Function to search for a specific grade in a list of grades.
# It uses a while loop to iterate through the list until the grade is found or the end of the list is reached.
def search(search_grade, stu_grades):
    found = False  # Initial flag to keep track of search status.
    i = 0  # Index to track the current position in the list.
    while not found and i < len(stu_grades):  # Loop until found is True or end of list is reached.
        if search_grade == stu_grades[i]:  # Check if current grade matches the search query.
            found = True  # Update flag if grade is found.
            print(f"The grade is in position/index {i} of the list.")
        else:
            i += 1  # Move to the next index if not found.

    if not found:  # After loop, check if the grade was not found and print a message.
        print("The grade is not found. Please try searching another number.")

# Function to check divisibility by 5.
# A number is divisible by 5 if the remainder of its division by 5 is 0.
def div5(number):
    if number % 5 == 0:  # Check for no remainder when divided by 5.
        print("The number is divisible by 5.")
    else:
        print("The number isn't divisible by 5.")

# Function to check divisibility by a user-defined divisor.
# It demonstrates taking user input and applying modular arithmetic.
def divBy(number):
    divisor = int(input("Enter a second integer for divisor: "))  # Prompt for a divisor.
    if number % divisor == 0:  # Modular operation to check divisibility.
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is not divisible by {divisor}.")

# Function to find the highest grade in a list.
# It iterates through the list, comparing each element to find the maximum.
def highest_grade(student_grades):
    top_grade = student_grades[0]  # Assume first grade is the highest initially.
    for index in range(1, len(student_grades)):  # Iterate starting from the second element.
        if student_grades[index] > top_grade:  # Compare current grade with the highest found so far.
            top_grade = student_grades[index]  # Update top_grade if a higher grade is found.

    print(f"The highest grade is {top_grade}.")

# Function to find the lowest grade in a list by iterating through the list and comparing each element.
def lowest_grades(students_grades):
    least_grade = students_grades[0]  # Assume first grade is the lowest initially.
    for index in range(1, len(students_grades)):
        if students_grades[index] < least_grade:  # Compare current grade with the lowest found so far.
            least_grade = students_grades[index]  # Update least_grade if a lower grade is found.

    print(f"The lowest grade is {least_grade}.")

# Main menu function to navigate through different functionalities of the program.
# It demonstrates control flow with while loop and if-elif-else statements for handling user choices.
def menu(grades):
    print("~*~ ................... ~*~ ................... ~*~")  # Decorative ASCII art for user interface.
    print("Hello, welcome to my program! Please select an option from the menu.")

    quit_prog = False
    while not quit_prog:  # Loop until the user decides to quit.
        print("~*~ ................. ~*~ ................. ~*~")  # Decorative separator.
        user_choice = input("Enter \n1 to search \n2 to check \n999 to quit. \nYour choice : ")
        if user_choice == "1":  # Handle search functionality.
            print("~*~ ................. ~*~ ................. ~*~")
            print("You have chosen to search.")
            search_grade = int(input("Enter a grade to search: "))
            search(search_grade, grades)
        elif user_choice == "2":  # Handle check functionality including various checks on a number.
            print("~*~ ................. ~*~ ................. ~*~")
            print("You have chosen to check.")
            number = int(input("Enter a number: "))
            chkPstNgt(number)
            chkEvOd(number)
            div5(number)
            divBy(number)
            highest_grade(grades)
            lowest_grades(grades)
        elif user_choice == "999":  # Handle program exit.
            quit_prog = True
            print("Goodbye! Thank you for using my program.")
        else:  # Handle invalid input.
            print("Invalid. Please try again.")

    print("~*~ ................. ~*~ ................. ~*~")  # Decorative separator for program end.

# Entry point of the program.
def main():
    grades = [5, 7, 6, 4, 2, 3]  # Sample list of grades for demonstration.
    menu(grades)  # Call the main menu function to start the program.

if __name__ == "__main__":
    main()


# Test Cases
# Instructions for Students:
# 1. Read the Test Case: Understand what the test case is trying to verify.
# 2. Run the Function: Input the given data into the function either through a driver code or interactively in an IDE.
# 3. Record the Actual Output: Write down what the program outputs in response to the input.
# 4. Compare Outputs: Check if the actual output matches the expected output.
# 5. Reflect on Discrepancies: If there's a mismatch, try to understand why. This might involve debugging the code or re-evaluating the understanding of the function's logic.

# Test 1: Check if a number is correctly identified as even
# Function: chkEvOd, Input: 4, Expected Output: "It is an even number."

# Test 2: Check if a number is correctly identified as odd
# Function: chkEvOd, Input: 3, Expected Output: "It is an odd number."

# Test 3: Verify the function identifies positive numbers
# Function: chkPstNgt, Input: 5, Expected Output: "Your number is positive."

# Test 4: Verify the function identifies negative numbers
# Function: chkPstNgt, Input: -5, Expected Output: "Your number is negative."

# Test 5: Verify the function identifies zero correctly
# Function: chkPstNgt, Input: 0, Expected Output: "Your number is 0."

# Test 6: Check if a number is correctly identified as divisible by 5
# Function: div5, Input: 10, Expected Output: "The number is divisible by 5."

# Test 7: Check if a number is correctly identified as not divisible by 5
# Function: div5, Input: 7, Expected Output: "The number isn't divisible by 5."

# Test 8: Verify the search function finds a grade that exists
# Function: search, Input: search_grade=6, stu_grades=[5, 7, 6, 4, 2, 3], Expected Output: "The grade is in position/index 2 of the list."

# Test 9: Verify the search function correctly handles a non-existent grade
# Function: search, Input: search_grade=9, stu_grades=[5, 7, 6, 4, 2, 3], Expected Output: "The grade is not found. Please try searching another number."

# Test 10: Ensure the functions identify the highest and lowest grades in a list
# Function: highest_grade, Input: student_grades=[5, 7, 6, 4, 2, 3], Expected Output: "The highest grade is 7."
# Function: lowest_grades, Input: students_grades=[5, 7, 6, 4, 2, 3], Expected Output: "The lowest grade is 2."
