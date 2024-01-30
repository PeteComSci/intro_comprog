## Conditional Statements: If, Else, and Elif

Let's dive into "Conditional Statements," specifically focusing on `if`, `else`, and `elif` statements, and also touch upon `switch/case` statements (though it's worth noting that Python does not natively support `switch/case` but can mimic similar functionality). We'll explore these concepts through detailed examples in pseudocode and Python, with inline comments for clarity.

---

Conditional statements allow the program to execute certain pieces of code based on whether a condition (or set of conditions) is true or false.

#### Pseudocode Example: Grading System

```plaintext
// Pseudocode: Grading System based on marks

// Input marks from the user
Output "Enter your marks: "
Input marks

// Determine the grade based on marks using conditional statements
If marks >= 90 Then
    Output "Grade: A"
Else If marks >= 80 Then
    Output "Grade: B"
Else If marks >= 70 Then
    Output "Grade: C"
Else If marks >= 60 Then
    Output "Grade: D"
Else
    Output "Grade: F"
End If
```

In this pseudocode:
- The `If`, `Else If`, and `Else` statements control which block of code gets executed based on the value of `marks`.
- The program outputs a grade depending on the range in which the marks fall.

---

#### Python Example: Grading System

```python
# Python: Grading System based on marks

# Input marks from the user
marks = int(input("Enter your marks: "))

# Determine the grade based on marks using conditional statements
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

In this Python code:
- The `if`, `elif`, and `else` statements are used similarly to the pseudocode to determine the grade.
- `print()` is used to display the grade.

---

### Switch/Case Statements (Language-specific)

`switch/case` statements provide an alternative to multiple `if` statements when dealing with multiple conditions. Python doesn't natively support `switch/case`, but you can use dictionaries to achieve similar functionality.

#### Python Example: Mimicking Switch/Case with Dictionary

```python
# Python: Simplified Mimicking Switch/Case using a dictionary for a simple calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# Dictionary mimicking switch/case
operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Input from user
operation = input("Enter the operation (add, subtract, multiply, divide): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check if the operation is in the dictionary
if operation in operation_dict:
    # If the operation is found, execute the corresponding function
    result = operation_dict[operation](num1, num2)
else:
    # If the operation is not found, set result to 'Invalid operation'
    result = "Invalid operation"

# Displaying the result
print("Result:", result)

```
In this Python code:
- We first check if the `operation` input by the user exists in the `operation_dict`.
- If it does, we retrieve the corresponding function from the dictionary and execute it with `num1` and `num2` as arguments.
- If it does not, we set `result` to "Invalid operation".
- Finally, we print the result.

---

These examples demonstrate how conditional statements and switch/case structures are used to direct the flow of a program based on different conditions, making your code more dynamic and responsive to user input or other variables.

---

<details>

<summary>Exercise 1: Understanding Basic Conditional Statements</summary>

Familiarize yourself with the basic structure and usage of `if`, `elif`, and `else` statements in Python.

**Instructions**:
1. Write a Python program that asks the user for an integer.
2. The program should output "Positive" if the number is greater than zero, "Negative" if the number is less than zero, and "Zero" if the number is exactly zero.

**Expected Output**: The program correctly identifies and outputs whether the input number is positive, negative, or zero.

</details>

---

<details>

<summary>Exercise 2: Enhanced Grading System</summary>

Enhance the grading system example to include more detailed feedback.

**Instructions**:
1. Modify the grading system code provided earlier.
2. Add an additional layer of feedback based on the following criteria:
   - If the grade is 'A' or 'B', output "Excellent! Keep it up."
   - If the grade is 'C', output "Good, but try to aim higher."
   - If the grade is 'D', output "You passed, but you should work harder."
   - If the grade is 'F', output "Unfortunately, you failed. Time to hit the books!"

**Expected Output**: The program outputs the grade along with a corresponding feedback message.

</details>

---

<details>

<summary>Exercise 3: Creating a Simple Calculator</summary>

Strengthen the understanding of dictionary-based conditional execution by creating a simple calculator.

**Instructions**:
1. Use the simplified mimicking `switch/case` code for a calculator as a base.
2. Extend the calculator's functionality to include the modulus operation (finding the remainder of a division).
3. Ensure that if the user tries to divide by zero or uses an invalid operation, the program outputs an appropriate error message.

**Expected Output**: The calculator should correctly perform addition, subtraction, multiplication, division, and modulus operations, or provide an error message for invalid inputs.

</details>

---

<details>

<summary>Exercise 4: Quiz - Conditional Statements</summary>

**Objective**: Test the students' understanding of conditional statements and their syntax.

**Questions**:
1. What is the purpose of the `elif` statement in Python?
2. Can an `if` statement exist without an `else` statement?
3. What will happen if the condition in an `if` statement is false and there are no `elif` or `else` blocks?

</details>

---
