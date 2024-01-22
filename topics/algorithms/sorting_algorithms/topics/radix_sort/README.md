Radix Sort is efficient for sorting numbers or strings when the length of the numbers (number of digits) is not significantly more than the log of the number count. It outperforms comparison-based sorting algorithms like Quick Sort for large datasets with a relatively small range or when the digit size is small.

### Radix Sort
```plaintext
function radixSort(array)
    maxElement = findMax(array)  // Get the maximum element in the array
    exp = 1  // Initialize exponent representing the digit position

    // Process each digit from least significant to most significant
    while maxElement / exp > 0
        countingSortForRadix(array, exp)
        exp = exp * 10
    // The array is now sorted
    return array

function countingSortForRadix(array, exp)
    arrayLength = length(array)
    outputArray = array of size arrayLength  // Output array
    countArray = array of size 10, initialized to 0  // Count array for each digit (0-9)

    // Store count of occurrences for each digit
    for i from 0 to arrayLength - 1
        index = (array[i] / exp) mod 10
        countArray[index] = countArray[index] + 1

    // Change countArray to contain the cumulative count
    for i from 1 to 9
        countArray[i] = countArray[i] + countArray[i - 1]

    // Build the output array using the cumulative count
    for i from arrayLength - 1 to 0 step -1
        index = (array[i] / exp) mod 10
        outputArray[countArray[index] - 1] = array[i]
        countArray[index] = countArray[index] - 1

    // Copy the sorted outputArray back to the original array
    for i from 0 to arrayLength - 1
        array[i] = outputArray[i]
```
**Explanation:**
- **maxElement = findMax(array)**: Find the maximum element to know the number of digits.
- **exp = 1**: Represents the current digit position we are sorting by, starting with the least significant digit.
- **while maxElement / exp > 0**: Continue until we've processed all digits.
- **countingSortForRadix(array, exp)**: Perform counting sort for each digit represented by `exp`.
- **countArray = array of size 10, initialized to 0**: Since digits range from 0-9, we need 10 slots to count each digit.
- **for i from 0 to arrayLength - 1**: Count the occurrences of each digit in the `exp` position.
- **index = (array[i] / exp) mod 10**: Calculate the index in `countArray` for the digit in the `exp` position.
- **for i from 1 to 9**: Modify `countArray` to contain the cumulative count.
- **for i from arrayLength - 1 to 0 step -1**: Build the sorted `outputArray` using the cumulative count, ensuring stability by iterating in reverse.
- **array[i] = outputArray[i]**: Copy the sorted `outputArray` back to the original `array`.

