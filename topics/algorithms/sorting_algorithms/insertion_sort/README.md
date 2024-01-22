Insertion Sort is efficient for small datasets or datasets that are mostly sorted. It has a time complexity of O(n²) in the worst case but performs well in the best case (O(n) when the array is already sorted) because it only requires a constant number of comparisons and swaps for each element.

### Insertion Sort
```plaintext
function insertionSort(array)
    arrayLength = length(array)  // Get the number of elements in the array

    // Outer loop - marks the unsorted element at the current iteration
    for i from 1 to arrayLength-1
        // The current element to be inserted into the sorted portion of the array
        currentElement = array[i]
        // Start comparing with the element before the current one
        j = i - 1

        // Inner loop - find the correct position for the currentElement in the sorted portion
        // Move elements of the sorted portion that are greater than the currentElement to one position ahead
        while j >= 0 and array[j] > currentElement
            array[j + 1] = array[j]
            j = j - 1

        // Insert the currentElement at its correct position
        array[j + 1] = currentElement
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array to know how many elements we need to sort.
- **for i from 1 to arrayLength-1**: This loop iterates through each element of the array, treating each element as the currentElement to be inserted into the sorted portion.
- **currentElement = array[i]**: This is the element we are currently trying to insert into the sorted portion of the array.
- **j = i - 1**: Initialize `j` to point to the end of the sorted portion of the array.
- **while j >= 0 and array[j] > currentElement**: This loop moves elements that are greater than `currentElement` one position ahead to make room for inserting `currentElement`.
- **array[j + 1] = array[j]**: Move the element at `j` to the next position.
- **array[j + 1] = currentElement**: Insert `currentElement` at its correct position in the sorted portion.
- **return array**: The array is now sorted and returned.

