## Break and Continue

The `break` and `continue` statements are essential for controlling the flow of loops. The `break` statement is used to exit a loop prematurely, while the `continue` statement is used to skip the current iteration and move to the next one. Let's explore these concepts with practical examples in both pseudocode and Python, including detailed inline comments for clarity.

---

### Break Statement

The `break` statement is used to exit a loop immediately, regardless of the loop's condition.

#### Pseudocode Example: Break Statement

```plaintext
// Pseudocode: Searching for a number in a list and stopping when found

Set numbers to [1, 3, 5, 7, 9]
Set search_number to 5
Set found to False

For each number in numbers Do
    If number equals search_number Then
        Set found to True
        Output "Number found!"
        Break
    End If
End For

If not found Then
    Output "Number not found."
End If
```

In this pseudocode:
- The `For` loop iterates through the `numbers` list.
- If the current `number` equals `search_number`, the program outputs "Number found!" and exits the loop using `Break`.
- If the loop completes without finding the number, "Number not found." is outputted.

#### Python Example: Break Statement

```python
# Python: Searching for a number in a list and stopping when found

numbers = [1, 3, 5, 7, 9]
search_number = 5
found = False

for number in numbers:
    if number == search_number:
        found = True
        print("Number found!")
        break

if not found:
    print("Number not found.")
```

In this Python code:
- The `for` loop iterates through the `numbers` list.
- If `number == search_number`, the program prints "Number found!" and exits the loop with `break`.
- If the loop completes without finding the number, "Number not found." is printed.

---

### Continue Statement

The `continue` statement is used to skip the current iteration of a loop and continue with the next iteration.

#### Pseudocode Example: Continue Statement

```plaintext
// Pseudocode: Printing only odd numbers from a list

Set numbers to [1, 2, 3, 4, 5, 6, 7, 8, 9]

For each number in numbers Do
    If number modulo 2 equals 0 Then
        Continue
    End If
    Output number
End For
```

In this pseudocode:
- The `For` loop iterates through the `numbers` list.
- If the current `number` is even (i.e., `number modulo 2 equals 0`), `Continue` skips the rest of the loop body, and the loop proceeds with the next iteration.
- Only odd numbers are outputted.

#### Python Example: Continue Statement

```python
# Python: Printing only odd numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
```

In this Python code:
- The `for` loop iterates through the `numbers` list.
- If `number % 2 == 0`, `continue` skips the rest of the loop body, and the loop proceeds with the next iteration.
- Only odd numbers are printed.

---

These examples demonstrate how the `break` and `continue` statements can be used to control the flow within loops, either by terminating the loop early or by skipping certain iterations, providing more nuanced control over your code's execution.
