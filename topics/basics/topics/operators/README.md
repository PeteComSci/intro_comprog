# Basic Operators

Basic operators in programming are the symbols that tell the computer to perform specific mathematical, relational, or logical operations. They are fundamental in manipulating data and implementing logic in your code. Let's explore the three main types of operators: arithmetic, comparison, and logical operators.

---

### Arithmetic Operators

Arithmetic operators are used to perform common mathematical operations.

#### Python Example: Arithmetic Operators

```python
# Arithmetic Operators in Python

# Variables for demonstration
number1 = 10
number2 = 3

# Addition
sum = number1 + number2
print("Sum:", sum)  # Output: 13

# Subtraction
difference = number1 - number2
print("Difference:", difference)  # Output: 7

# Multiplication
product = number1 * number2
print("Product:", product)  # Output: 30

# Division
quotient = number1 / number2
print("Quotient:", quotient)  # Output: 3.333...

# Floor Division
floor_division = number1 // number2
print("Floor Division:", floor_division)  # Output: 3

# Modulus (remainder of division)
remainder = number1 % number2
print("Remainder:", remainder)  # Output: 1

# Exponentiation (power)
power = number1 ** number2
print("Power:", power)  # Output: 1000
```

---

> [!NOTE]
> You can find some [Python and Pseudocode examples here](https://github.com/PeteComSci/intro_comprog/tree/main/topics/basics/topics/operators/examples/python).

---

### Comparison Operators

Comparison operators are used to compare values. They return a Boolean value (`True` or `False`).

#### Python Example: Comparison Operators

```python
# Comparison Operators in Python

# Variables for demonstration
a = 10
b = 20

# Equal to
print("a equals b:", a == b)  # Output: False

# Not equal to
print("a not equal to b:", a != b)  # Output: True

# Greater than
print("a greater than b:", a > b)  # Output: False

# Less than
print("a less than b:", a < b)  # Output: True

# Greater than or equal to
print("a greater than or equal to b:", a >= b)  # Output: False

# Less than or equal to
print("a less than or equal to b:", a <= b)  # Output: True
```

---

### Logical Operators

Logical operators are used to combine conditional statements.

#### Python Example: Logical Operators

```python
# Logical Operators in Python

# Variables for demonstration
x = True
y = False

# Logical AND
print("x AND y is", x and y)  # Output: False

# Logical OR
print("x OR y is", x or y)  # Output: True

# Logical NOT
print("NOT x is", not x)  # Output: False
```

---

In the examples above:
- Arithmetic operators perform mathematical calculations.
- Comparison operators compare values and return `True` or `False`.
- Logical operators combine boolean values and return `True` or `False`.

---

Understanding and using these basic operators is crucial for data manipulation and implementing logic in your programs. They form the backbone of decision-making and controlling the flow of your programs.
