Merge Sort is particularly effective for large datasets because its time complexity is consistently O(n log n), regardless of the initial order of the elements. It's also stable (does not change the relative order of elements with equal keys) but requires additional space proportional to the array size for the merging process.

### Merge Sort
```plaintext
function mergeSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Base case: a single element is always sorted
    if arrayLength > 1
        mid = arrayLength / 2  // Find the middle point to divide the array into two halves
        leftHalf = array[0..mid]  // Left subarray
        rightHalf = array[mid..arrayLength]  // Right subarray

        // Recursively sort both halves
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        // Merge the sorted halves
        merge(array, leftHalf, rightHalf)
    // The array is now sorted
    return array

function merge(array, leftHalf, rightHalf)
    // Initialize pointers for leftHalf, rightHalf, and array
    i = 0; j = 0; k = 0

    // Traverse and merge the sorted arrays
    while i < length(leftHalf) and j < length(rightHalf)
        if leftHalf[i] <= rightHalf[j]
            array[k] = leftHalf[i]
            i = i + 1
        else
            array[k] = rightHalf[j]
            j = j + 1
        k = k + 1

    // If there are remaining elements in leftHalf, add them to array
    while i < length(leftHalf)
        array[k] = leftHalf[i]
        i = i + 1; k = k + 1

    // If there are remaining elements in rightHalf, add them to array
    while j < length(rightHalf)
        array[k] = rightHalf[j]
        j = j + 1; k = k + 1
    // The array is now merged and sorted
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **if arrayLength > 1**: The base case for recursion. If the array has only one element, it's already sorted.
- **mid = arrayLength / 2**: Find the middle of the array to divide it into two halves.
- **leftHalf = array[0..mid], rightHalf = array[mid..arrayLength]**: Split the array into left and right halves.
- **mergeSort(leftHalf), mergeSort(rightHalf)**: Recursively sort the two halves.
- **merge(array, leftHalf, rightHalf)**: Merge the sorted halves into a single sorted array.
- **while i < length(leftHalf) and j < length(rightHalf)**: Traverse both halves and merge them into the main array in sorted order.
- **while i < length(leftHalf)**: If there are remaining elements in leftHalf, add them to the main array.
- **while j < length(rightHalf)**: If there are remaining elements in rightHalf, add them to the main array.

