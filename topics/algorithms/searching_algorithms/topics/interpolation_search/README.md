# Interpolation Search

Interpolation search is a searching technique that applies the principles of the binary search but with an enhancement for uniformly distributed data. Instead of always dividing the range in half, it tries to guess a better position of the target element based on its value relative to the values at the current range's boundaries. This can lead to significantly fewer steps when searching through a large, uniformly distributed dataset.

---

<details>
<summary>Example: Interpolation Search with Page Numbers</summary>

Imagine you have a textbook with 1000 pages, and you're looking for a specific topic you know starts around page 600.

Here's how Interpolation Search can efficiently find this page:

1. **Initial Boundaries:**
   - Your book has 1000 pages, so the start is page 1, and the end is page 1000.

2. **First Guess:**
   - The algorithm makes an initial guess based on the uniform distribution of pages. It calculates that the topic you're looking for (around page 600) should be roughly 60% of the way through the book.
   - So, it first checks page 600.

3. **Refine Guess:**
   - If the page it checks isn't quite right, but it's close, it'll make another guess. This time, it uses the information from the pages it has already checked to make a better guess.
   - Suppose the first guess lands at a topic that starts on page 580. The algorithm uses this information to adjust its next guess closer to where your topic should start.

4. **Narrowing Down:**
   - With each step, the algorithm narrows down the range where your topic could start, making educated guesses based on the pages it has already checked.
   - This continues until it lands on the exact starting page of your topic.

In this example, Interpolation Search uses the distribution of the data (in this case, the uniform distribution of topics across the pages) to make smarter guesses, finding your topic much faster than if it checked each page one by one or simply split the book in half each time.

</details>

---

<details>
<summary>Trace Table</summary>
A trace table helps visualize the steps taken by the Interpolation Search algorithm in finding a specific page in the textbook.

Given textbook with 1000 pages and target page around 600:

| Step | Guess  | Page Checked | Description                                                 | Next Step                                 |
|------|--------|--------------|-------------------------------------------------------------|-------------------------------------------|
| 1    | 600    | 600          | First guess based on uniform distribution.                  | Page 600 content is before the target, adjust guess forward. |
| 2    | 650    | 650          | Second guess, refined based on previous check.              | Page 650 content is after the target, adjust guess backward. |
| 3    | 625    | 625          | Third guess, further refined.                               | Page 625 content is just before the target, adjust guess slightly forward. |
| 4    | 630    | 630          | Fourth guess, close to the target.                          | Page 630 is the start of the target topic. Search complete!  |

In this trace table:
- Each "Step" shows the algorithm's current action.
- The "Guess" column indicates the page the algorithm decides to check next.
- The "Page Checked" tells us which page is currently being reviewed.
- The "Description" provides insight into why the algorithm makes its next move.
- The "Next Step" anticipates the algorithm's action based on the page content it finds.

This table demonstrates how Interpolation Search makes educated guesses to quickly zero in on the specific page, making it a fast and efficient search method for uniformly distributed data.

</details>

---

### Pseudocode Example: Interpolation Search

```plaintext
// Pseudocode: Interpolation Search to find a specific page in a textbook

// Array of pages in the textbook
Set pages to array of page numbers [1, 2, 3, ..., 1000]

// The page number we are searching for
Set targetPage to 600

// Define the start and end indices
Set startIndex to 1
Set endIndex to length of pages

// While the range is valid
While startIndex is less than or equal to endIndex and targetPage is within the range Do
    // Estimate the position (interpolation)
    Set position to startIndex + ((targetPage - pages[startIndex]) * (endIndex - startIndex)) / (pages[endIndex] - pages[startIndex])

    // Check the guessed position
    If pages[position] equals targetPage Then
        Output "Page found at position: ", position
        Exit
    End If

    // Adjust the range based on the guess
    If pages[position] is less than targetPage Then
        Set startIndex to position + 1
    Else
        Set endIndex to position - 1
    End If
End While

// If the page is not found
Output "Page not found."
```

In this pseudocode:
- We start with the first and last page as the initial range.
- The position is estimated using interpolation, considering the distribution of pages.
- Depending on the comparison, we adjust the range to either the left or the right of the guessed position.

---

### Python Example: Interpolation Search

```python
# Python: Interpolation Search to find a specific page in a textbook

# List of pages in the textbook
pages = list(range(1, 1001))

# The page number we are searching for
target_page = 600

# Define the start and end indices
start_index = 0
end_index = len(pages) - 1

# This 'while' loop continues as long as two conditions are met:
# 1. The start index is less than or equal to the end index, ensuring the search range is still valid.
# 2. The target page number falls within the range defined by the pages at the start and end indices.
# If the target page is less than the page at the start index or greater than the page at the end index,
# the target cannot be in the current range, and the loop should not continue.

while start_index <= end_index and pages[start_index] <= target_page <= pages[end_index]:
    # Estimate the position (interpolation)
    position = start_index + int((float(target_page - pages[start_index]) / (pages[end_index] - pages[start_index])) * (end_index - start_index))

    # Check the guessed position
    if pages[position] == target_page:
        print(f"Page found at position: {position}")
        break

    # Adjust the range based on the guess
    if pages[position] < target_page:
        start_index = position + 1
    else:
        end_index = position - 1
else:
    # If the loop completes without finding the page
    print("Page not found.")
```

In this Python code:
- We use the same logic as in the pseudocode to find the range where the target page could be.
- The position is estimated using interpolation, taking into account the distribution of pages.
- Depending on the comparison, we adjust the range to either the left or the right of the guessed position.

---

Interpolation search is especially effective for uniformly distributed datasets, as it intelligently estimates the position of the target, leading to faster search times compared to other algorithms.
