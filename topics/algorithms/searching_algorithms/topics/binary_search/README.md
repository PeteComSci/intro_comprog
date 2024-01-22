# Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed down the possible locations to just one.

It is a quick way to find an item in a list that's already in order. Imagine you're looking for a specific page in a big dictionary. Instead of going through each page one by one, you start in the middle. If the page you want comes before the middle page, you then focus only on the first half of the dictionary. If it's after, you look in the second half. Then, you pick the middle page of this smaller section and repeat the process, each time cutting the number of pages you have to look at in half.
This way, you find the page you're looking for much faster than if you flipped through each page one at a time. The catch is, the list (or in our example, the dictionary) must be sorted for this to work. If it's not sorted, you're better off using a different way to search, like starting from the beginning and checking each item one by one.

---

### Pseudocode Example: Binary Search

```plaintext
// Pseudocode: Binary Search to find a word in a sorted dictionary

// The sorted array of words
Set words to ["aardvark", "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

// The word we are searching for
Set targetWord to "fig"

// Define the starting and ending index
Set startIndex to 0
Set endIndex to length of words - 1

// While the start index is less than or equal to the end index
While startIndex is less than or equal to endIndex Do
    // Find the middle index
    Set middleIndex to (startIndex + endIndex) / 2
    
    // Check if the middle word is the target word
    If words[middleIndex] equals targetWord Then
        Output "Word found at position: ", middleIndex
        Exit
    End If
    
    // If the target word is in the lower half
    If words[middleIndex] is greater than targetWord Then
        Set endIndex to middleIndex - 1
    // If the target word is in the upper half
    Else
        Set startIndex to middleIndex + 1
    End If
End While

// If the word is not found
Output "Word not found."
```

In this pseudocode:
- The list `words` is sorted and contains the words of the dictionary.
- `targetWord` is the word we are looking for.
- The search is performed within the indices `startIndex` and `endIndex`.
- We repeatedly find the `middleIndex` and compare the word at that index with `targetWord`.
- Depending on the comparison, we adjust the `startIndex` or `endIndex`.
- If `targetWord` is found, its position is outputted. Otherwise, we output that the word is not found.

---

### Python Example: Binary Search

```python
# Python: Binary Search to find a word in a sorted dictionary

# The sorted list of words
words = ["aardvark", "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

# The word we are searching for
target_word = "fig"

# Define the starting and ending index
start_index = 0
end_index = len(words) - 1

# While the start index is less than or equal to the end index
while start_index <= end_index:
    # Find the middle index
    middle_index = (start_index + end_index) // 2  # Use '//' for integer division in Python
    
    # Check if the middle word is the target word
    if words[middle_index] == target_word:
        print(f"Word found at position: {middle_index}")
        break
    
    # If the target word is in the lower half
    if words[middle_index] > target_word:
        end_index = middle_index - 1
    # If the target word is in the upper half
    else:
        start_index = middle_index + 1
else:
    # If the loop completes without finding the word
    print("Word not found.")
```

In this Python code:
- The list `words` is sorted and contains the words of the dictionary.
- `target_word` is the word we are looking for.
- The search is performed within the indices `start_index` and `end_index`.
- We repeatedly find the `middle_index` and compare the word at that index with `target_word`.
- Depending on the comparison, we adjust the `start_index` or `end_index`.
- If `target_word` is found, its position is printed. Otherwise, we print that the word is not found.

---

These examples demonstrate the binary search algorithm in both pseudocode and Python, illustrating an efficient way to search through a sorted collection by repeatedly dividing the search interval in half.
