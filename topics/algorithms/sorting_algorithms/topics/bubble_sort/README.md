Bubble Sort is simple but not very efficient for large datasets due to its O(n²) time complexity. It performs well when the data is almost sorted because it can terminate early if no swaps are needed.

### Bubble Sort
```plaintext
function bubbleSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Outer loop - manages the number of passes
    for i from 0 to arrayLength-1
        // Inner loop - performs the comparison in each pass
        for j from 0 to arrayLength-i-2
            // Compare adjacent elements
            if array[j] > array[j+1]
                // Swap if they are in wrong order
                swap(array[j], array[j+1])
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array to know how many elements we need to sort.
- **for i from 0 to arrayLength-1**: This loop represents each pass through the array. In each pass, we "bubble up" the largest unsorted element to its correct position at the end of the array.
- **for j from 0 to arrayLength-i-2**: This loop compares adjacent elements in the array. The `-i` part ensures that we don't compare elements that have already been sorted in previous passes.
- **if array[j] > array[j+1]**: This is the key comparison step. If the current element is larger than the next element, they are out of order and should be swapped.
- **swap(array[j], array[j+1])**: This swaps the two elements to put them in the correct order.
- **return array**: The sorted array is returned after all passes are complete.
