# Exponential Search

Exponential search is an algorithm that combines the principles of binary search and jump search. It's particularly useful when dealing with unbounded or infinite lists, or when the size of the list is unknown. The algorithm works in two phases: in the first phase, it finds the range where the target could be by growing the interval exponentially, and in the second phase, it performs a binary search within that range.

---

<details>

<summary>Example: Exponential Search with Real Names</summary>

Imagine you have a list of students' names in alphabetical order, and you're looking for the name "Isaac":

`students = ["Adam", "Bella", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]`

Let's walk through how Exponential Search would help you find "Isaac":

1. **Start at the Beginning (i = 1):**
   - You start with the first name, "Adam", at the beginning of the list.
   - "Adam" comes before "Isaac" alphabetically, so you decide to jump ahead.

2. **First Jump (i = 2):**
   - You jump to the second name, "Bella".
   - "Bella" still comes before "Isaac", so you decide to jump further ahead.

3. **Second Jump (i = 4):**
   - Now, you're at "Diana".
   - "Diana" is also before "Isaac", so you make another jump.

4. **Third Jump (i = 8):**
   - This time, you land on "Hannah".
   - "Hannah" is still not "Isaac", but it's getting closer! So, you jump again, but this time you'll be careful not to jump too far.

5. **Fourth Jump (i = 16):**
   - Oops! The list doesn't have 16 names. So, you just go to the end of the list, which is "Julia".

6. **Narrowed Down the Range:**
   - Now you know "Isaac" has to be between "Hannah" and "Julia".

7. **Time to Search:**
   - You start checking each name between "Hannah" and "Julia".
   - And there it is! You find "Isaac" right after "Hannah".

In this example, Exponential Search helped you skip over a bunch of names quickly, and then you carefully checked the few names where "Isaac" could be. This method is like a quick hop and a few careful steps to find exactly what you're looking for. It's a lot faster than checking every single name from the start, especially if you had a really long list of names!

</details>

---

<details>

<summary>Trace Table</summary>
A trace table is a great way to visualize how the Exponential Search algorithm works, step by step. Let's create a trace table for the Exponential Search in our previous example, where we're looking for "Isaac" in the list of student names.

Given list: `students = ["Adam", "Bella", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]`

| Step | Jump to Index | Name at Index | Description                                                 | Next Step                                |
|------|---------------|---------------|-------------------------------------------------------------|------------------------------------------|
| 1    | 1             | "Bella"       | First jump: Start from the beginning.                        | "Bella" isn't "Isaac", so we jump ahead. |
| 2    | 2             | "Charlie"     | Second jump: Double the index to 2.                          | "Charlie" isn't "Isaac", so we jump ahead.|
| 3    | 4             | "Ethan"       | Third jump: Double the index to 4.                           | "Ethan" isn't "Isaac", so we jump ahead.  |
| 4    | 8             | "Hannah"      | Fourth jump: Double the index to 8.                          | "Hannah" isn't "Isaac", so we jump ahead. |
| 5    | 16            | (Out of Range)| Overshot: The index went beyond the list length.             | Set the search limit to the list's end.   |
| 6    | 8 to 10       | "Hannah" to "Julia" | Search range: The area where "Isaac" could be.         | Start checking names one by one.          |
| 7    | 8             | "Isaac"       | Found "Isaac": The search in the range found "Isaac".       | Search complete!                          |

In this trace table:
- Each "Step" describes what's happening at that point in the search.
- The "Jump to Index" column shows where we are in the list.
- The "Name at Index" tells us which name we're currently checking.
- The "Description" gives a simple explanation of the step.
- The "Next Step" tells us what we're going to do next based on the name we found.

This table walks you through each jump and explains why we're jumping or checking names, making it clearer how Exponential Search speeds up the process of finding a name in a sorted list.

</details>

---

Let's illustrate this with a specific example, using both pseudocode and Python, with detailed inline comments for clarity.


### Pseudocode Example: Exponential Search

```plaintext
// Pseudocode: Exponential Search to find a specific contact in a digital phonebook

// Sorted array of contacts (names)
Set contacts to ["Adam", "Bella", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]

// The contact we are searching for
Set targetContact to "Isaac"

// Start with the first element
Set i to 1

// Finding the range for binary search by doubling i each time
While i < length of contacts and contacts[i] is less than targetContact Do
    Set i to i * 2
End While

// Perform binary search between i/2 and minimum(i, length of contacts)
// Call a BinarySearch function (not detailed here) with the found range
Set position to BinarySearch(contacts, i / 2, minimum(i, length of contacts - 1), targetContact)

// Output the result
If position is not equal to -1 Then
    Output "Contact found at position: ", position
Else
    Output "Contact not found."
End If
```

In this pseudocode:
- We start with the first element and exponentially increase the index to find the range where the target could be.
- Once the range is identified, we perform a binary search in that range.
- The `BinarySearch` function is assumed to be defined elsewhere.

---

### Python Example: Exponential Search

```python
# Python: Exponential Search to find a specific contact in a digital phonebook

def binary_search(arr, left, right, target):
    # Binary search code (omitted for brevity)
    pass

# Sorted list of contacts (names)
contacts = ["Adam", "Bella", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]

# The contact we are searching for
target_contact = "Isaac"

# Start with the first element
i = 1

# Finding the range for binary search by doubling i each time
while i < len(contacts) and contacts[i] < target_contact:
    i *= 2

# Perform binary search between i/2 and minimum(i, length of contacts)
position = binary_search(contacts, i // 2, min(i, len(contacts)-1), target_contact)

# Output the result
if position != -1:
    print(f"Contact found at position: {position}")
else:
    print("Contact not found.")
```

In this Python code:
- We use the same logic as in the pseudocode to find the range where the target contact could be.
- Once the range is identified, we call the `binary_search` function to search within that range.
- `binary_search` is a placeholder for the actual binary search implementation.

Exponential search is particularly effective when the elements are exponentially distributed. The initial phase where the range is identified by doubling the index helps in quickly narrowing down the potential area where the target element could be, and the subsequent binary search phase then efficiently pinpoints the exact position of the target. This combination makes exponential search a powerful algorithm, especially for large datasets with an unknown size or when the size is infinite.
