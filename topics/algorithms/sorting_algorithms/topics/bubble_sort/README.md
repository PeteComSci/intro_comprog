# Introduction to Bubble Sort

Welcome to our lesson on sorting algorithms, focusing on one of the simplest methods to understand and implement: **Bubble Sort**. Whether you realize it or not, sorting is a fundamental aspect of our daily lives and computer science. Let's dive into the world of algorithms together, starting with the basics!

## What is a Sorting Algorithm?

A sorting algorithm is a method for rearranging a list or array of items in a certain order - typically ascending or descending. Think about organizing your bookshelf by height or arranging your playlist by song length. In computer science, sorting helps manage and analyze data more efficiently.

## Why Learn About Sorting?

Sorting is everywhere! From the contacts list on your phone to the search results on the web, efficient sorting is key to quick access and data processing. By learning how sorting algorithms work, you're unlocking one of the core principles of computer science.

## Introducing Bubble Sort

Bubble Sort is a straightforward sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process resembles bubbles rising to the surface, hence the name.

### How Bubble Sort Works

The bubble sort algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted. Here’s a step-by-step breakdown:

1. **Starting from the beginning of the list:** The algorithm compares the first two adjacent elements.
2. **Comparison and Swap (if necessary):** If the first element is greater than the second (for ascending order; reverse for descending order), the algorithm swaps them.
3. **Move to the next pair:** The process is repeated for each pair of adjacent elements down the list.
4. **Completing the pass:** The first pass through the list places the largest element in its final position.
5. **Repeat the process:** The algorithm repeats this process for the remaining list (excluding the last sorted elements).
6. **Termination:** The algorithm terminates when a pass through the list requires no swaps, indicating that the list is sorted.

### Pseudocode for Bubble Sort

The pseudocode for the bubble sort algorithm emphasizes its simplicity:

```plaintext
FUNCTION BubbleSort(LIST_TO_SORT)
    // This function sorts a list in ascending order using the bubble sort algorithm.

    // A flag to check if any swaps have occurred in the current pass.
    SWAP_HAPPENED = TRUE
    
    // Continue looping until a pass occurs where no swaps are made.
    WHILE SWAP_HAPPENED
        // Initially assume no swap will occur in this pass.
        SWAP_HAPPENED = FALSE
        
        // Iterate over the list from the first element (0) up to the second-to-last element.
        // The range is inclusive, hence we use LENGTH(LIST_TO_SORT) - 2.
        FOR I = 0 TO LENGTH(LIST_TO_SORT) - 2
            // Compare the current element with the next element.
            IF LIST_TO_SORT[I] > LIST_TO_SORT[I + 1] THEN
                // Swap the elements to order them.
                TEMP = LIST_TO_SORT[I]
                LIST_TO_SORT[I] = LIST_TO_SORT[I + 1]
                LIST_TO_SORT[I + 1] = TEMP
                
                // Mark that a swap has occurred, so another pass is needed.
                SWAP_HAPPENED = TRUE
            ENDIF
        ENDFOR
    ENDWHILE
    
    // Once no swaps occur in a pass, the list is sorted, and we can return it.
    RETURN LIST_TO_SORT
ENDFUNCTION

```

## Visualizing Bubble Sort

Imagine you have a row of numbered cards:

```
5 3 8 4 2
```

**Bubble Sort** will compare and swap these cards until they are in ascending order:

```
3 5 4 2 8 -> 3 4 2 5 8 -> 3 2 4 5 8 -> 2 3 4 5 8
```

## Activity Time: Role Play Bubble Sort

To help us better understand bubble sort, we'll do a fun role-play activity. You'll stand in a line, and each of you will be an element in an array. By comparing and "swapping" places with each other, you'll physically act out the bubble sort!


## Online Resources

Go to https://www.toptal.com/developers/sorting-algorithms and test run different algorithms and observe the difference.

Sorting Algorithm Animation System (SAAS) features a very clear comparison of [sort algorithms](https://www.mundayweb.com/html/Sorting%20Algorithm%20Animation%20System%20%28SAAS%29.html) using animation. This animation can also be downloaded for offline use at any time.

---

### Bubble Sort in Python
Here's a typical implementation of bubble sort in Python:

```python
def bubble_sort(list_to_sort):
    """
    Sorts a list in ascending order using the bubble sort algorithm.
    
    Arguments:
    list_to_sort -- the list to be sorted
    
    Returns:
    The sorted list.
    """
    
    # Initialize a flag to track whether a swap has occurred in the current pass.
    # The algorithm needs to continue as long as at least one swap has been made in a pass,
    # indicating that the list may still be out of order.
    swap_happened = True
    
    # Continue looping until a pass occurs where no swaps are made,
    # indicating the list is sorted.
    while swap_happened:
        # Assume no swap will occur in this pass. If no swap occurs, the list is sorted,
        # and the loop will terminate.
        swap_happened = False
        
        # Iterate over the list, stopping one element before the last to avoid index out of range errors
        # when comparing an element to its next neighbor.
        for i in range(len(list_to_sort) - 1):
            # If the current element is greater than the next element, a swap is needed.
            if list_to_sort[i] > list_to_sort[i + 1]:
                # Swap the elements to order them. This is done by temporary storing
                # one of the values before overwriting its slot in the list.
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
                
                # Since a swap occurred, we set the flag to True to indicate another pass is needed.
                swap_happened = True
    
    # Once no swaps occur in a pass, the list is sorted, and we can return it.
    return list_to_sort

```
<details>

<summary>Explantations</summary>

Let's break down the provided `bubble_sort` function and align each part of the code with the corresponding steps in the bubble sort algorithm.

### Function Definition
```python
def bubble_sort(list_to_sort):
```
This line defines a function in Python named `bubble_sort`, which takes one argument, `list_to_sort`. This is the list of elements that will be sorted in ascending order.

### Docstring
```python
"""
Sorts a list in ascending order using the bubble sort algorithm.

Arguments:
list_to_sort -- the list to be sorted

Returns:
The sorted list.
"""
```
Here is a docstring providing documentation on what the function does, the argument it takes, and what it returns.

### Initialization of the Swap Flag
```python
swap_happened = True
```
We declare a variable `swap_happened` and initialize it to `True`. This flag will be used to determine if a pass through the list resulted in any swaps. If no swaps occur, it means the list is sorted, and the algorithm can stop running.

### While Loop to Repeat Passes
```python
while swap_happened:
```
This `while` loop will keep running as long as `swap_happened` is `True`. A single pass through the list occurs within this loop, and if the list is already sorted, the flag will not be set to `True` again, which will break the loop and end the function.

### Resetting the Swap Flag
```python
swap_happened = False
```
Before each pass begins, we reset `swap_happened` to `False`. The assumption is that no swaps will be needed and the list is sorted. If a swap happens, this will be set back to `True`.

### For Loop for Comparing Adjacent Elements
```python
for i in range(len(list_to_sort) - 1):
```
This `for` loop goes through the list from the start to the second-to-last element. It avoids out-of-range errors that would occur if we tried to compare the last element to a non-existent "next" element.

### Comparison and Potential Swap
```python
if list_to_sort[i] > list_to_sort[i + 1]:
    temp = list_to_sort[i]
    list_to_sort[i] = list_to_sort[i + 1]
    list_to_sort[i + 1] = temp
    swap_happened = True
```
Inside the loop, we compare each element `i` with the element directly after it `i + 1`. If element `i` is greater than element `i + 1`, they are out of order, and we must swap them. The swap is done using a temporary variable `temp` to hold the value of `list_to_sort[i]` before we overwrite it. After swapping, we set `swap_happened` to `True`, indicating that a swap has occurred and another pass may be necessary.

### Loop Completion and Returning the Sorted List
```python
return list_to_sort
```
Once the while loop has completed without any swaps being made in the final pass, `swap_happened` remains `False`, signifying that the list is sorted. The sorted list is then returned.

### Bubble Sort Algorithm Steps and Their Implementation in Code
Here's how the steps of the bubble sort algorithm correspond to the sections of the code:
1. Start with the first element in the list (implicit in the for loop).
2. Compare it to the next element.
3. If the first is greater than the second, swap them (the `if` statement and the lines that follow).
4. Move to the next element and repeat the comparison and potential swap until you reach the end of the list (the for loop).
5. At the end of the list, check if any swaps were made (controlled by the `swap_happened` flag).
   - If yes, perform another pass (the while loop continues).
   - If no, the list is sorted, and the algorithm terminates (the while loop ends, and the function returns the sorted list).

</details>

---

### Use of While Loop

1. **Adaptive Looping**: The `while` loop is used because the number of iterations needed to sort the list is not known in advance and depends on the data's initial order. A `for` loop is generally used when the number of iterations is known before entering the loop. In contrast, a `while` loop is ideal for situations where the loop must continue until a certain condition is met, such as no more swaps being necessary, indicating that the list is sorted.

2. **Flexibility**: The `while` loop provides flexibility to stop the iterations based on the sorting progress (i.e., if the list becomes sorted before going through all the potential passes). This is dynamically determined during runtime by whether any swaps were made during a pass through the list.

### Use of a Flag (`swap`) vs. Break

1. **Clarity and Intent**: Using a boolean flag (`swap`) to control the loop's execution clearly communicates the algorithm's intention—to continue sorting until no swaps are necessary. This approach enhances readability and understanding, making it clear that the sorting process is conditionally continuous rather than finite.

2. **Control Flow**: The flag provides a straightforward mechanism to manage the loop's execution based on the actual sorting process's state. If at least one swap is made during a pass, the algorithm needs another pass to ensure the list is sorted. The absence of swaps indicates the completion of sorting, allowing the loop to terminate naturally. This method avoids abrupt interruptions in the loop's flow, which could happen with a `break` statement, offering a more structured control flow that aligns with the algorithm's logic.

3. **Extensibility and Debugging**: Using a flag can also simplify debugging and extending the algorithm. For example, if additional actions or checks needed to be performed before exiting the loop (such as logging, or implementing some optimization), having a flag makes it easier to insert these actions before the loop naturally terminates, rather than immediately exiting the loop with a `break` statement.

In essence, the use of a `while` loop and a boolean flag in the bubble sort algorithm enhances its adaptability, readability, and control flow management. It aligns the implementation closely with the algorithm's logical requirements, providing a clear and efficient approach to achieving a sorted list.

---

### Examples

### Bubble Sort by String Length
This version will sort strings by their length. You need to replace the comparison condition to compare the lengths of the strings (`len(string)`) instead of the string values themselves.

```python
def bubble_sort_by_length(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            if len(list_to_sort[i]) > len(list_to_sort[i + 1]):
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
                swap_happened = True
    return list_to_sort
```

### Bubble Sort Alphabetically
This version will sort strings alphabetically. In Python, strings are compared based on lexicographical order by default, so you can use the greater-than operator to compare strings alphabetically.

<details>

<summary>Detailed Explanations</summary>

In Python, strings are sequences of characters, and when you compare two strings, the comparison is performed lexicographically. This is somewhat similar to how words are arranged in a dictionary, which is why it's often referred to as "dictionary order" or "alphabetical order."

Here's what happens during lexicographical comparison:

1. The comparison starts with the first character of each string.
2. If the characters are different, their Unicode values (essentially their numeric representations) are compared. The string with the lower Unicode value is considered "less" than the other string.
3. If the first characters are the same, the comparison moves on to the next character, and so on.
4. This process continues until a difference is found or until the end of one of the strings is reached.
5. If one string is a prefix of another (like "apple" and "app"), the shorter string is considered "less" than the longer one.

Here's a practical example:

```python
string1 = "apple"
string2 = "banana"

# The first characters are 'a' and 'b', so their Unicode values are compared.
# Since 'a' < 'b', "apple" is considered less than "banana".
result = string1 < string2  # This will be True
```

In the case where strings have mixed case (upper and lower case), Python compares them using the Unicode values, where all upper case letters have lower values than lower case letters:

```python
string1 = "Apple"
string2 = "apple"

# The first characters are 'A' (Unicode 65) and 'a' (Unicode 97).
# Since the Unicode value of 'A' is less than that of 'a', "Apple" is considered less than "apple".
result = string1 < string2  # This will be True
```

If you want to compare strings alphabetically without considering the case (i.e., treat "Apple" and "apple" as equal), you should convert both strings to either lower case or upper case before comparison:

```python
string1 = "Apple".lower()
string2 = "apple".lower()

# After converting both strings to lower case, they are considered equal.
result = string1 == string2  # This will be True
```

Using these principles, you can use relational operators like `<` (less than), `>` (greater than), `==` (equal to), etc., to compare strings in Python based on their lexicographical order.

</details>

```python
def bubble_sort_alphabetically(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i].lower() > list_to_sort[i + 1].lower():
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i + 1]
                list_to_sort[i + 1] = temp
                swap_happened = True
    return list_to_sort
```

Note that for alphabetical sorting, we use the `.lower()` method to ensure the comparison is case-insensitive, as Python string comparison is case-sensitive by default, and uppercase letters are considered less than lowercase letters.

### Comprehensive Example
Now let's combine both sorting by length and then alphabetically within the same bubble sort function:

```python
def bubble_sort_strings(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            # Sort primarily by length
            if len(list_to_sort[i]) > len(list_to_sort[i + 1]):
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_happened = True
            # If lengths are equal, sort alphabetically
            elif len(list_to_sort[i]) == len(list_to_sort[i + 1]) and list_to_sort[i].lower() > list_to_sort[i + 1].lower():
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_happened = True
    return list_to_sort
```

---

<details>

<summary>Examples - Sorting Strings</summary>

### Example 1: Case Insensitive Alphabetical Sorting of Names

Suppose you have a list of names and you want to sort them alphabetically without considering the case sensitivity:

```python
names = ["Alice", "bob", "alex", "Bob", "Clara", "claire"]

def bubble_sort_case_insensitive(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i].lower() > list_to_sort[i + 1].lower():
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_happened = True
    return list_to_sort

sorted_names = bubble_sort_case_insensitive(names)
```

After sorting, `sorted_names` will be:

```
["alex", "Alice", "bob", "Bob", "Clara", "claire"]
```

Notice how names that start with the same letter are sorted regardless of their case, e.g., "Alice" and "alex".

---

### Example 2: Sorting Strings by Last Character

Let's sort strings by their last character. If the last characters are the same, we'll sort them by the first character:

```python
words = ["banana", "apple", "cherry", "date", "grape", "fig"]

def bubble_sort_by_last_char(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            last_char1 = list_to_sort[i][-1]
            last_char2 = list_to_sort[i + 1][-1]
            if last_char1 > last_char2 or (last_char1 == last_char2 and list_to_sort[i] > list_to_sort[i + 1]):
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_happened = True
    return list_to_sort

sorted_words = bubble_sort_by_last_char(words)
```

<details>

<summary>Using `len()` from String stead of `[-1]`</summary>

To simplify the code with a focus on detailed computational steps using built-in functions in Python's String module, we'll employ more descriptive and foundational string handling techniques. Since the goal is to access the last character of strings in a list, we can use a combination of foundational Python string functions such as `len()` and direct indexing to achieve this.

```python
def get_last_character_explicit(string):
    """
    This function returns the last character of a given string in a more explicit manner,
    utilizing the len() function and direct indexing.
    """
    # Calculate the length of the string
    string_length = len(string)
    # Access the last character using the length - 1, as indices start at 0
    last_character = string[string_length - 1]
    return last_character

# Assuming list_to_sort is a list of strings and i is the current index we are examining
# Example: list_to_sort = ['apple', 'banana', 'cherry'], i = 0

# Use the function to get the last character of strings at indices i and i + 1 in list_to_sort
last_char1 = get_last_character_explicit(list_to_sort[i])
last_char2 = get_last_character_explicit(list_to_sort[i + 1])
```

This approach uses basic Python functions and operations to achieve the same result as the original code. By employing `len()` to determine the string's length and then subtracting 1 to get the index of the last character, we make the computational steps explicit and clear. This method enhances understanding, especially for beginners, by highlighting how string manipulation and indexing work in Python.

</details>

After sorting, `sorted_words` will be:

```
["banana", "apple", "grape", "date", "fig", "cherry"]
```

In this example, "banana" and "apple" are sorted because "a" (from "banana") comes before "e" (from "apple"), even though "banana" comes after "apple" in standard alphabetical order.

---

### Example 3: Sorting Strings by Their Reverse

Now imagine you want to sort strings based on their reverse. This could be a fun way to look for potential palindromes or just to sort in a non-standard way:

```python
phrases = ["step on no pets", "able was I saw elba", "no lemon no melon"]

def bubble_sort_by_reverse(list_to_sort):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(len(list_to_sort) - 1):
            if list_to_sort[i][::-1] > list_to_sort[i + 1][::-1]:
                list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
                swap_happened = True
    return list_to_sort

sorted_phrases = bubble_sort_by_reverse(phrases)
```

After sorting, `sorted_phrases` will be:

```
["able was I saw elba", "no lemon no melon", "step on no pets"]
```

This example shows sorting based on the reversed strings, which places "able was I saw elba" before "no lemon no melon", due to the reverse of "elba" being "able", which comes alphabetically before "nom".

These examples demonstrate how flexible and fun string comparison can be when you incorporate it into sorting algorithms like bubble sort. You can set up various criteria for comparison to achieve different sorting behaviors.

</details>

---

<details>

<summary>Advanced Examples - Sorting Numbers</summary>

### Example 1: Sorting Numbers by Number of Divisors

```python
def bubble_sort_by_divisors(numbers):
    n = len(numbers)
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(n - 1):
            count_i = 0
            count_j = 0
            # Count divisors for numbers[i]
            for div_i in range(1, numbers[i] + 1):
                if numbers[i] % div_i == 0:
                    count_i += 1
            # Count divisors for numbers[i + 1]
            for div_j in range(1, numbers[i + 1] + 1):
                if numbers[i + 1] % div_j == 0:
                    count_j += 1
            if count_i > count_j:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                swap_happened = True
    return numbers
```

---

### Example 2: Sorting Numbers by Proximity to a Given Value

```python
def bubble_sort_by_proximity(numbers, pivot):
    n = len(numbers)
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(n - 1):
            proximity_i = abs(numbers[i] - pivot)
            proximity_j = abs(numbers[i + 1] - pivot)
            if proximity_i > proximity_j:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                swap_happened = True
    return numbers
```

---

### Example 3: Sorting Numbers by Sum of Digits

```python
def bubble_sort_by_digit_sum(numbers):
    n = len(numbers)
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for i in range(n - 1):
            sum_i = 0
            num_i = numbers[i]
            sum_j = 0
            num_j = numbers[i + 1]
            # Calculate sum of digits for numbers[i]
            while num_i > 0:
                sum_i += num_i % 10
                num_i //= 10
            # Calculate sum of digits for numbers[i + 1]
            while num_j > 0:
                sum_j += num_j % 10
                num_j //= 10
            if sum_i > sum_j:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                swap_happened = True
    return numbers
```

</details>

---

<details>

<summary>Complexity Analysis</summary>

- **Time Complexity:**
  - **Best Case (already sorted list):** O(n). Only one pass through the list is needed.
  - **Average and Worst Case (random list or reverse sorted list):** O(n^2). Each element needs to be compared to every other element.
- **Space Complexity:** O(1). Bubble sort is an in-place sorting algorithm that requires no additional storage space apart from temporary variables.

</details>

<details>

<summary>Advantages</summary>

- **Simplicity:** Bubble sort is straightforward to understand and implement.
- **No Additional Memory Needed:** It sorts the list in place, requiring minimal extra storage.
- **Adaptive:** It can be optimized to stop early if the list becomes sorted before completing all the passes.
- **Detection of a Sorted List:** It can detect that the list is already sorted and terminate early.

</details>

<details>

<summary>Disadvantages</summary>

- **Inefficiency:** Bubble sort is less efficient compared to other sorting algorithms like quicksort, mergesort, or heapsort, especially on large lists.
- **Performance:** Its quadratic time complexity makes it impractical for datasets that are not small or nearly sorted.

</details>

<details>

<summary>Use Cases</summary>

Despite its inefficiencies, bubble sort has its place in educational environments for teaching basic algorithm concepts. It's also suitable for small datasets or nearly sorted datasets where its simplicity and the property of being adaptive can be advantageous.

</details>

---

### Sort List in Ascending Order (Beginner)

**Objective:**  
Sort a list of integers in ascending order. Use the bubble sort algorithm to achieve this.

**Instructions:**

1. Compare each pair of adjacent elements in the list.
2. Swap them if they are in the wrong order (the first is greater than the second).
3. Continue this process until the entire list is sorted in ascending order.

**Starter Code:**

```python
def ascending_bubble_sort(numbers):
    # Implement the bubble sort logic here to sort the list in ascending order
    
    return numbers

# Test the function with this list
test_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = ascending_bubble_sort(test_list)
print(sorted_list)
```

**Expected Output:**  
```
[11, 12, 22, 25, 34, 64, 90]
```

---

### Sort Negative Numbers (Beginner)

**Objective:**  
Given a list that includes both positive and negative integers, sort the list so that all negative numbers come before positive numbers. Ignore the order among negative or positive numbers.

**Instructions:**

1. Modify the bubble sort algorithm to prioritize moving negative numbers to the beginning of the list.
2. You don’t need to sort the negative numbers or the positive numbers among themselves; just separate negatives from positives.

**Starter Code:**

```python
def sort_negatives(numbers):
    # Modify the bubble sort logic to move negative numbers to the start of the list
    
    return numbers

# Test the function with this list
test_list = [3, -1, -4, 0, -2, 5, -3]
sorted_list = sort_negatives(test_list)
print(sorted_list)
```

**Expected Output:**  
The exact order of negative and positive numbers may vary, but all negative numbers should come before any non-negative numbers, for example:
```
[-1, -4, -2, -3, 3, 0, 5]
```

---

### Sort Even Numbers (Beginner)

**Objective:**  
Sort a list of integers such that all even numbers are at the beginning of the list. The order among even or odd numbers does not matter.

**Instructions:**

1. Apply bubble sort modifications to move all even numbers to the start of the list.
2. The internal order among even or odd numbers does not need to be sorted.

**Starter Code:**

```python
def sort_evens_first(numbers):
    # Adjust the bubble sort to place even numbers at the beginning of the list
    
    return numbers

# Test the function with this list
test_list = [1, 2, 4, 3, 7, 16, 10]
sorted_list = sort_evens_first(test_list)
print(sorted_list)
```

**Expected Output:**  
The exact order of even and odd numbers may vary, but all even numbers should come before any odd numbers, for example:
```
[2, 4, 16, 10, 1, 3, 7]
```

---

### Exercise 1: Favorite Colors Sorter (Easy)

**Objective:**  
You and your friends have listed your favorite colors. Sort this list in alphabetical order using bubble sort to easily find who likes what color.

**Instructions:**

1. Given a list of favorite colors, sort them alphabetically.
2. Use bubble sort algorithm for sorting.
3. This exercise helps understand how strings can be sorted using their alphabetical order.

**Starter Code:**

```python
def favorite_colors_sorter(colors):
    # Implement bubble sort for alphabetical sorting
    
    return colors

# List of favorite colors
favorite_colors = ["blue", "red", "green", "yellow", "purple"]
print(favorite_colors_sorter(favorite_colors))
```

### Exercise 2: Class Attendance Sorter (Easy)

**Objective:**  
Your teacher has a list of students' names and their attendance counts. Sort the students by their attendance counts in ascending order using bubble sort.

**Instructions:**

1. Given parallel lists: one with student names and one with their attendance counts, sort the students based on their attendance counts in ascending order.
2. Maintain the association between student names and their attendance counts.
3. This exercise helps understand sorting with parallel lists and the importance of maintaining associations between them.

**Starter Code:**

```python
def class_attendance_sorter(names, attendance):
    # Implement bubble sort to sort by attendance, keeping names associated with their respective attendance counts
    
    return names, attendance

# Student names and their corresponding attendance counts
student_names = ["Emma", "John", "Mike", "Lily", "Rose"]
attendance_counts = [23, 45, 12, 34, 29]
sorted_names, sorted_attendance = class_attendance_sorter(student_names, attendance_counts)
print(sorted_names)
print(sorted_attendance)
```

### Exercise 3: Group Project Teams (Easy)

**Objective:**  
For a group project, students were randomly assigned numbers. Sort the students into teams based on these numbers in ascending order using bubble sort.

**Instructions:**

1. Given a list of student names and a parallel list of team numbers, sort the students into their teams by sorting the team numbers in ascending order.
2. Ensure that student names stay associated with their original team numbers.
3. This exercise demonstrates the use of parallel lists and sorting to organize group assignments.

**Starter Code:**

```python
def group_project_teams(names, team_numbers):
    # Implement bubble sort to sort students into teams by team number
    
    return names, team_numbers

# Student names and their assigned team numbers
student_names = ["Sophia", "Lucas", "Mia", "Jackson", "Ava"]
team_numbers = [3, 1, 4, 2, 5]
sorted_names, sorted_teams = group_project_teams(student_names, team_numbers)
print(sorted_names)
print(sorted_teams)
```

#### Exercise 4: Library Book Sorter (Easy)

**Objective:**  
A small library wants to sort books based on their ID numbers in ascending order to make inventory checks easier.

**Instructions:**

1. Given a list of book titles and a parallel list of book ID numbers, sort the books by their ID numbers in ascending order.
2. Keep the titles associated with their respective ID numbers.
3. Use bubble sort for the sorting mechanism.

**Starter Code:**

```python
def library_book_sorter(titles, ids):
    # Your bubble sort logic here
    
    return titles, ids

# Book titles and their ID numbers
book_titles = ["The Great Gatsby", "1984", "Moby-Dick", "Hamlet", "War and Peace"]
book_ids = [3, 2, 5, 1, 4]
sorted_titles, sorted_ids = library_book_sorter(book_titles, book_ids)
print("Sorted Titles:", sorted_titles)
print("Sorted IDs:", sorted_ids)
```

#### Exercise 5: Sports Team Draft Picks (Easy)

**Objective:**  
A sports league is conducting a draft where teams pick players in turns. Each team's next pick number is listed, and you need to sort the teams based on their upcoming draft pick number.

**Instructions:**

1. Given a list of team names and a parallel list of their next draft pick numbers, sort the teams by their pick numbers in ascending order.
2. Maintain the association between team names and their draft pick numbers.
3. Implement the sorting using bubble sort.

**Starter Code:**

```python
def sports_team_draft_picks(teams, pick_numbers):
    # Your bubble sort logic here
    
    return teams, pick_numbers

# Team names and their next draft pick numbers
team_names = ["Lions", "Tigers", "Bears", "Hawks", "Eagles"]
draft_pick_numbers = [32, 15, 7, 22, 3]
sorted_teams, sorted_picks = sports_team_draft_picks(team_names, draft_pick_numbers)
print("Sorted Teams:", sorted_teams)
print("Sorted Draft Picks:", sorted_picks)
```

### Exercise 6: Sort Even and Odd Numbers Separately (Medium)

**Objective:**  
Modify the bubble sort algorithm to sort even numbers in ascending order and odd numbers in descending order within the same list.

**Instructions:**

1. Use a `while` loop to continue sorting until no swaps are needed.
2. Inside the `while` loop, use a `for` loop to traverse the list.
3. Determine if two adjacent numbers are both even or both odd.
4. Swap even numbers if the left is greater than the right for ascending order.
5. Swap odd numbers if the left is less than the right for descending order.
6. Ensure even and odd numbers are sorted within their own groups according to the specified order.

**Starter Code:**

```python
def sort_even_odd_separately(numbers):
    n = len(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            # Hint: Use conditions to check parity and decide on swapping logic
            # Your swapping logic here
    return numbers

# Test the function
test_list = [5, 8, 6, 3, 4, 2, 1, 7, 9]
print(sort_even_odd_separately(test_list))
```

---

## Integrating Bubble Sort Into a Program

Finally, you'll get to integrate the bubble sort function into a real program, enhancing its functionality by sorting data such as a list of names or scores.
