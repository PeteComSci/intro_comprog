Counting Sort is efficient when the range of input data (i.e., `maxValue`) is not significantly larger than the number of objects to be sorted. Its complexity is O(n + k), where `n` is the number of elements in the input array and `k` is the range of the input.

### Counting Sort
```plaintext
function countingSort(array, maxValue)
    arrayLength = length(array)  // Get the number of elements in the array
    countArray = array of size (maxValue + 1), initialized to 0  // Array to store the count of each unique object

    // Store the count of each element
    for num in array
        countArray[num] = countArray[num] + 1

    // Modify countArray such that each element at each index
    // stores the sum of previous counts (cumulative count)
    for i from 1 to maxValue
        countArray[i] = countArray[i] + countArray[i - 1]

    // Build the output array by placing elements at their correct positions
    outputArray = array of size arrayLength
    for i from arrayLength - 1 to 0 step -1
        outputArray[countArray[array[i]] - 1] = array[i]
        countArray[array[i]] = countArray[array[i]] - 1

    // Copy the sorted elements to the original array
    for i from 0 to arrayLength - 1
        array[i] = outputArray[i]
    // The array is now sorted
    return array
```
**Explanation:**
- **arrayLength = length(array)**: Determine the size of the array.
- **countArray = array of size (maxValue + 1), initialized to 0**: Create an array to store the count of each unique element. The size is `maxValue + 1` because we need to include all possible values from 0 to `maxValue`.
- **for num in array**: Count each element's occurrence.
- **for i from 1 to maxValue**: Modify `countArray` such that `countArray[i]` now contains the number of elements less than or equal to `i`. This is done by accumulating the count of elements.
- **for i from arrayLength - 1 to 0 step -1**: Iterate over the original array in reverse order to build the sorted `outputArray`.
- **outputArray[countArray[array[i]] - 1] = array[i]**: Place each element in the correct position in the `outputArray` based on the cumulative count.
- **countArray[array[i]] = countArray[array[i]] - 1**: Decrease the count for each element processed.
- **for i from 0 to arrayLength - 1**: Copy the sorted elements from `outputArray` back to the original `array`.

