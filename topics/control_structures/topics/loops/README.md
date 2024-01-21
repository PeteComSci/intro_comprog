## Loops or Iterations

Loops are a fundamental concept in programming, allowing you to execute a block of code multiple times. Let's explore `for` loops, `while` loops, and the concept of `do-while` loops through detailed examples in pseudocode and Python, including inline comments for clarity.

---

### For Loops

`For` loops are used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.

#### Pseudocode Example: For Loop

```plaintext
// Pseudocode: Printing numbers from 1 to 5

For number from 1 to 5 Do
    Output number
End For
```

In this pseudocode:
- The `For` loop iterates from 1 to 5.
- The current number in the sequence is printed each iteration.

#### Python Example: For Loop

```python
# Python: Printing numbers from 1 to 5

for number in range(1, 6):
    print(number)
```

In this Python code:
- `range(1, 6)` generates a sequence of numbers from 1 to 5.
- `for` loop iterates through the sequence.
- `print()` outputs each number.

---

### While Loops

`While` loops repeatedly execute a block of code as long as a condition is true. It's crucial to ensure the condition eventually becomes false, to avoid infinite loops.

#### Pseudocode Example: While Loop

```plaintext
// Pseudocode: Counting down from 5 to 1

Set counter to 5

While counter > 0 Do
    Output counter
    Set counter to counter - 1
End While
```

In this pseudocode:
- The `While` loop continues as long as `counter` is greater than 0.
- The current value of `counter` is printed, and then `counter` is decreased by 1.

#### Python Example: While Loop

```python
# Python: Counting down from 5 to 1

counter = 5

while counter > 0:
    print(counter)
    counter -= 1
```

In this Python code:
- The `while` loop checks if `counter` is greater than 0.
- `print()` outputs the current `counter` value.
- `counter -= 1` decreases `counter` by 1 each iteration.

---

### Do-While Loops (Language-specific)

`Do-while` loops are a variant where the code block is executed at least once before the condition is checked. Python does not have a built-in `do-while` loop, but we can mimic its behavior.

#### Pseudocode Example: Do-While Loop

```plaintext
// Pseudocode: Executing a block at least once and repeating while the condition is true

Do
    // Code block
    Output "This block is executed at least once."
    // Condition for the next iteration
    Prompt "Continue? (yes/no): " and input response
While response equals "yes"
```

#### Python Example: Mimicking Do-While Loop

```python
# Python: Mimicking Do-While Loop

while True:
    print("This block is executed at least once.")
    
    response = input("Continue? (yes/no): ")
    if response != "yes":
        break
```

In this Python code:
- The loop starts with `while True:` meaning it will run indefinitely.
- After executing the code block, it prompts the user for input.
- If the response is not "yes," the `break` statement exits the loop.

---

These examples demonstrate the power of loops in programming, allowing you to execute code multiple times with dynamic conditions, making your programs more efficient and capable of handling repetitive tasks.
