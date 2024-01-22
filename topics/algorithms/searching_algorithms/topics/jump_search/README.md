# Jump Search

Jump Search combines the principles of a linear search and a binary search. It aims to reduce the number of comparisons by jumping ahead by fixed steps, instead of checking every element or dividing the list into halves. The key to its efficiency lies in choosing the optimal jump size.

---

1. **Minimizes the Total Number of Steps:** The total number of steps in jump search (the number of jumps plus the number of linear searches) becomes approximately √n (where n is the size of the list) if the jump size is chosen as √n. This size balances out the number of jumps and the size of the linear search space.

2. **Optimal in Worst-Case Scenario:** In the worst-case scenario, the element being searched for is just after the last jumped index, or not present at all. In such cases, having a jump size of √n ensures that the total number of comparisons (jumps + linear search steps) is still in the order of √n.

3. **Practical and Easy to Implement:** Calculating the square root is computationally simple and doesn't require additional data structures or memory, making it practical for various applications.

---

<details>

<summary>Example: Why Square Root as Jump Size?</summary>

Imagine you have a sorted list of 100 elements. You're looking for a specific item in this list.

#### Without Jump Search (Linear Search):
- You might have to check up to 100 elements one by one in the worst case.
- Number of comparisons in the worst case: 100.

#### With Jump Search:
- Let's choose the jump size. If you pick the square root of the list's length as the jump size, in this case, the square root of 100 is 10. So, you decide to jump every 10 elements.

**Jumping Phase:**
- You check the 10th, 20th, 30th... elements. This is much faster than checking each element one by one.
- If the list has 100 elements, you only make a maximum of 10 jumps (because 100/10 = 10).

**Linear Search Phase (After Jumping):**
- In the worst case, the element you are looking for is just before the next jump point. For example, if it's at position 19, you jump to the 20th element and realize you've jumped too far. Now you perform a linear search backward from the 20th to the 11th element.
- So, in the worst case, you perform up to 10 comparisons in the linear search phase after jumping.

**Total Comparisons:**
- Jumps: 10
- Linear search after jumping: 10
- Total: 20 comparisons in the worst case, which is much less than 100 comparisons needed for a linear search.

This illustrates why using the square root of the list's length as the jump size is efficient. It's a balance between not jumping too far (to avoid missing the target) and not making too small jumps (to avoid too many comparisons). This way, Jump Search reduces the number of comparisons significantly compared to a linear search, especially in larger lists, making it much faster while still being simple to implement.

</details>

---

Now, let's incorporate this rationale into the pseudocode and Python example for clarity.

### Pseudocode Example: Jump Search

```plaintext
// Pseudocode: Jump Search to find a song in an alphabetically organized playlist

// Sorted list of songs
Set songs to ["A Sky Full of Stars", "Bohemian Rhapsody", "Come As You Are", "Don't Stop Believin'", "Eye of the Tiger"]

// The song we are searching for
Set targetSong to "Come As You Are"

// Determine the optimal jump size, the square root of the list's length
// The square root balances the number of jumps and linear search steps
Set jumpSize to square root of length of songs

// The starting point of the search
Set startIndex to 0

// Jumping ahead in fixed intervals
// This allows us to skip checking every element and reduces comparisons
While startIndex < length of songs and songs[startIndex] is less than targetSong Do
    Set startIndex to startIndex + jumpSize
End While

// Performing linear search in the smaller interval
// After jumping, we conduct a more detailed search in a smaller section
For i from startIndex - jumpSize to minimum(startIndex, length of songs) Do
    If songs[i] equals targetSong Then
        Output "Song found at position: ", i
        Exit
    End If
End For

// If the song is not found, we output the result
Output "Song not found."
```

---

### Python Example: Jump Search

```python
# Python: Jump Search to find a song in an alphabetically organized playlist

import math

# Sorted list of songs
songs = ["A Sky Full of Stars", "Bohemian Rhapsody", "Come As You Are", "Don't Stop Believin'", "Eye of the Tiger"]

# The song we are searching for
target_song = "Come As You Are"

# Determine the optimal jump size, the square root of the list's length
# The square root is chosen to balance the number of jumps and linear search steps
jump_size = int(math.sqrt(len(songs)))

# The starting point of the search
start_index = 0

# Jumping ahead in fixed intervals to reduce comparisons
while start_index < len(songs) and songs[start_index] < target_song:
    start_index += jump_size

# Performing linear search in the smaller interval for detailed checking
for i in range(start_index - jump_size, min(start_index, len(songs))):
    if songs[i] == target_song:
        print(f"Song found at position: {i}")
        break
else:
    # If the loop completes without finding the song, we output the result
    print("Song not found.")
```
