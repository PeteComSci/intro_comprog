Selection Sort has a time complexity of O(n²) due to the nested loops, similar to Bubble Sort. However, it performs fewer swaps compared to Bubble Sort, which can be beneficial when the swap operation is costly.

### Selection Sort
```plaintext
function selectionSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Outer loop - iterate through the entire array
    for i from 0 to arrayLength-1
        // Assume the minimum element is the first unsorted element
        minIndex = i

        // Inner loop - find the minimum element in the unsorted portion of the array
        for j from i+1 to arrayLength-1
            // Compare the current element to the current minimum
            if array[j] < array[minIndex]
                // Update minIndex if a new minimum is found
                minIndex = j

        // Swap the minimum element with the first unsorted position
        if i != minIndex
            swap(array[i], array[minIndex])
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array to know how many elements we need to sort.
- **for i from 0 to arrayLength-1**: This loop represents the current position in the array where we intend to place the smallest element found in the unsorted portion.
- **minIndex = i**: Initially assume that the first unsorted element is the minimum.
- **for j from i+1 to arrayLength-1**: Iterate through the unsorted portion of the array to find the smallest element.
- **if array[j] < array[minIndex]**: If we find an element smaller than the current assumed minimum, we update `minIndex` to the index of this new minimum.
- **if i != minIndex; swap(array[i], array[minIndex])**: After finding the minimum element in the unsorted portion, swap it with the first unsorted element. The check `i != minIndex` ensures that we don't swap an element with itself, which is unnecessary.
- **return array**: Return the sorted array after placing all elements in their correct positions.

