Tim Sort is particularly effective for datasets that are partially sorted or have a lot of repeated elements. Its complexity is O(n log n), similar to Merge Sort, but it performs better on real-world data due to its hybrid approach.

### Tim Sort
```plaintext
function timSort(array)
    arrayLength = length(array)  // Get the number of elements in the array
    minRun = determineMinRun(arrayLength)  // Find a natural run size (a balance between Insertion and Merge Sort)

    // Sort individual sub-arrays of size minRun
    for start from 0 to arrayLength step minRun
        end = min(start + minRun - 1, arrayLength - 1)
        insertionSort(array, start, end)  // Use Insertion Sort for small segments

    // Start merging from size minRun (or the size of natural runs)
    size = minRun
    while size < arrayLength
        // Pick starting point of the left sub-array to merge
        for left from 0 to arrayLength step 2*size
            // Calculate mid and right pointers for the sub-arrays to merge
            mid = min(left + size - 1, arrayLength - 1)
            right = min(left + 2*size - 1, arrayLength - 1)

            // Merge the sub-arrays array[left..mid] & array[mid+1..right]
            if mid < right
                merge(array, left, mid, right)
        
        // Double the size for the next merge
        size = 2*size
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **minRun = determineMinRun(arrayLength)**: Compute a reasonable small segment size. This value is crucial for optimizing the performance of Tim Sort and varies based on the size of the array.
- **for start from 0 to arrayLength step minRun**: Divide the array into segments of size `minRun` and sort each segment using Insertion Sort.
- **insertionSort(array, start, end)**: A modified version of Insertion Sort that sorts the elements from `start` to `end`.
- **while size < arrayLength**: After sorting small segments, start merging them. The size of the segments to be merged doubles after each iteration.
- **for left from 0 to arrayLength step 2*size**: Determine the starting point of the left sub-array that needs to be merged.
- **mid = min(left + size - 1, arrayLength - 1), right = min(left + 2*size - 1, arrayLength - 1)**: Calculate the `mid` and `right` index to find the bounds of the sub-arrays to merge.
- **if mid < right; merge(array, left, mid, right)**: If the right index is greater than the mid index, merge the two sub-arrays.
- **size = 2*size**: Increase the size of the segments to merge in the next iteration.

