# Python Basics - Numbers

Unlock the world of Python by mastering the basics of numbers and lists.

---

## Numbers in Python

Numbers are the building blocks in programming. In Python, you can perform various operations with numbers, making your programs dynamic and powerful.

### Types of Numbers

Python mainly deals with two types of numbers:

1. **Integers (Int):** Whole numbers like 3, 300, or -5.
2. **Floats:** Numbers with a decimal point, like 0.5, -1.25, or 3.14.

---

### Operations with Integers

You can add (`+`), subtract (`-`), multiply (`*`), and divide (`/`) numbers in Python.

Example:
```python
print(2 + 3)  # Output: 5
print(3 - 2)  # Output: 1
print(2 * 3)  # Output: 6
print(3 / 2)  # Output: 1.5
```

Python also supports exponentiation (`**`) and follows the order of operations (PEMDAS).

---

### Floats and Precision

Floats are numbers that have decimal points, like 3.14, 0.5, or -2.718. 
While working with floats, remember that the result may have an arbitrary number of decimal places, which can be surprising.

**Creating Floats:**
  - Use a decimal point: `number = 3.14`
  - Use scientific notation: `number = 6.022e23` (which means 6.022 x 10^23)

Example:
```python
print(0.2 + 0.1)  # Output: 0.30000000000000004
```

**Precision: Not Always Exact**

- **Limited Storage:** Computers can only store a limited amount of information for each float.
- **Rounding:** This can lead to rounding errors, meaning some decimal values might not be stored perfectly.
- **Example:**
  ```python
  print(0.1 + 0.2)  # Output: 0.30000000000000004
  ```
  - The result is slightly off due to rounding.

**Key Points:**

- **Don't compare floats directly with `==`:** It might not give accurate results due to rounding errors. Use a small tolerance instead.
- **Be aware of precision limitations:** Especially in calculations where accuracy is crucial, like financial calculations or scientific simulations.
- **Format for readability:** Use `f-strings` or `format()` to control how many decimal places are displayed:
  ```python
  result = 0.1 + 0.2
  print(f"The result is {result:.2f}")  # Output: The result is 0.30
  ```

**Additional Tips for Python:**

- **Python uses 64-bit floats by default:** This provides good precision for most tasks.
- **For higher precision, explore libraries:** If you need even more precise decimal handling, consider libraries like `decimal` or `gmpy2`.

---

### Constants and Variables

Constants are like unchangeable variables. Python doesn’t have built-in constant types, so we use all capital letters to indicate a variable should be treated as a constant.

Example:
```python
MAX_CONNECTIONS = 5000
PI = 3.14
```

---

# Questions and Exercises

## Multiple Choice Questions

1. Which operation is used for exponentiation in Python?
   - a) `*`
   - b) `^`
   - c) `**`
   - d) `//`
   
2. What would be the output of `print(3 / 2)` in Python?
   - a) `1`
   - b) `1.5`
   - c) `2`
   - d) `0.5`

3. Match the concept on the left with its correct description on the right.
   - Integer
   - Float
   - `**`
   - `//`
   - a) A type of number with decimal points
   - b) A type of number without decimal points
   - c) Used for exponentiation in Python
   - d) Performs floor division

---

<details>
  
<summary>Exercise 1: Playing with Numbers</summary>

Create four different operations (addition, subtraction, multiplication, division) that result in a number given by the user. Display the results using `print()`.

Example for number 8:
```python
print(5 + 3)
print(10 - 2)
print(4 * 2)
print(16 / 2)
```

</details>

---

<details>

<summary>Exercise 2: Your Favorite Number</summary>

Store your favorite number in a variable and use it to create a message that reveals your favorite number. Display the message.

Example:
```python
favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)
```

</details>

---

<details>

<summary>Exercise 3: The Age Calculator</summary>

Create a program that calculates a person's age in years, months, and days.

1. Ask the user to enter their birth year, month, and day.
2. Calculate and print their age in years, months, and days based on the current date.

_Hint: You may want to explore Python's `datetime` module for dealing with dates._


</details>

---

<details>
  
<summary>Exercise 4: Grade Calculator (advanced and optional) </summary>

Simulate a grading system that calculates the final grade based on multiple scores.

1. Ask the user to input scores for assignments, quizzes, and the final exam.
2. Each category should have its own weight (e.g., assignments 40%, quizzes 20%, final exam 40%).
3. Calculate and display the final weighted grade.

_Hint: Ensure the weights add up to 100%._


</details>

---

<details>

<summary>Exercise 5: Multiplication Quiz</summary>

Develop a quiz program that tests the user's multiplication skills.

1. The program should randomly generate two numbers to multiply.
2. Ask the user to input the answer.
3. Check the answer and give feedback (correct or incorrect).
4. Repeat the process for a set number of times and then display the final score.

_Hint: Use the `random` module to generate numbers._

</details>

---

<details>
  
<summary>Exercise 6: Restaurant Bill Calculator</summary>

Create a program that calculates the total bill at a restaurant, including tax and tip.

1. Ask the user to input the cost of their meal.
2. Add a specific percentage for tax and another percentage for the tip.
3. Display the meal cost, tax amount, tip amount, and total bill.

_Hint: Ensure that percentages are converted correctly for calculations._

</details>

