Quick Sort is known for its performance, with average and best-case time complexities of O(n log n). However, its worst-case time complexity is O(n²), which occurs when the smallest or largest element is always chosen as the pivot. This can be mitigated by using more sophisticated pivot selection methods.

### Quick Sort
```plaintext
function quickSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Base case: If the array has 0 or 1 element, it is already sorted
    if arrayLength <= 1
        return array

    // Recursive case: Sort the array
    else
        pivot = array[0]  // Choosing the first element as the pivot
        less = []  // Elements less than pivot
        greater = []  // Elements greater than pivot

        // Partition the array into less, greater based on the pivot
        for element in array[1..arrayLength]
            if element <= pivot
                append element to less
            else
                append element to greater

        // Recursively apply quickSort to the partitions and combine with pivot
        return quickSort(less) + [pivot] + quickSort(greater)
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **if arrayLength <= 1**: The base case for recursion. If the array has zero or one element, it's already sorted.
- **pivot = array[0]**: Choose the first element as the pivot. Note: The choice of pivot can be optimized using various strategies like median-of-three or random pivot selection.
- **less = [], greater = []**: Initialize two empty arrays to hold elements less than and greater than the pivot.
- **for element in array[1..arrayLength]**: Partition the array into `less` and `greater` based on their comparison with the pivot.
- **return quickSort(less) + [pivot] + quickSort(greater)**: Recursively sort the `less` and `greater` partitions. Concatenate the sorted `less` array, pivot, and sorted `greater` array to get the full sorted array.

