Shell Sort is particularly effective for medium-sized arrays and improves upon the performance of Insertion Sort by allowing the exchange of elements that are far apart, thereby reducing the total number of movements required to sort the entire array.

### Shell Sort
```plaintext
function shellSort(array)
    arrayLength = length(array)  // Get the number of elements in the array
    gap = arrayLength / 2  // Initialize gap size

    // Start with a big gap, then reduce the gap until it becomes 0
    while gap > 0
        // Do a "gapped" insertion sort for this gap size
        // The first gap elements are already in gapped order, keep adding one more element until the entire array is gap sorted
        for i from gap to arrayLength - 1
            // Add array[i] to the elements that have been gap sorted
            temp = array[i]
            // Shift earlier gap-sorted elements up until the correct location for array[i] is found
            j = i
            while j >= gap and array[j - gap] > temp
                array[j] = array[j - gap]
                j = j - gap
            
            // Put temp (the original array[i]) in its correct location
            array[j] = temp
        gap = gap / 2  // Reduce the gap for the next round
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **gap = arrayLength / 2**: Start with a large gap, then reduce it. The exact gap sequence can vary, and different sequences can lead to different performance characteristics.
- **while gap > 0**: Continue until the gap size reduces to 0. Each pass will sort the array elements for the given gap size.
- **for i from gap to arrayLength - 1**: Iterate through the array, starting from the first element that is `gap` distance away from the start of the array.
- **temp = array[i]**: Store the current element for comparison.
- **while j >= gap and array[j - gap] > temp**: Move each element `gap` positions ahead until the correct spot for `temp` is found.
- **array[j] = temp**: Place `temp` in its correct position within the sorted subsequence.
- **gap = gap / 2**: Reduce the gap size for the next iteration. Different gap reduction strategies can lead to different performances.

