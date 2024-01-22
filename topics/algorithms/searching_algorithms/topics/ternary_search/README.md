# Ternary Search

Ternary search is a divide-and-conquer search algorithm that, like binary search, is used to find the position of an element in a sorted array. However, ternary search divides the array into three parts, making it potentially faster in certain situations because it reduces the search interval more rapidly.

---

<details>
<summary>Example: Ternary Search for Finding the Highest Point</summary>

Imagine you're looking for the highest point on a smooth, gently sloping hill. The hill's profile can be represented as a sorted array of heights, and your goal is to find the peak, the highest point.

Here's how Ternary Search can efficiently find this peak:

1. **Initial Range:**
   - The hill extends from the starting point (index 0) to the ending point (the last index in the array).

2. **Divide the Range:**
   - Instead of dividing the range into two parts (as in binary search), you divide it into three parts. You do this by finding two midpoints, `mid1` and `mid2`, which split the range into three equal parts.

3. **Compare Heights at Midpoints:**
   - Check the heights at `mid1` and `mid2`.
   - If the height at `mid1` is greater than at `mid2`, the peak must be between the start and `mid2`.
   - If the height at `mid2` is greater than at `mid1`, the peak must be between `mid1` and the end.
   - If heights at `mid1` and `mid2` are equal, the peak can be anywhere between `mid1` and `mid2`.

4. **Eliminate One-Third of the Range:**
   - Based on the comparisons, eliminate one-third of the range where the peak cannot be.
   - If the peak is between the start and `mid2`, focus on this range. Similarly, if the peak is between `mid1` and the end, focus on that range.

5. **Repeat the Process:**
   - Continue this process of dividing the range and eliminating one-third until you've narrowed it down to a single point, the highest point on the hill.

In this example, Ternary Search uses the nature of the hill's slope (sorted array) to intelligently and efficiently find the peak, significantly reducing the area to be searched in each step.

</details>

---

<details>
<summary>Trace Table</summary>
A trace table helps visualize the steps taken by the Ternary Search algorithm in finding the highest point on the hill.

Given a hill profile represented as a sorted array of heights, let's assume the peak is around the middle:

| Step | Range                         | Action                                                     | Description                                           |
|------|-------------------------------|------------------------------------------------------------|-------------------------------------------------------|
| 1    | Full range                    | Find `mid1` and `mid2`                                     | Divide the range into three equal parts.              |
| 2    | Check heights at `mid1` and `mid2` | Compare heights                                            | Determine which third of the range to eliminate.      |
| 3    | Adjust range                  | Focus on the range between `mid1` and `mid2`               | Eliminate one-third of the range where the peak isn't.|
| 4    | Repeat steps 1-3              | Continue until the range is narrowed down to a single point| Find the exact position of the peak.                  |

This table demonstrates how Ternary Search makes intelligent decisions to quickly focus in on the highest point, making it a fast and efficient search method for finding peaks in sorted datasets.

</details>

---

### Pseudocode Example: Ternary Search

```plaintext
// Pseudocode: Ternary Search to find the highest point

// Array representing the hill's profile (heights)
Set heights to array of heights [..]

// The range we are searching within
Set startIndex to 0
Set endIndex to length of heights - 1

// While there is more than one element in the range
While startIndex < endIndex Do
    // Find the midpoints
    Set mid1 to startIndex + (endIndex - startIndex) / 3
    Set mid2 to endIndex - (endIndex - startIndex) / 3

    // Compare heights at midpoints
    If heights[mid1] < heights[mid2] Then
        // Focus on the range from mid1 to endIndex
        Set startIndex to mid1 + 1
    Else
        // Focus on the range from startIndex to mid2
        Set endIndex to mid2 - 1
    End If
End While

// The highest point is at startIndex (or endIndex, as they are the same at this point)
Output "The highest point is at position: ", startIndex
```

In this pseudocode:
- We start with the full range of the hill.
- We find two midpoints (`mid1` and `mid2`) that divide the range into three parts.
- Depending on the comparison of heights at `mid1` and `mid2`, we adjust the range to either the left or right third.
- The process repeats, narrowing down the range until we find the highest point.

---

### Python Example: Ternary Search

```python
# Python: Ternary Search to find the highest point

# Array representing the hill's profile (heights)
heights = [...]

# The range we are searching within
start_index = 0
end_index = len(heights) - 1

# While there is more than one element in the range
while start_index < end_index:
    # Find the midpoints
    mid1 = start_index + (end_index - start_index) // 3
    mid2 = end_index - (end_index - start_index) // 3

    # Compare heights at midpoints
    if heights[mid1] < heights[mid2]:
        # Focus on the range from mid1 to endIndex
        start_index = mid1 + 1
    else:
        # Focus on the range from startIndex to mid2
        end_index = mid2 - 1

# The highest point is at start_index (or end_index, as they are the same at this point)
print(f"The highest point is at position: {start_index}")
```

In this Python code:
- We use the same logic as in the pseudocode to narrow down the range where the highest point could be.
- Depending on the comparison of heights at `mid1` and `mid2`, we adjust the range to either the left or right third.
- The process repeats, narrowing down the range until we find the highest point.

---

Ternary search is an efficient algorithm for finding the maximum or minimum in a unimodal function or finding the peak in a strictly increasing or decreasing array. By dividing the search range into three parts and eliminating one-third in each step, it often finds the target faster than binary search.
